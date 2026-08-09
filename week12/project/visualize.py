#!/usr/bin/env python3
# scripts/visualize.py — 12주차 2교시 시각화 통합 스크립트
# (slide 3 시계열 + slide 4 히스토그램/박스플롯 + slide 5 2x2 대시보드)
# 실행: python3 scripts/visualize.py  ->  data/ 에 PNG 4개 생성
import matplotlib
matplotlib.use("Agg")   # WSL: GUI 없이 파일로 저장 (pyplot import 전에 설정)
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

# --- 데이터 로드 (SQLite3 DB -> pandas DataFrame) ---
conn = sqlite3.connect("data/sensor.db")
df = pd.read_sql("SELECT * FROM sensor_data", conn)
conn.close()

# --- 1) 시계열 그래프 (slide 3) ---
plt.figure(figsize=(12, 4))
plt.plot(df["id"], df["raw_value"], "b-", linewidth=0.8, label="RAW")
plt.xlabel("Measurement ID")
plt.ylabel("Raw Value (0-4095)")
plt.title("CDS Sensor Raw Values Over Time")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("data/sensor_timeseries.png", dpi=150)
plt.close()
print("그래프 저장: data/sensor_timeseries.png")

# --- 2) 히스토그램 (slide 4) ---
plt.figure(figsize=(6, 4))
plt.hist(df["raw_value"], bins=20, color="steelblue", edgecolor="white")
plt.xlabel("Raw Value")
plt.ylabel("Frequency")
plt.title("Distribution of Sensor Values")
plt.savefig("data/histogram.png")
plt.close()
print("그래프 저장: data/histogram.png")

# --- 3) 박스플롯 (slide 4) ---
plt.figure(figsize=(6, 4))
plt.boxplot(df["raw_value"], vert=True, patch_artist=True)
plt.ylabel("Raw Value")
plt.title("Sensor Value Box Plot")
plt.savefig("data/boxplot.png")
plt.close()
print("그래프 저장: data/boxplot.png")

# --- 4) 2x2 종합 대시보드 (slide 5) ---
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0, 0].plot(df["id"], df["raw_value"], "b-", linewidth=0.5)
axes[0, 0].set_title("Time Series")
axes[0, 1].hist(df["raw_value"], bins=20, color="steelblue")
axes[0, 1].set_title("Distribution")
axes[1, 0].boxplot(df["raw_value"], patch_artist=True)
axes[1, 0].set_title("Box Plot")
df["ma"] = df["raw_value"].rolling(window=5).mean()   # 5개 이동평균
axes[1, 1].plot(df["id"], df["raw_value"], "b-", alpha=0.3)
axes[1, 1].plot(df["id"], df["ma"], "r-", linewidth=2, label="MA(5)")
axes[1, 1].set_title("Moving Average")
axes[1, 1].legend()
fig.tight_layout()
fig.savefig("data/sensor_dashboard.png", dpi=150)
plt.close(fig)
print("그래프 저장: data/sensor_dashboard.png")
