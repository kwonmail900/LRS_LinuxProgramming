#!/usr/bin/env python3
# 이동평균 (Moving Average) — 시계열 노이즈 제거 / 추세 파악
#   SMA(단순): rolling(N).mean()  — 최근 N개 산술평균, 처음 N-1개는 NaN
#   EMA(지수): ewm(span=N).mean() — 최근 값에 더 큰 가중치 (변화에 빠르게 반응)
import matplotlib
matplotlib.use("Agg")   # WSL: GUI 없이 파일로 저장 (pyplot import 전에 설정)
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

# --- 데이터 로드 (DB -> DataFrame) ---
conn = sqlite3.connect("data/sensor.db")
df = pd.read_sql("SELECT * FROM sensor_data", conn)
conn.close()

# --- 단순 이동평균 (SMA) ---
df["sma_5"] = df["raw_value"].rolling(window=5).mean()
df["sma_10"] = df["raw_value"].rolling(window=10).mean()

# --- 지수 이동평균 (EMA) — 최근 값에 더 큰 가중치 ---
df["ema_5"] = df["raw_value"].ewm(span=5).mean()

# --- 시각화 (원본 + SMA + EMA 겹쳐 그리기) ---
plt.figure(figsize=(12, 5))
plt.plot(df["id"], df["raw_value"], "b-", alpha=0.3, label="원본")
plt.plot(df["id"], df["sma_5"], "r-", linewidth=2, label="SMA(5)")
plt.plot(df["id"], df["ema_5"], "g-", linewidth=2, label="EMA(5)")
plt.legend()
plt.title("Moving Averages")
plt.savefig("data/moving_average.png", dpi=150)
print("그래프 저장: data/moving_average.png")
