from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exams.db'
db = SQLAlchemy(app)

class Exams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    school = db.Column(db.String(120), unique=False, nullable=False)
    classno = db.Column(db.String(120), unique=False, nullable=False)
    teacher = db.Column(db.String(120), unique=False, nullable=False)
    answers = db.Column(db.String(300), unique=False, nullable=False)

    def __repr__(self):
        return '<exam of %r>' % self.name

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), unique=True, nullable=False)
    opt_a = db.Column(db.String(100), unique=False, nullable=False)
    opt_b = db.Column(db.String(100), unique=False, nullable=False)
    opt_c = db.Column(db.String(100), unique=False, nullable=False)
    opt_d = db.Column(db.String(100), unique=False, nullable=False)

    def ___repr__(self):
        return '<question %r>' % self.question

db.create_all()

with open('questions.csv', 'r', encoding='utf-8') as qfile:
    for line in qfile:
        segments = line.split(',,,')
        db.session.add(Question(text=segments[0], opt_a=segments[1], opt_b=segments[2], opt_c=segments[3], opt_d=segments[4]))
    db.session.commit()

Question.query.filter_by(grade='2')