# web/app.py — 센서 대시보드 (13주차 2교시 slide 2 + slide 3)
from flask import Flask, render_template, jsonify
import sqlite3, json, os

app = Flask(__name__)
DB = os.path.join(os.path.dirname(__file__), "..", "data", "sensor.db")

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row  # dict-like 접근
    return conn

@app.route("/")
def index():
    conn = get_db()
    stats = conn.execute("SELECT COUNT(*) as cnt, ROUND(AVG(raw_value),1) as avg,"
        " MAX(raw_value) as mx, MIN(raw_value) as mn FROM sensor_data").fetchone()
    recent = conn.execute("SELECT * FROM sensor_data ORDER BY id DESC LIMIT 10").fetchall()
    conn.close()
    # 12주차 리포트 JSON 로드
    report_path = os.path.join(os.path.dirname(__file__), "..", "data", "report.json")
    report = json.load(open(report_path)) if os.path.exists(report_path) else {}
    return render_template("index.html", stats=stats, recent=recent, report=report)

# JSON API — 전체 데이터
@app.route("/api/data")
def api_data():
    conn = get_db()
    rows = conn.execute("SELECT * FROM sensor_data ORDER BY id DESC").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

# JSON API — 통계
@app.route("/api/stats")
def api_stats():
    report_path = os.path.join(os.path.dirname(__file__), "..", "data", "report.json")
    if os.path.exists(report_path):
        return jsonify(json.load(open(report_path)))
    return jsonify({"error": "리포트 없음"}), 404

# JSON API — 최근 N건
@app.route("/api/recent/<int:n>")
def api_recent(n):
    conn = get_db()
    rows = conn.execute(f"SELECT * FROM sensor_data ORDER BY id DESC LIMIT {n}").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

if __name__ == "__main__":
    app.run(debug=True)   # 실행용 (원문 슬라이드에는 없음). http://127.0.0.1:5000
