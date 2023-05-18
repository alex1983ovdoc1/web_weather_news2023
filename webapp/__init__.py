
from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager,current_user, login_required
from flask_migrate import Migrate

from webapp.db import db
from webapp.admin.views import blueprint as admin_blueprint
from webapp.news.views import blueprint as news_blueprint
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint


'''
+ Add weather
# Flask -> Jinja2 {{ }} -> put values from Python to html (rander_template(x, y, ....))

'''



def create_app():
    app = Flask(__name__)                   # create Flask's object
    app.config.from_pyfile('config.py')     # load config.py -> .config + .from_pyfile
    db.init_app(app)                        # initialisation db object (App)
    migrate = Migrate(app, db)              # create object migrate for DB

    login_manager = LoginManager()          # create logMan's object
    login_manager.init_app(app)             # initialisation object
    # login_manager.login_view = 'user.login' # name function for this object
    login_manager.login_view = 'user.login' # name function for this object

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(news_blueprint)
    app.register_blueprint(user_blueprint)   # inithialization user_blueprint


    # gived user from DB
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id) 


    return app
