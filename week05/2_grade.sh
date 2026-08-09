#!/bin/bash
# grade.sh — if-elif-else 학점 판별 (5주차 slide 18)
read -p "점수를 입력하세요: " score

if [ $score -ge 90 ]; then
    echo "A 학점입니다."
elif [ $score -ge 80 ]; then
    echo "B 학점입니다."
elif [ $score -ge 70 ]; then
    echo "C 학점입니다."
elif [ $score -ge 60 ]; then
    echo "D 학점입니다."
else
    echo "F 학점입니다."
fi
