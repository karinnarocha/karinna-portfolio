from flask import Flask
from flask_mail import Mail
from PORTIFOLIO.config import Config

mail = Mail()

def create_app():

    app = Flask(__name__, static_folder='static', template_folder='templates')

    app.config.from_object(Config)
    mail.init_app(app)
    
    from .IndexPage.routes import indexPage
    from .WorkPage.routes import workPage
    from .AboutPage.routes import aboutPage
    from .ContactPage.routes import contactPage


    app.register_blueprint(indexPage)
    app.register_blueprint(workPage)
    app.register_blueprint(aboutPage)
    app.register_blueprint(contactPage)

    return app
