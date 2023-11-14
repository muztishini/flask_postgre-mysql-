from flask import Flask, render_template, redirect, request
from model_posgre import Users, db

app = Flask(__name__)

username = 'testuser'
password = '123456'
server = 'localhost'

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{username}:{password}@{server}/testf"

db.init_app(app)


@app.route('/')
def index():
    people = Users.query.order_by(Users.id).all()
    return render_template('index.html', people=people)


@app.route('/create/', methods=['POST'])
def create():
    if request.method == "POST":
        user = Users(name=request.form['name'])
        db.session.add(user)
        db.session.commit()
    return redirect('/')


@app.route('/edit/<id>', methods=['POST', 'GET'])
def edit(id):
    person = Users.query.get(id)
    if request.method == "POST":
        name = request.form['name']
        person.name = name
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "При редактировании произошла ошибка"
    else:
        return render_template("edit.html", person=person)


@app.route('/delete/<id>')
def delete(id):
    user = Users.query.get(id)
    db.session.delete(user)
    try:
        db.session.commit()
        return redirect('/')
    except:
        return "При удалении произошла ошибка"


if __name__ == '__main__':
    app.run(debug=True)
