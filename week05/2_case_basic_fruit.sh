#!/bin/bash
# case_basic_fruit.sh — case 문 기본 구조 (5주차 slide 22)
fruit="apple"
case $fruit in
    "apple")
        echo "사과입니다."
        ;;
    "banana")
        echo "바나나입니다."
        ;;
    *)
        echo "알 수 없는 과일."
        ;;
esac
