from flask import Flask, render_template, request, redirect, url_for, session
from getitem import getitem
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "w^dr8@O4IiR7"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class DataBass(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    runtime = db.Column(db.Integer)
    keyword = db.Column(db.String())
    
    def __init__(self, runtime, keyword):
        self.runtime = runtime
        self.keyword = keyword

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
    app.run(debug=True)
