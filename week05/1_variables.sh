#!/bin/bash
# variables.sh — 변수 선언/참조·산술·입력 (5주차 slide 7,11)

# 변수 선언 (= 양쪽에 공백 없음!)
greeting="Hello"
name="Linux"
count=10

# 변수 참조와 산술
echo "$greeting $name"
result=$((count * 2))
echo "결과: $result"

# 환경 변수 / 읽기 전용
export MY_VAR="hello"
echo "$MY_VAR"
readonly PI=3.14
echo "PI=$PI"
# PI=3.0   # readonly 변수는 재할당 시 error

# 사용자 입력
read -p "숫자 입력: " num
echo "$num x 2 = $((num * 2))"
