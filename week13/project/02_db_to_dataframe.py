#!/usr/bin/env python3
# 12주차 1교시 - slide 7, 8
# SQLite3 DB -> pandas DataFrame (핵심 연결)
import pandas as pd
import sqlite3

# DB에서 직접 DataFrame으로 로드
conn = sqlite3.connect("data/sensor.db")
df = pd.read_sql("SELECT * FROM sensor_data", conn)
conn.close()

print(f"Shape: {df.shape}")   # (50, 5)
print(df.head())              # 처음 5행
print(df.describe())          # 통계 요약 (count/mean/std/min/사분위/max)
print(df.info())              # 각 열 데이터 타입 + non-null 개수
