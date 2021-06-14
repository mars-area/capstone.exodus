import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkeyforcapstonebangkit21'

    from .views import views
    from .get_prediction import get_prediction

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(get_prediction, url_prefix='/')
    
    return app