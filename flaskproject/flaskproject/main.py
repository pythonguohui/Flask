import os

import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import session
from flask_wtf.csrf import CSRFProtect
from flask_restful import Api,Resource

pymysql.install_as_MySQLdb()

app=Flask(__name__)
# BASE_DIR =os.path.abspath(os.path.dirname(__file__))
#
# app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(BASE_DIR,"Student.sqlite")
# app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"]=True
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True

# app.config.from_pyfile("settings.py")

api=Api(app)

class Hello(Resource):
    def get(self):
        return {"hello":"world"}

api.add_resource(Hello,"/API/")

csrf=CSRFProtect(app)

app.config.from_object("config.DebugConfig")

models=SQLAlchemy(app)

