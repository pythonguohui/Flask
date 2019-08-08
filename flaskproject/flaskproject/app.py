from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route("/index/")
def helloword():
    student=[
        {'name':"张三","age":18,"score":80},
        {'name': "李四", "age": 28, "score": 83},
        {'name': "贾五", "age": 16, "score": 85},
        {'name': "陈六", "age": 19, "score": 89},
        {'name': "赵七", "age": 21, "score": 81},
    ]
    return render_template("student_list.html",student=student)

@app.route("/base/")
def base():
    return render_template("blank.html")

if __name__=='__main__':
    app.run()