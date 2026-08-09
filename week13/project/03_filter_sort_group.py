#!/usr/bin/env python3
# 12주차 1교시 - slide 9
# 데이터 가공: 필터링 / 정렬 / 그룹화 / 파생변수 / 결측치
import pandas as pd
import sqlite3

conn = sqlite3.connect("data/sensor.db")
df = pd.read_sql("SELECT * FROM sensor_data", conn)
conn.close()

# 필터링 (Boolean Indexing)
high = df[df["raw_value"] > 3000]
cds = df[df["sensor_type"] == "CDS"]

# 정렬
sorted_df = df.sort_values("raw_value", ascending=False)

# 그룹화 & 집계 (SQL GROUP BY 와 동일)
grouped = df.groupby("sensor_type")["raw_value"].agg(["mean", "max", "min", "count"])

# 파생 변수 추가 (apply + lambda)
df["category"] = df["raw_value"].apply(
    lambda x: "밝음" if x > 3000 else ("보통" if x > 1000 else "어두움"))

# 결측치 처리
print(df.isnull().sum())   # 열별 결측치 개수
df_clean = df.dropna()     # 결측치 행 삭제
df_filled = df.fillna(0)   # 결측치를 0으로 채움
