// src/receiver_main.c — FIFO → SQLite3 DB 저장
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sqlite3.h>
#include "sensor.h"

#define FIFO_PATH "/tmp/sensor_fifo"
#define DB_PATH   "data/sensor.db"

int main() {
    unlink(FIFO_PATH);
    mkfifo(FIFO_PATH, 0666);
    
    // SQLite3 DB 열기
    sqlite3 *db;
    sqlite3_open(DB_PATH, &db);
    sqlite3_exec(db, "CREATE TABLE IF NOT EXISTS sensor_data("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "sensor_type TEXT, raw_value INTEGER, lux REAL,"
        "timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)", 0, 0, 0);
    
    // FIFO 열기
    int fd = open(FIFO_PATH, O_RDONLY);
    SensorData data;
    int count = 0;
    
    // 준비된 문장 (Prepared Statement)
    sqlite3_stmt *stmt;
    sqlite3_prepare_v2(db,
        "INSERT INTO sensor_data (sensor_type, raw_value, lux) VALUES (?,?,?)",
        -1, &stmt, 0);
    
    while (read(fd, &data, sizeof(SensorData)) > 0) {
        sqlite3_bind_text(stmt, 1, data.type, -1, SQLITE_STATIC);
        sqlite3_bind_int(stmt, 2, data.raw_value);
        sqlite3_bind_double(stmt, 3, data.converted);
        sqlite3_step(stmt);
        sqlite3_reset(stmt);
        sensor_print(&data);
        count++;
    }
    
    sqlite3_finalize(stmt);
    close(fd);
    unlink(FIFO_PATH);
    sqlite3_close(db);
    printf("[수신기] %d건 DB 저장 완료\n", count);
    
    return 0;
}
