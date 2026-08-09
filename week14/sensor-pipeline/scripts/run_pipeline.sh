#!/bin/bash
# scripts/run_pipeline.sh — 센서 파이프라인 전체 실행 (14주차 2교시 slide 4)
set -euo pipefail
cd "$(dirname "$0")/.."
COUNT=${1:-100}

echo "╔══════════════════════════════════════╗"
echo "║  센서 데이터 파이프라인 (Step 1~6)   ║"
echo "╚══════════════════════════════════════╝"

echo "▶ [Step 0] Build..."
make -s

echo "▶ [Step 1~3] Sensor → IPC → DB..."
python3 scripts/db_create.py
./ipc_receiver & RPID=$!; sleep 1
./sensor_sim $COUNT
wait $RPID 2>/dev/null

echo "▶ [Step 4] AI Analysis..."
python3 scripts/analyze.py
[ -d web/static ] && cp data/dashboard.png web/static/

echo "▶ [Complete] Results:"
echo "  DB: data/sensor.db ($(du -h data/sensor.db | cut -f1))"
echo "  Graph: data/dashboard.png"
echo "  Report: data/report.json"
echo "  Web: make web (Flask 서버 시작)"
