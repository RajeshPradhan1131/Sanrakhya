from app import app
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/hospitals')
def hospitals():
    all_hospitals = Hospital.query.all()
    return render_template('hospitals.html', hospitals=all_hospitals)