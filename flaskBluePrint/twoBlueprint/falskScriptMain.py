from flask import Flask
from flask_script import Manager

app=Flask(__name__)

@app.route("/")
def index():
    return "hello"

manager=Manager(app)

if __name__=="__main__":
    manager.run()