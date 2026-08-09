#!/usr/bin/env python3
# 12주차 1교시 - slide 10
# WSL 대화형 실습 세션을 스크립트로 정리
#   $ cd ~/linux_lab/project && python3
import pandas as pd
import sqlite3

conn = sqlite3.connect("data/sensor.db")
df = pd.read_sql("SELECT * FROM sensor_data", conn)
conn.close()

# 확인
print(df.shape)        # (50, 5)
print(df.head())       # 처음 5행
print(df.describe())   # 통계 요약

# 가공
print(df[df["raw_value"] > 3000])                        # 필터링
print(df.sort_values("lux", ascending=False).head(5))    # 정렬
print(df.groupby("sensor_type")["raw_value"].mean())     # 그룹별 평균

# 저장 (index=False: 행 인덱스는 파일에 쓰지 않음)
df.to_csv("data/analysis.csv", index=False)
