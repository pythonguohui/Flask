import wtforms
from wtforms import validators
from flask_wtf import Form
from flaskproject.models import Course

course_list=[(i.id,i.name) for i in Course.query.all()]

class  TeacherFrom(Form):
    name=wtforms.StringField("教师姓名",
                             render_kw={
                                 "class":"form-control",
                                 "placeholder":"教师姓名"
                             },
                             validators=[validators.DataRequired("姓名不能为空")]
    )
    age=wtforms.IntegerField("教师年龄",
                             render_kw={
                                 "class":"form-control",
                                 "placeholder":"教师年龄"
                             },
                             validators=[validators.DataRequired("年龄不能为空")]
    )
    gender=wtforms.SelectField("教师性别",
                               choices=[("1","男"),("2","女"),],
                               render_kw={
                                   "class":"form-control",
                               },
    )
    course=wtforms.SelectField(
        "学科",
        choices=course_list,
        render_kw={
            "class":"form-control"
        }
    )