#!/bin/bash
# for_demo.sh — for 문 3가지 형태 (5주차 slide 31)

# 1) 목록 반복
for fruit in apple banana orange; do
    echo "과일: $fruit"
done

# 2) 숫자 범위 {시작..끝}
for num in {1..5}; do
    echo "숫자: $num"
done

# 3) C 스타일 for 문
for ((i=1; i<=10; i++)); do
    echo "$i"
done
