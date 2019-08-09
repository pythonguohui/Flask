from flask import Blueprint

simple_blueprint1=Blueprint("page1",__name__)

@simple_blueprint1.route("/index1/")
def index():
    return "hello world1"