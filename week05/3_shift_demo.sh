#!/bin/bash
# shift_demo.sh — while + shift로 인자 순차 처리 (5주차 slide 38)
count=1
while [ $# -gt 0 ]; do
    echo "인자 $count: $1"
    shift                 # $1 제거, $2→$1로 이동
    count=$((count + 1))
done
# 실행: ./shift_demo.sh arg1 arg2 arg3
