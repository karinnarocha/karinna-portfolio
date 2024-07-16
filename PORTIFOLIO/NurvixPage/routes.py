from flask import Blueprint, render_template

nurvixPage = Blueprint('nurvixPage', __name__)


@nurvixPage.route("/NurVIX")
def nurvixpage():
    return render_template("NurVIX.html")
