from flaskproject.main import models

db=models.session()

class Base(models.Model):
    __abstract__=True
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)

    def save(self):
        db.add(self)
        db.commit()
    def delete_object(self):
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

# models.drop_all()
# models.create_all()

# course=Course()
# course.name="python"
# course.description="python"
# course.save()
#
# course1=Course()
# course1.name="liunx"
# course1.description="liunx"
# course1.save()
#
# s=Students()
# s.name="小白"
# s.age=18
# s.gender=1
# s.save()
#
# s1=Students()
# s1.name="小黑"
# s1.age=21
# s1.gender=1
# s1.save()
#
# s.to_course=[course]
# s.save()
# s1.to_course=[course1]
# s1.save()
#
# student=Students.query.get(1)
# print(student.to_course.all())
#
# course=Course.query.get(1)
# print(course.to_student.all())


# t=Teacher(name="小红",age=26,gender=1,course_id=1)
# t1=Teacher()
# t1.name="小黑"
# t1.age=33
# t1.gender=2
# t1.course_id=1
# t2={"name":"小白","age":29,"gender":2,"course_id":1}
# t2=Teacher(**t2)
# session.add_all([t,t1,t2])
# session.commit()

# t=Teacher.query.get(1)
# print(t)
# t.name="哈哈"
# session.add(t)
# session.commit()

# t=Teacher.query.get(1)
# session.delete(t)
# # session.commit()

# t=Teacher.query.get(2)
# t.name="哈哈"
# t.save()

# t=Teacher.query.get(2).delete_object()


# t= Teacher.query.filter_by(age=123).all()
# print(t)

# t=Teacher.query.order_by("age").all()
# print(t)
# t= Teacher.query.order_by(models.desc("age")).all()
# print(t)
# t= Teacher.query.order_by(Teacher.age.desc()).all()
# print(t)
# t= Teacher.query.offset(1).limit(2).all()
# print(t)

# t=Teacher.query.get(1)
# print(t.to_course_data)
# t=Course.query.get(1)
# print(t.to_teacher)