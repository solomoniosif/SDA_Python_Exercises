from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from person import Person
import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Register.sqlite3'

db = SQLAlchemy(app)


class PersonDb(db.Model):
    __tablename__ = 'person'

    _id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.Date(), nullable=False)

    def __init__(self, person):
        self.first_name = person.first_name
        self.last_name = person.last_name
        self.birthdate = person.birthdate


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form
        first_name = data['first_name']
        last_name = data['last_name']
        birthdate = datetime.datetime.strptime(data['birthdate'], '%Y-%m-%d').date()
        new_person = Person(first_name, last_name, birthdate)
        new_data = PersonDb(new_person)
        db.session.add(new_data)
        db.session.commit()

        register = PersonDb.query.all()

        return render_template("index.html", register=register)
    return render_template("index.html")


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        data = request.form
        first_name = data['first_name']
        last_name = data['last_name']
        if first_name and last_name:
            query = PersonDb.query.filter_by(first_name=first_name, last_name=last_name)
        elif first_name and not last_name:
            query = PersonDb.query.filter_by(first_name=first_name)
        elif not first_name and last_name:
            query = PersonDb.query.filter_by(last_name=last_name)
        else:
            query = PersonDb.query.all()
        return render_template("search.html", query=query)
    return render_template("search.html")


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
