from app import models

class Base(models.Model):
    __abstract__=True
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    def save(self):
        db=models.session()
        db.add(self)
        db.commit()
    def delete_object(self):
        db = models.session()
        db.delete(self)
        db.commit()

class User(Base):
    username=models.Column(models.String(32))
    password=models.Column(models.String(32))
    identity=models.Column(models.Integer)
    identity_id=models.Column(models.Integer,nullable=True)

class Students(Base):
    __tablename__="students"

    name=models.Column(models.String(32))
    age=models.Column(models.Integer)
    gender=models.Column(models.Integer,default=1)#1 男，2 女 ，3 未知

Stu_Cou=models.Table(
    "stu_cou",
    models.Column("id",models.Integer,primary_key=True,autoincrement=True),
    models.Column("course_id",models.Integer,models.ForeignKey("course.id")),
    models.Column("student_id",models.Integer,models.ForeignKey("students.id"))
)

class Course(Base):
    __tablebname__ = "course"
    name = models.Column(models.String(32), unique=True)
    description=models.Column(models.Text)
    to_teacher=models.relationship(
        "Teacher",
        backref="to_course_data"
    )

    to_student=models.relationship(
        "Students",
        secondary=Stu_Cou,
        backref=models.backref("to_course",lazy="dynamic"),
        lazy="dynamic"
    )

class Score(Base):
    __tablebname__="score"

    name = models.Column(models.String(32), unique=True)
    course_id=models.Column(models.Integer,models.ForeignKey("course.id"))
    students_id = models.Column(models.Integer, models.ForeignKey("students.id"))

class Clock(Base):
    __tablebname__ = "clock"

    att_time=models.Column(models.Date)
    status=models.Column(models.Integer,default=1) #1 正常出勤 2，迟到 3，早退 4 ，请假 5，旷课
    student_id=models.Column(models.Integer,models.ForeignKey("students.id"))

class Teacher(Base):
    __tablebname__ = "teacher"

    name = models.Column(models.String(32))
    age = models.Column(models.Integer)
    gender = models.Column(models.Integer, default=1)  # 1 男，2 女 ，3 未知
    course_id=models.Column(models.Integer,models.ForeignKey("course.id"))
