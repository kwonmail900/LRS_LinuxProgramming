#!/bin/bash
# Step 1~5 통합 실행 (센서 → IPC → DB → 분석 → Flask 웹)
# 12주차 run_full_pipeline.sh 확장: dashboard.png를 static/으로 복사 + Flask 서버 시작
set -euo pipefail
cd $(dirname $0)/..

# Step 0: 빌드
make

# Step 1~3: 센서 → IPC → DB
python3 scripts/db_create.py
./ipc_receiver & RPID=$!; sleep 1
./sensor_sim ${1:-100}
wait $RPID

# Step 4: 분석
python3 scripts/analyze.py
cp data/dashboard.png web/static/   # Flask는 web/static/의 파일만 서빙 → 복사 필수

# Step 5: 웹 서버
echo '=== Flask 웹서버 시작 ==='
echo 'http://127.0.0.1:5000'
cd web2 && python3 app.py
