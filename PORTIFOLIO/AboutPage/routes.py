from flask import Blueprint, render_template

aboutPage = Blueprint('aboutPage', __name__)


@aboutPage.route("/About")
def aboutpage():
    return render_template("About.html")
