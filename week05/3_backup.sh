#!/bin/bash
# backup.sh — 종합 실습: 자동 백업 스크립트 (5주차 slide 39)
if [ $# -eq 0 ]; then
    echo "사용법: $0 <백업할 디렉토리>"
    exit 1
fi

src="$1"
dest="${src}_backup_$(date +%Y%m%d)"

if [ -d "$src" ]; then
    cp -r "$src" "$dest"
    echo "백업 완료: $src → $dest"
else
    echo "오류: $src 디렉토리가 존재하지 않습니다."
    exit 1
fi
