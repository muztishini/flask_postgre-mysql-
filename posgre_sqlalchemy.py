from flask import Flask, render_template
from model_posgre import Users, db

app = Flask(__name__)

username = 'testuser'
password = '123456'
server = 'localhost'

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{username}:{password}@{server}/testf"

db.init_app(app)

@app.route('/')
def index():   
    users = Users.query.all()
    return render_template('user_sql.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)