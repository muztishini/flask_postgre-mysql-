from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'test'



@app.route('/')
def index():   
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
    