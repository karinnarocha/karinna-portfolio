from flask import render_template, Blueprint

indexPage = Blueprint('indexPage', __name__)


@indexPage.route("/")
def home():
    return render_template("index.html")
