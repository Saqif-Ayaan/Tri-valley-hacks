from flask import render_template, Blueprint, request

start = Blueprint('start', __name__)

@start.route('/')
def home():
    return render_template("HomePage.html")