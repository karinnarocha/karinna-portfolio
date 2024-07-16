from flask import Flask
from flask_mail import Mail
from PORTIFOLIO.config import Config

mail = Mail()

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)
    mail.init_app(app)
    
    from .IndexPage.routes import indexPage
    from .WorkPage.routes import workPage
    from .AboutPage.routes import aboutPage
    from .ContactPage.routes import contactPage
    from .NurvixPage.routes import nurvixPage
    from .AIBeansPage.routes import AIBeansPage

    app.register_blueprint(indexPage)
    app.register_blueprint(workPage)
    app.register_blueprint(aboutPage)
    app.register_blueprint(contactPage)
    app.register_blueprint(nurvixPage)
    app.register_blueprint(AIBeansPage)

    return app
