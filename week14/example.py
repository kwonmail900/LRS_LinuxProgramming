# scripts/db_create.py (Simplified)
import sqlite3
conn = sqlite3.connect('data/sensor.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS sensor_data (id INTEGER PRIMARY KEY, value REAL)''')
conn.commit()
conn.close()

# web/app.py (Simplified)
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return "Sensor Dashboard"
if __name__ == '__main__':
    app.run(debug=True)
