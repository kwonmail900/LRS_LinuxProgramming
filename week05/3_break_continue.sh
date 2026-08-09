#!/bin/bash
# break_continue.sh — 흐름 제어 (5주차 slide 35)

# break: 루프 강제 종료 (i==5에서 중단)
for ((i=1; i<=10; i++)); do
    echo $i
    if [ $i -eq 5 ]; then
        break
    fi
done
# 출력: 1 2 3 4 5

# continue: 현재 반복 건너뛰기 (짝수 skip → 홀수만 출력)
for ((i=1; i<=5; i++)); do
    if ((i % 2 == 0)); then
        continue
    fi
    echo $i
done
# 출력: 1 3 5
