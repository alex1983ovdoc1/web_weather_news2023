
from flask import Flask, render_template
# from a2_weather import weather_by_city 

from webapp.model import db
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


    @app.route('/')                                                 # start flask's object -> app
    def index():
        title = "News Python"                                       # name title
        #weather = weather_by_city('Kyiv,Ukraine')
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])           # go function weather
        news_list = get_python_news()                                           # go function news
        return render_template('index.html', page_title=title, weather = weather, news_list=news_list) # send to site
    return app
