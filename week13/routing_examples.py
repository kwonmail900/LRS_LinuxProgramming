#!/usr/bin/env python3
# 13주차 1교시 - slide 7
# Flask 라우팅: 기본 / URL 파라미터 / JSON API / HTTP 메서드
from flask import Flask, jsonify, request   # request: 슬라이드 코드에서 사용되어 추가

app = Flask(__name__)

# 기본 페이지
@app.route("/")
def index():
    return "<h1>센서 대시보드</h1>"

# URL 파라미터 (<int:...> 정수 변환기)
@app.route("/sensor/<int:sensor_id>")
def sensor(sensor_id):
    return f"센서 ID: {sensor_id}"

# JSON 응답 (REST API)
@app.route("/api/data")
def api_data():
    return jsonify({"status": "ok", "count": 50})

# 여러 HTTP 메서드
@app.route("/api/sensor", methods=["GET", "POST"])
def api_sensor():
    if request.method == "POST":
        return jsonify({"msg": "데이터 수신"})
    return jsonify({"msg": "데이터 조회"})

if __name__ == "__main__":
    app.run(debug=True)
