from flask import Flask, render_template, request, redirect, url_for, session
from getitem import getitem
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "w^dr8@O4IiR7"
app.config['SQLALCHEMY_DATABASE_URL'] = "postgres://etrdaefwshxfkb:16d8d6f38f1b3021b4c5b833cb2e2d4407d2ec91acb560174386c9782867c6d4@ec2-52-86-73-86.compute-1.amazonaws.com:5432/dada9tvecoeq0h"

db = SQLAlchemy(app)

class DataBass(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    runtime = db.Column(db.Integer)
    keyword = db.Column(db.String())
    
    def __init__(self, runtime, keyword):
        self.runtime = runtime
        self.keyword = keyword

def getApp():
    return app

@app.route("/", methods=["GET", "POST"])
@app.route("/start", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        session["keyword"] = request.form["keyword"]
        return redirect(url_for("output"))
    else:
        return render_template("main.html")

@app.route("/output")
def output():
    if "keyword" in session:
        img = getitem(session["keyword"])[0]
        runtime = getitem(session["keyword"])[1]
        data = DataBass(runtime, session["keyword"].lower())
        db.session.add(data)
        db.session.commit()
        session.pop("keyword")
        return render_template("output.html", img=img, runtime=runtime)
    else:
        return 'no keyword, go to <a href="/start">start</a>'

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
