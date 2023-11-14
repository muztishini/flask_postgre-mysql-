from flask import Flask, render_template
from model_mysql import Users, db

app = Flask(__name__)

username = 'root'
password = '12345'
server = 'localhost'
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{username}:{password}@{server}/test"
# app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{username}:{password}@{server}/testf"

db.init_app(app)

@app.route('/')
def index():   
    users = Users.query.all()
    return render_template('user_sql.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)