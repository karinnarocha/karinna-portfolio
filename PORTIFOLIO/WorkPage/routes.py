from flask import Blueprint, render_template

workPage = Blueprint('workPage', __name__)


@workPage.route("/Work")
def workpage():
    return render_template("Work.html")
