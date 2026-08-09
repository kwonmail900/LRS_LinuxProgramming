#!/bin/bash
# read_example.sh — read 명령어 (5주차 slide 10)
read -p "이름을 입력하세요: " name
read -p "나이를 입력하세요: " age
echo "안녕하세요, ${name}님! ${age}살이시군요."

# read 옵션 참고:
#   -p "프롬프트"   프롬프트 메시지 표시
#   -s             입력 숨기기 (비밀번호)   ex) read -s -p "암호: " pw
#   -n N           N글자만 입력            ex) read -n 1 key
#   -t N           N초 후 타임아웃          ex) read -t 5 answer
