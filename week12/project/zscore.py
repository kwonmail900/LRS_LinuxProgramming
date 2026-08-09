#!/usr/bin/env python3
# 이상치 탐지 — Z-score 방법
#   z = (x - mean) / std   ->   |z| > 2 (또는 3) 이면 이상치
#   |z|>2 : 정규분포 95.4% 범위 밖 / |z|>3 : 99.7% 범위 밖
import pandas as pd
import sqlite3
import numpy as np

# --- 데이터 로드 (DB -> DataFrame) ---
conn = sqlite3.connect("data/sensor.db")
df = pd.read_sql("SELECT * FROM sensor_data", conn)
conn.close()

# --- Z-score 계산: 평균에서 표준편차의 몇 배만큼 떨어져 있는지 ---
mean = df["raw_value"].mean()
std = df["raw_value"].std()
df["z_score"] = (df["raw_value"] - mean) / std

# --- 이상치 탐지 (|z| > 2) ---
outliers_z = df[df["z_score"].abs() > 2]
print(f"Z-score 이상치: {len(outliers_z)}건")
print(outliers_z[["id", "raw_value", "z_score"]])

# --- 정상 데이터만 추출 ---
normal = df[df["z_score"].abs() <= 2]
print(f"정상: {len(normal)}건, 이상치: {len(outliers_z)}건")
