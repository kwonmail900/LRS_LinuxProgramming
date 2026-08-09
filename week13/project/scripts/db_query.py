#!/usr/bin/env python3
# scripts/db_query.py — 센서 데이터 조회 및 통계
import sqlite3

DB_PATH = "data/sensor.db"

with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    # 전체 건수
    total = cursor.execute("SELECT COUNT(*) FROM sensor_data").fetchone()[0]
    print(f"전체 데이터: {total}건")
    
    # 평균/최대/최소
    cursor.execute("SELECT AVG(raw_value), MAX(raw_value), MIN(raw_value) FROM sensor_data")
    avg, mx, mn = cursor.fetchone()
    print(f"RAW 평균: {avg:.1f}, 최대: {mx}, 최소: {mn}")
    
    # 센서 타입별 통계
    cursor.execute("SELECT sensor_type, COUNT(*), AVG(lux) FROM sensor_data GROUP BY sensor_type")
    for row in cursor.fetchall():
        print(f"  {row[0]}: {row[1]}건, 평균 Lux: {row[2]:.1f}")
    
    # 최근 5건
    print("\n최근 5건:")
    cursor.execute("SELECT * FROM sensor_data ORDER BY id DESC LIMIT 5")
    for row in cursor.fetchall():
        print(f"  ID:{row[0]} {row[1]} Raw:{row[2]} Lux:{row[3]:.1f}")
