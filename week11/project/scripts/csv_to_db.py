#!/usr/bin/env python3
# scripts/csv_to_db.py — 10주차 CSV 데이터를 DB로 저장
import sqlite3, csv, os

DB_PATH = "data/sensor.db"
CSV_PATH = "data/sensor_data.csv"

def import_csv():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        if not os.path.exists(CSV_PATH):
            print(f"[Error] {CSV_PATH} 파일을 찾을 수 없습니다.")
            return
        with open(CSV_PATH, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                cursor.execute(
                    "INSERT INTO sensor_data (sensor_type, raw_value, lux) VALUES (?, ?, ?)",
                    (row["type"], int(row["raw_value"]), float(row["lux"]))
                )
        count = cursor.execute("SELECT COUNT(*) FROM sensor_data").fetchone()[0]
        print(f"[DB] {count}건 임포트 완료")

if __name__ == "__main__":
    import_csv()
