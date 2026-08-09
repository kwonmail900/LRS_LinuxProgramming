#!/bin/bash
# nested_if.sh — 중첩 if / 복합 조건 (5주차 slide 27)
a=5; b=10

# 중첩 if
if [ $a -gt 0 ]; then
    if [ $b -gt 0 ]; then
        echo "둘 다 양수"
    else
        echo "a만 양수"
    fi
else
    echo "a는 음수/0"
fi

# 복합 조건 방법 1: && / ||
if [ $a -gt 0 ] && [ $a -lt 100 ]; then
    echo "0~100 사이"
fi

# 방법 2: [[ ]] (bash)
if [[ $a -gt 0 && $a -lt 100 ]]; then
    echo "0~100 사이"
fi

# 방법 3: -a / -o (POSIX)
if [ $a -gt 0 -a $a -lt 100 ]; then
    echo "0~100 사이"
fi
