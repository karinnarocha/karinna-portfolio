from flask import Blueprint, render_template

AIBeansPage = Blueprint('AIBensPage', __name__)

@AIBeansPage.route("/AIBeans")
def aibeanspage():
 return render_template("AIBEans.html")