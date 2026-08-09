#!/bin/bash
# until_demo.sh — until 문: 조건이 거짓인 동안 반복 (5주차 slide 34)
# while 과 반대: 조건이 '참'이 되면 종료
counter=1
until [ $counter -gt 5 ]; do
    echo "카운터: $counter"
    counter=$((counter + 1))
done
# 동일하게 1~5 출력

# 참고 (while vs until)
#   while : 조건이 참(True)인 동안 반복 → 거짓이 되면 종료
#   until : 조건이 거짓(False)인 동안 반복 → 참이 되면 종료
