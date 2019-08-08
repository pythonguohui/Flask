import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SECRET_KEY在session_id和csrf_token生成的时候使用，session_id和csrf_token在生成的过程当前使用了加盐算法
    SECRET_KEY = "guohui123"

class DebugConfig(BaseConfig):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "Student.sqlite")
    # SQLALCHEMY_DATABASE_URI = "mysql//root:999@localhost/flask"
class OnlineConfig(BaseConfig):
    DEBUG=False
    QLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "Student.sqlite")