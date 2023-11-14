from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='test2',
                            user = 'testuser',
                            password='123456')
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM cities;')
    cities = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', cities=cities)

if __name__ == '__main__':
    app.run(debug=True)