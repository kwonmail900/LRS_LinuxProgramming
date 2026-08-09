#!/usr/bin/env python3
# DB → pandas → 통계/이상치/이동평균 → 대시보드 PNG + JSON 리포트
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd, sqlite3, numpy as np, json

DB = "data/sensor.db"    # 매직 스트링 제거: 경로를 상수로 분리
OUT = "data"

# 1. 데이터 로드
conn = sqlite3.connect(DB)
df = pd.read_sql("SELECT * FROM sensor_data", conn)
conn.close()
print(f"[분석] {len(df)}건 로드 완료")

# 2. 기본 통계 (NumPy int64/float64 → JSON 위해 float()/int() 변환)
stats = {
    "total": len(df),
    "mean": float(df["raw_value"].mean()),
    "std": float(df["raw_value"].std()),
    "max": int(df["raw_value"].max()),
    "min": int(df["raw_value"].min()),
}

# 3. 이상치 탐지 (Z-score)
df["z_score"] = (df["raw_value"] - stats["mean"]) / stats["std"]
outliers = df[df["z_score"].abs() > 2]
stats["outliers"] = len(outliers)

# 4. 이동평균
df["sma5"] = df["raw_value"].rolling(5).mean()

# 5. 종합 그래프 (2x2)
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0,0].plot(df["id"], df["raw_value"], "b-", lw=0.5)
axes[0,0].set_title("Time Series")
axes[0,1].hist(df["raw_value"], bins=20, color="steelblue", ec="w")
axes[0,1].set_title("Distribution")
axes[1,0].boxplot(df["raw_value"], patch_artist=True)
axes[1,0].set_title("Box Plot")
axes[1,1].plot(df["id"], df["raw_value"], "b-", alpha=0.3)
axes[1,1].plot(df["id"], df["sma5"], "r-", lw=2, label="MA(5)")
axes[1,1].legend(); axes[1,1].set_title("Moving Average")
fig.suptitle("Sensor Data Analysis Dashboard", fontsize=14)
fig.tight_layout(); fig.savefig(f"{OUT}/dashboard.png", dpi=150)

# 6. JSON 리포트 저장 (Flask에서 사용)
with open(f"{OUT}/report.json", "w") as f:
    json.dump(stats, f, indent=2)

# 7. 텍스트 리포트 출력
print(f"\n=== 센서 데이터 분석 리포트 ===")
print(f"전체: {stats['total']}건")
print(f"평균: {stats['mean']:.1f}, 표준편차: {stats['std']:.1f}")
print(f"최대: {stats['max']}, 최소: {stats['min']}")
print(f"이상치(|z|>2): {stats['outliers']}건")
print(f"\n그래프: {OUT}/dashboard.png")
print(f"리포트: {OUT}/report.json")
