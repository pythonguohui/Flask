from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect


import pymysql
pymysql.install_as_MySQLdb()

csrf=CSRFProtect()
models=SQLAlchemy()


def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object("settings.DebugConfig")

    csrf.init_app(app)
    models.init_app(app)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app