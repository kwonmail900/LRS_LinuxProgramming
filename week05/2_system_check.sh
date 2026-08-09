#!/bin/bash
# system_check.sh — 조건문 종합 실습: 디스크 사용률 (5주차 slide 25)
usage=$(df -h / | awk 'NR==2{print $5}' | tr -d '%')

if [ $usage -ge 90 ]; then
    echo "⚠️ 경고: 디스크 사용률 ${usage}% (위험)"
elif [ $usage -ge 70 ]; then
    echo "주의: 디스크 사용률 ${usage}% (높음)"
else
    echo "정상: 디스크 사용률 ${usage}%"
fi
