#!/bin/bash
# for_examples.sh — for 문 활용 예제 (5주차 slide 32)

# 파일 목록 반복
for file in ~/linux_lab/week5/*.sh; do
    echo "파일: $file ($(wc -l < $file) 줄)"
done

# 명령 결과 반복
for user in $(cut -d: -f1 /etc/passwd | head -5); do
    echo "사용자: $user"
done

# 디렉토리 내 파일 권한 변경
for script in ~/linux_lab/week5/*.sh; do
    chmod +x "$script"
    echo "실행 권한 부여: $script"
done
