from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
DB_NAME = "portfolio.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "&@$&VN&yehuh8tw49y&T^*Rc6gtf87^&E%ER%habsufa"


    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, DB_NAME)


    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix="/")

    from .modules import Project
    create_database(app)

    return app


def create_database(app):
    if not os.path.exists("website/" + DB_NAME):
        with app.app_context():
            db.create_all()
            


    