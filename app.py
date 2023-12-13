from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure your database URI, track modifications, and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://helmerc:6h7#e61CfWEFl#@oege.ie.hva.nl/zhelmerc"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'sdjhdjhsnkdnkdsnkshuhuhnn'
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'connect_args': {'ssl': {'fake_flag_to_enable_tls': True}}}

# Initialize the SQLAlchemy instance
db = SQLAlchemy(app)


class QuestionDotshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_1 = db.Column(db.String(100), nullable=False)
    question_2 = db.Column(db.String(100), nullable=False)
    question_3 = db.Column(db.String(100), nullable=False)
    question_4 = db.Column(db.String(100), nullable=False)
    question_5 = db.Column(db.String(100), nullable=False)
    question_6 = db.Column(db.String(100), nullable=False)
    question_7 = db.Column(db.String(100), nullable=False)
    question_8 = db.Column(db.String(100), nullable=False)
    question_9 = db.Column(db.String(100), nullable=False)
    question_10 = db.Column(db.String(100), nullable=False)
    question_11 = db.Column(db.String(100), nullable=False)
    question_12 = db.Column(db.String(100), nullable=False)
    question_13 = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'Response {self.name}'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit_question", methods=["POST"])
def submit_question():
    # Retrieve form data
    form_data = {f"question_{i}": request.form[f"question_{i}"] for i in range(1, 14)}

    # Create a QuestionDotshop instance
    question_dotshop = QuestionDotshop(**form_data)

    # Add and commit to the database
    db.session.add(question_dotshop)
    db.session.commit()

    # Flash a message to the user
    flash('Bedankt voor uw medewerking')

    # Redirect to the question_dotshop route
    return redirect(url_for('question_dotshop'))


@app.route("/question_dotshop")
def question_dotshop():
    return render_template("question.html")


if __name__ == "__main__":
    # Run the app
    app.run(debug=True, host='0.0.0.0')
