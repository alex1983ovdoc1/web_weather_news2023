from flask import Flask, render_template
# from a2_weather import weather_by_city 
from webapp.weather_html import weather_by_city 
from webapp.python_news import get_python_news

'''
+ Add weather
# Flask -> Jinja2 {{ }} -> put values from Python to html (rander_template(x, y, ....))

'''

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        title = "News Python"
        #weather = weather_by_city('Kyiv,Ukraine')
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news = get_python_news()
        return render_template('index.html', page_title=title, weather = weather, news_list=news)
    return app
