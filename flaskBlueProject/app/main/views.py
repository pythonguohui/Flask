import hashlib

from flask import request
from flask import jsonify
from flask import redirect
from flask import session
from flask import render_template
from flask import make_response

from . import  main
from app import csrf
from app.models import *
from . forms import TeacherFrom
# from app import cache

@main.route("/student_list/")
def student_list():
    student=Students.query.all()
    return render_template("student_list.html",**locals())

def loginVerify(fun):
    def inner(*args,**kwargs):
        username=request.cookies.get("username")
        user_id=request.cookies.get("user_id")
        session_username=session.get("username")
        if username and user_id and session_username:
            if username==session_username:
                return fun(*args,**kwargs)
        return redirect("/login/")
    return inner

@main.route("/index/",methods=["GET","POST"])
@loginVerify
def index():
    teacher_id=request.cookies.get("identity_id")
    if teacher_id:
        teachers=Teacher.query.get(int(teacher_id))
    else:
        teachers={}
    if request.method=="POST":
        username=request.form.get("username")
        age = request.form.get("age")
        gender = request.form.get("gender")
        course = request.form.get("course")

        if request.cookies.get("identity")=="0":
            student=Students()
            student.name=username
            student.age=age
            student.gender=gender
            student.save()

        else:
            teachers=Teacher()
            teachers.name=username
            teachers.age=age
            teachers.gender=gender
            teachers.course_id=int(course)
            teachers.save()

            user=User.query.get(int(request.cookies.get("user_id")))
            user.identity_id=teachers.id
            user.save()

            response=make_response(render_template("index.html",**locals()))
            response.set_cookie("identity_id",str(teacher_id))
            return response
    return render_template("index.html",**locals())

def set_password(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()


@main.route("/register/",methods=["GET","POST"])
def register():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        identity=request.form.get("identity")
        if username and password and identity:
            user=User()
            user.username=username
            user.password=set_password(password)
            user.identity=int(identity)
            user.save()
            return redirect("/login/")
    return render_template("register.html")


@main.route("/login/",methods=["GET","POST"])
# @cache.cached(timeout=30)
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username and password :
            user=User.query.filter_by(username=username).first()
            identity=user.identity
            identity_id=user.identity_id

            if user:
                web_password=set_password(password)
                db_password=user.password
                if web_password==db_password:
                    response=redirect("/index/")
                    response.set_cookie("username",username)
                    response.set_cookie("user_id",str(user.id))

                    response.set_cookie("identity",str(identity))

                    if identity_id:
                        response.set_cookie("identity_id",str(identity_id))
                    else:
                        response.set_cookie("identity_id","")
                    session["username"]=username
                    return response
    return render_template("login.html",**locals())

@main.route("/logout/")
def LogOut():
    response=redirect("/login/")
    cookie_list=request.cookies
    for key in cookie_list:
        response.delete_cookie(key)
    del session["username"]
    return response

# @csrf.exempt
@main.route("/add_teacher/",methods=["POST","GET"])
def add_teacher():
    teacher_from = TeacherFrom()
    if request.method=="POST":
        name=request.form.get("name")
        age=request.form.get("age")
        gender = request.form.get("gender")
        course=request.form.get("course")

        teacher=Teacher()
        teacher.name=name
        teacher.age=age
        teacher.gender=gender
        teacher.course_id=int(course)
        teacher.save()
    return render_template("add_teacher.html",**locals())

# @csrf.error_handler
@main.route("/csrf_403/")
def csrf_403(reason):
    return render_template("csrf_403.html")

@main.route("/userverify/",methods=["GET","POST"])
def UserVerify():
    result={"code":"","data":""}
    if request.method=="POST":
        data=request.form.get("username")
        if data:
            user=User.query.filter_by(username=data).first()
            if user:
                result["code"]= "400"
                result["data"]="用户名已存在"
            else:
                result["code"] = "200"
                result["data"] = "用户名未被注册，可以使用"
    else:
        result["code"] = "100"
        result["data"] = "请求类型错误"
    return jsonify(result)
