#!/usr/bin/env python3
# 13주차 1교시 - slide 6
# Flask Hello World (설치: pip3 install Flask)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)   # 개발 서버. 운영에서는 debug=False
# 실행: python3 helloflask.py  ->  http://127.0.0.1:5000
