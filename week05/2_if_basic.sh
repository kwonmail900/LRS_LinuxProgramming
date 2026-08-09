#!/bin/bash
# if_basic.sh — if 문 기본 구조 (5주차 slide 17)
# 주의: [ ] 안쪽에 반드시 공백!  [ $a -eq $b ] O   [$a -eq $b] X
age=20
if [ $age -ge 18 ]; then
    echo "성인입니다."
else
    echo "미성년자입니다."
fi
