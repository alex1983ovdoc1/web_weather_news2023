
from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
# from a2_weather import weather_by_city 

from webapp.forms import LoginForm
from webapp.model import db, News, User
from webapp.weather_html import weather_by_city 
from webapp.python_news import get_python_news


'''
+ Add weather
# Flask -> Jinja2 {{ }} -> put values from Python to html (rander_template(x, y, ....))

'''



def create_app():
    app = Flask(__name__)                   # create Flask's object
    app.config.from_pyfile('config.py')     # load config.py -> .config + .from_pyfile
    db.init_app(app)                        # initialisation db object (App)

    login_manager = LoginManager()          # create logMan's object
    login_manager.init_app(app)             # initialisation object
    login_manager.login_view = 'login'      # name function for this object

    # gived user from DB
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')                                                 # start flask's object -> app
    def index():
        title = "News Python"                                       # name title
        #weather = weather_by_city('Kyiv,Ukraine')
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])           # go function weather
        # news_list = get_python_news()
        news_list = News.query.order_by(News.published.desc()).all()                                           # go function news
        return render_template('index.html', page_title=title, weather = weather, news_list=news_list) # send to site


    # user's form
    @app.route('/login')
    def login():
        if current_user.is_authenticated:           # if user authenticated
            return redirect(url_for('index'))       # go start page
        title = 'Authorization'
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)


    # processing login
    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()

        if form.validate_on_submit():
            user = User.query.filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('/ You going in site! /')
                return redirect(url_for('index'))
        flash('/ Name or password not correct /')
        return redirect(url_for('login'))

    # user logout
    @app.route('/logout')
    def logout():
        logout_user()
        flash('/ You logout from site. /')
        return redirect(url_for('index'))

    # page for admin
    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return "Hello admin!"
        else:
            return "You aren't admin."


    return app
