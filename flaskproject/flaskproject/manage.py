from flaskproject.models import models
from flaskproject.views import app


if __name__=="__main__":
    models.create_all()
    app.run()