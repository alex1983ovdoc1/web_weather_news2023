from flask import Blueprint, current_app, render_template

# from webapp.python_news import get_python_news
from webapp.news.models import News
from webapp.weather_html import weather_by_city 


blueprint = Blueprint('news', __name__)


# @app.route('/')                                                 # start flask's object -> app
@blueprint.route('/') 
def index():
    title = "News Python"                                       # name title
    #weather = weather_by_city('Kyiv,Ukraine')
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])           # go function weather
    # news_list = get_python_news()
    news_list = News.query.order_by(News.published.desc()).all()                                           # go function news
    return render_template('news/index.html', page_title=title, weather = weather, news_list=news_list) # send to site