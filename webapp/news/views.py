from flask import abort, Blueprint, current_app, render_template

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
    news_list = News.query.filter(News.text.isnot(None)).order_by(News.published.desc()).all()                                         # go function news
    return render_template('news/index.html', page_title=title, weather = weather, news_list=news_list) # send to site


# text new's from DB to my site
@blueprint.route('/news/<int:news_id>')
def single_news(news_id):
    my_news = News.query.filter(News.id == news_id).first()

    if not my_news:
        abort(404)
    return render_template('news/single_news.html', page_title=my_news.title, news=my_news)