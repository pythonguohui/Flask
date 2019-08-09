from  flask import Flask
from BluePrint1 import simple_blueprint1
from BluePrint2 import simple_blueprint2



app=Flask(__name__)
app.register_blueprint(simple_blueprint1)
app.register_blueprint(simple_blueprint2)

if __name__=="__main__":
    app.run()