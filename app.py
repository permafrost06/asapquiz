from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = b'_5#y2LoekcrQ8z\n\xec]/'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
db = SQLAlchemy(app)

class Exam(db.Model):
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
    grade = db.Column(db.String(5), unique=False, nullable=False)

    def ___repr__(self):
        return '<question %r>' % self.question

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/questions", methods=["POST"])
def questions():
    if request.method == "POST":
        session["name"] = request.form.get('student_name')
        session["school"] = request.form.get('school')
        session["class"] = request.form.get('cls')
        session["teacher"] = request.form.get('teacher')
        if session["class"] == 'std2' or session["class"] == 'std3':
            questions_list = Question.query.filter_by(grade='2')
        else:
            questions_list = Question.query.filter_by(grade='4')
        return render_template("questions.html", questions=questions_list)

@app.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        answers = []
        if session["class"] == 'std2' or session["class"] == 'std3':
            questions_list = Question.query.filter_by(grade='2')
        else:
            questions_list = Question.query.filter_by(grade='4')
        for i in range(1,questions_list.count()+1):
            answers.append(str(request.form.get("q{}".format(i))))
        db.session.add(Exam(name=session["name"], school=session["school"], classno=session["class"], teacher=session["teacher"], answers=",".join(answers)))
        db.session.commit()
        return render_template("success.html")