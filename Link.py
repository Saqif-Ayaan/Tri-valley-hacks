from flask import render_template, Blueprint, request
import os
from PIL import Image
import roboflow

start = Blueprint('start', __name__)
detector = Blueprint('detector', __name__)
info = Blueprint('info', __name__)

@start.route('/')
def home():
    return render_template("home.html")

@detector.route('/detector', methods = ["POST", "GET"])
def detect():
    if request.method == "POST":
        file = request.files['Insert_photo']
        file.save(os.path.join(file.filename))

        rf = roboflow.Roboflow(api_key = "7gfJQ83G4t1jbyfIhIPM")
        project = rf.project("garbageclassification-bhacz")
        model = project.version("1").model

        prediction = model.predict(file.filename)
        pval = prediction.predictions
        print(pval)

        return render_template("detector.html", pred = pval)
    return render_template("detector.html")

@info.route('/info')
def inf():
    return render_template("info.html")
