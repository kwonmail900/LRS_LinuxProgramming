#!/bin/bash
# while_demo.sh — while 문 (5주차 slide 33)

# 카운터
counter=1
while [ $counter -le 5 ]; do
    echo "카운터: $counter"
    counter=$((counter + 1))
done
# 출력: 1, 2, 3, 4, 5

# 파일 줄 단위 읽기
while IFS= read -r line; do
    echo "줄: $line"
done < /etc/passwd | head -5

# 또는 파이프 사용
# cat /etc/passwd | while read line; do echo $line; done
