#!/bin/bash
# args.sh — 명령행 인자 (5주차 slide 37)
echo "스크립트: $0"
echo "첫 번째 인자: $1"
echo "인자 개수: $#"
echo "모든 인자: $*"

# for 루프로 인자 처리 ("$@" 권장)
for arg in "$@"; do
    echo "인자: $arg"
done
# 실행: ./args.sh hello world 123
