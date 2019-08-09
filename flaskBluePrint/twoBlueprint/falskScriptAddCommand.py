from flask import Flask
from flask_script import Manager

app=Flask(__name__)

@app.route("/")
def index():
    return "hello"

manager=Manager(app)

@manager.command
def hello(name="createsuperuser"):
    username=input("please enter your username: ")
    email = input("please enter your email: ")
    password = input("please enter your password: ")
    print("恭喜你执行命令成功%s"%name)
    return "哈哈哈，小傻瓜"

@manager.command
def run(ip="127.0.0.1",port=8000):
    print("runserver in %s:%s"%(ip,port))

if __name__=="__main__":
    manager.run()