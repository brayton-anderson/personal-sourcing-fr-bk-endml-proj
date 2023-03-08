import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate

migrate = Migrate()
db = SQLAlchemy()

mail = Mail()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USERNAME"] = os.environ.get("prince.bray98@gmail.com")
    app.config["MAIL_PASSWORD"] = os.environ.get("786@Reyreina")
    app.config["MAIL_USE_TLS"] = False
    app.config["MAIL_USE_SSL"] = True

    migrate.init_app(app, db)
    db.init_app(app)
    db.app = app
    mail = Mail(app)

    api = Api(app=app)

    from website.routes import create_authentication_routes, create_view_routes

    create_authentication_routes(api=api)
    create_view_routes(api=api)

    create_db(app)

    return app


def create_db(app):
    with app.test_request_context():
        if not os.path.exists("instance/personal.db"):
            db.create_all()
            from website.insertdata import Insertdata

            Insertdata.insert_language_data()
            Insertdata.insert_competency_data()
            Insertdata.insert_educationlevel_data()
            Insertdata.insert_workavailability_data()
            Insertdata.insert_roles_data()
            Insertdata.insert_skills_data()
            Insertdata.insert_programinglanguages_data()
            Insertdata.insert_frameworks_data()
