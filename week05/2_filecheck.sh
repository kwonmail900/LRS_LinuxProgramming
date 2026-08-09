#!/bin/bash
# filecheck.sh — 파일/디렉토리 테스트 조건문 (5주차 slide 20)
read -p "파일 경로를 입력하세요: " filepath

if [ -f "$filepath" ]; then
    echo "$filepath 는 일반 파일입니다."
    echo "크기: $(stat -c %s $filepath) bytes"
elif [ -d "$filepath" ]; then
    echo "$filepath 는 디렉토리입니다."
    echo "내용: $(ls $filepath | wc -l) 개 항목"
elif [ -L "$filepath" ]; then
    echo "$filepath 는 심볼릭 링크입니다."
else
    echo "$filepath 가 존재하지 않습니다."
fi
