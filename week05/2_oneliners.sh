#!/bin/bash
# oneliners.sh — 한 줄 표현과 종료 코드 활용 (5주차 slide 26)

# if 한 줄 표현
[ -f file.txt ] && echo "파일 존재" || echo "파일 없음"

# 명령 성공 시 실행
mkdir /tmp/test && echo "디렉토리 생성 성공"

# 명령 실패 시 실행
rm nonexist.txt 2>/dev/null || echo "삭제할 파일 없음"

# 종료 코드 활용
grep -q "error" log.txt
if [ $? -eq 0 ]; then
    echo "에러가 발견되었습니다!"
fi

# test 명령 ([ ] 와 동일)
test -f /etc/passwd && echo "passwd 존재"
