#!/usr/bin/env python3
# 13주차 1교시 - slide 9 (좌측 코드 박스)
# Jinja2 템플릿 예제: DB 조회 -> HTML 테이블
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect("../data/sensor.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sensor_data ORDER BY id DESC LIMIT 20")
    data = cursor.fetchall()
    conn.close()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
