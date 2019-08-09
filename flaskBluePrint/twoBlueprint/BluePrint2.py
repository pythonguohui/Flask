from flask import Blueprint

simple_blueprint2=Blueprint("page2",__name__)

@simple_blueprint2.route("/index2/")
def index():
    return "hello world2"