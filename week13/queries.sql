-- =====================================================================
-- 13주차 강의자료에서 추출한 SQL 문 모음
-- 출처: 13주차 1/2/3교시 (Flask 기초 · Flask+DB 대시보드 · Step5 통합)
-- 대상 DB: data/sensor.db  (SQLite3, 11주차 Step3에서 생성)
-- 테이블: sensor_data
-- =====================================================================

-- [테이블 스키마] (11주차 Step3에서 정의, Flask 코드가 참조)
CREATE TABLE IF NOT EXISTS sensor_data (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_type  TEXT,
    raw_value    INTEGER,
    lux          REAL,
    timestamp    DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- [1교시] Jinja2 테이블 예제 (최신 20건, 역순)
SELECT * FROM sensor_data ORDER BY id DESC LIMIT 20;

-- [2교시] 대시보드 통계 집계 (index 라우트) — COUNT/AVG/MAX/MIN 한 번에
SELECT COUNT(*)               AS cnt,
       ROUND(AVG(raw_value),1) AS avg,
       MAX(raw_value)          AS mx,
       MIN(raw_value)          AS mn
FROM sensor_data;

-- [2교시] 최근 10건 (대시보드 테이블)
SELECT * FROM sensor_data ORDER BY id DESC LIMIT 10;

-- [2교시] REST API /api/data — 전체 데이터 (역순)
SELECT * FROM sensor_data ORDER BY id DESC;

-- [2교시] REST API /api/recent/<int:n> — 최근 N건
--   ※ n 은 <int:n> 라우트로 정수 검증됨 (SQL Injection 안전)
SELECT * FROM sensor_data ORDER BY id DESC LIMIT :n;
