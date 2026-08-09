#!/bin/bash
# case_wildcard.sh — case 와일드카드 패턴 매칭 (5주차 slide 24)
read -p "파일명: " filename

case "$filename" in
    *.txt)
        echo "텍스트 파일입니다."
        cat "$filename"
        ;;
    *.sh)
        echo "쉘 스크립트입니다."
        chmod +x "$filename"
        ;;
    *.tar.gz | *.tgz)
        echo "압축 파일입니다."
        tar -tzvf "$filename"
        ;;
    *)
        echo "알 수 없는 형식: $filename"
        ;;
esac
