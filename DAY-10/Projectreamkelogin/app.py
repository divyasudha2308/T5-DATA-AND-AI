import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# FIXED spelling: templates
base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=os.path.join(base_dir, "templates"))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# User Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(120))


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Add user
@app.route("/adduser", methods=["POST"])
def adduser():
    username = request.form.get("username")
    password = request.form.get("password")

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for("users"))


# Show users
@app.route("/users")
def users():
    users = User.query.all()
    return render_template("users.html", users=users)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # create table with password column
    app.run(debug=True)
