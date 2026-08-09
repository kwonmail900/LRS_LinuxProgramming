#!/usr/bin/env python3
# scripts/db_create.py — 센서 데이터 DB 초기화
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sensor.db")

def create_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS sensor_data")
        cursor.execute("""
            CREATE TABLE sensor_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sensor_type TEXT NOT NULL,
                raw_value INTEGER NOT NULL,
                lux REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        print(f"[DB] 테이블 생성 완료: {DB_PATH}")

if __name__ == "__main__":
    create_db()
