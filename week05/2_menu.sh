#!/bin/bash
# menu.sh — case 문 실전 예제 (5주차 slide 23)
echo "=== 메뉴 ==="
echo "1) 파일 목록"
echo "2) 디스크 사용량"
echo "3) 현재 시간"
read -p "선택: " choice

case $choice in
    1) ls -la ;;
    2) df -h ;;
    3) date ;;
    *) echo "잘못된 선택" ;;
esac
