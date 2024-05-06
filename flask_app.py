from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)


def get_canteens():
    conn = sqlite3.connect('DINERS.db')
    c = conn.cursor()
    c.execute("SELECT * FROM CANTEEN")
    canteens = c.fetchall()
    conn.close()
    return canteens


@app.route('/')
def index():
    canteens = get_canteens()
    return render_template('index.html', canteens=canteens)


@app.route('/api/canteens', methods=['GET'])
def api_get_canteens():
    canteens = get_canteens()
    return jsonify(canteens)

if __name__ == '__main__':
    app.run(debug=True)
