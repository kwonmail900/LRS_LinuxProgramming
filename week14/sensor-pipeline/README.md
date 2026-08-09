# Sensor Data Pipeline

리눅스 프로그래밍 프로젝트 — 센서→IPC→DB→AI→Flask 파이프라인

## 구조
- Step 1: C 센서 시뮬레이터 (rand → CDS ADC 0~4095)
- Step 2: FIFO IPC로 데이터 수집
- Step 3: SQLite3 DB 저장
- Step 4: pandas/matplotlib AI 분석 (이상치, 이동평균)
- Step 5: Flask 웹 대시보드
- Step 6: Git 관리 + 자동화

## 빠른 시작
```bash
git clone https://github.com/student/sensor-pipeline.git
cd sensor-pipeline
make install-deps
make run N=100      # 파이프라인 실행 (100회)
make web N=100      # Flask 웹서버 포함 실행
```

## 기술 스택
C, GCC/Make, FIFO, SQLite3, Python, pandas, matplotlib, Flask
