#!/bin/bash
# scripts/run_pipeline.sh — 10주차 3교시 slide 9
# Step 2 파이프라인 자동 실행 (빌드 + 수신기 + 센서)
set -euo pipefail
cd $(dirname $0)/..
make

# 수신기를 백그라운드로 실행
./ipc_receiver &
RECEIVER_PID=$!
sleep 1  # FIFO 생성 대기

# 센서 실행 (인자: 측정 횟수, 기본 30)
./sensor_sim ${1:-30}

# 수신기 종료 대기
wait $RECEIVER_PID

echo "=== 파이프라인 완료 ==="
echo "데이터: $(wc -l < data/sensor_data.csv) 라인"
