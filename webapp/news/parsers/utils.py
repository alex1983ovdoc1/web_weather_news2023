import requests

from webapp.db import db
from webapp.news.models import News


def get_html(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
	try:
		result = requests.get(url, headers=headers)
		result.raise_for_status() # answer server
		return result.text
	# requests.RequestException 	- network problem
	# ValueError 					- server problem
	except(requests.RequestException, ValueError):
		print('-- NETWORK ERROR --')
		return False


def save_news(title, url, published):
	news_exists = News.query.filter(News.url == url).count()
	print(news_exists)
	if not news_exists:
		news_news = News(title=title, url=url, published=published)
		db.session.add(news_news)				# add to DB
		db.session.commit()						# save in DB		