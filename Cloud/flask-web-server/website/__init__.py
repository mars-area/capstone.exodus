import os
from flask import Flask

def create_app():
    # static_url_path='/static' use for passing image from folder static to html
    app = Flask(__name__, static_url_path='/static')
    app.config['SECRET_KEY'] = 'secretkeyforcapstonebangkit21'

    from .views import views
    from .get_prediction import get_prediction

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(get_prediction, url_prefix='/')
    
    return app