from app import create_app,models
from flask_script import Manager
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from gevent import monkey


monkey.patch_all()

app=create_app("running")

manager=Manager(app)

migrate=Migrate(app,models)

manager.add_command("db",MigrateCommand)

@manager.command
def runserver_gevent():
    from gevent import pywsgi
    server=pywsgi.WSGIServer(("127.0.0.1",5000),app)
    server.serve_forever()

if __name__=="__main__":
    manager.run()

