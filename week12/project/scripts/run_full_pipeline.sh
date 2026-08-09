#!/bin/bash
# scripts/run_full_pipeline.sh — 12주차 3교시 slide 7
# Step 1~4 통합 실행 (센서 → IPC → DB → 분석/시각화)
set -euo pipefail
cd $(dirname $0)/..

echo "=== Step 0: Build ==="
make

echo "=== Step 1~2: Sensor → IPC → Receiver ==="
python3 scripts/db_create.py  # DB 초기화
./ipc_receiver &
RPID=$!; sleep 1
./sensor_sim ${1:-100}
wait $RPID

echo "=== Step 4: Analysis ==="
python3 scripts/analyze.py

echo "=== Pipeline Complete ==="
echo "DB: data/sensor.db"
echo "Graph: data/dashboard.png"
echo "Report: data/report.json"
