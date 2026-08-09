#!/bin/bash
set -euo pipefail

# 빌드
cd $(dirname $0)/..
make

# 실행 (인자: 측정 횟수, 기본 20)
count=${1:-20}
echo "=== 센서 시뮬레이터 시작 (${count}회) ==="
./sensor_sim $count
echo "=== 완료 ==="
echo "데이터: data/sensor_data.csv"
echo "라인 수: $(wc -l < data/sensor_data.csv)"

# 간단한 통계
awk -F, 'NR>1{sum+=$3;cnt++} END{printf "평균 RAW: %.1f\n", sum/cnt}' data/sensor_data.csv