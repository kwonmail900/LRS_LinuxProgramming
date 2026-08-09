// src/sensor_main.c — FIFO를 통해 센서 데이터 전송
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include "sensor.h"

#define FIFO_PATH "/tmp/sensor_fifo"

int main(int argc, char *argv[]) {
    int count = (argc > 1) ? atoi(argv[1]) : 30;
    sensor_init();
    
    // FIFO 열기 (쓰기 모드 — 수신기가 열릴 때까지 블로킹)
    int fd = open(FIFO_PATH, O_WRONLY);
    if (fd < 0) { perror("open FIFO"); return 1; }

    for (int i = 1; i <= count; i++) {
        SensorData data = sensor_read(i);
        write(fd, &data, sizeof(SensorData));  // 구조체 직접 전송
        sensor_print(&data);  // 화면에도 출력
        usleep(200000);       // 0.2초 간격
    }

    close(fd);
    printf("[센서] %d회 전송 완료\n", count);
    return 0;
}
