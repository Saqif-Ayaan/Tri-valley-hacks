from flask import render_template, Blueprint, request

start = Blueprint('start', __name__)
detector = Blueprint('detector', __name__)
info = Blueprint('info', __name__)

@start.route('/')
def home():
    return render_template("home.html")

@detector.route('/detector')
def detect():
    return render_template("detector.html")

@info.route('/info')
def inf():
    return render_template("info.html")