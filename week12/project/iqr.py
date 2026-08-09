#!/usr/bin/env python3
# 이상치 탐지 — IQR (Interquartile Range) 방법
#   Q1(25%), Q3(75%), IQR = Q3 - Q1
#   이상치: Q1 - 1.5*IQR 미만 또는 Q3 + 1.5*IQR 초과  (Tukey's Fences)
#   * 박스플롯 수염(whisker) 범위와 동일한 기준
#   * 중앙값/사분위수 기반이라 극단값에 강건(robust)
import pandas as pd
import sqlite3

# --- 데이터 로드 (DB -> DataFrame) ---
conn = sqlite3.connect("data/sensor.db")
df = pd.read_sql("SELECT * FROM sensor_data", conn)
conn.close()

# --- 사분위수 & IQR ---
Q1 = df["raw_value"].quantile(0.25)   # 하위 25%
Q3 = df["raw_value"].quantile(0.75)   # 상위 25%
IQR = Q3 - Q1                          # 중앙 50% 범위

# --- 이상치 경계 (1.5 x IQR) ---
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# --- 이상치 탐지 ---
outliers_iqr = df[(df["raw_value"] < lower) | (df["raw_value"] > upper)]
print(f"IQR 이상치: {len(outliers_iqr)}건")
print(f"정상 범위: {lower:.0f} ~ {upper:.0f}")
