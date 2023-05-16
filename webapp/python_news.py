from datetime import datetime

import requests
from bs4 import BeautifulSoup

from webapp.db import db
from webapp.news.models import News


def get_html(url):
	try:
		result = requests.get(url)
		result.raise_for_status() # answer server
		return result.text
	# requests.RequestException 	- network problem
	# ValueError 					- server problem
	except(requests.RequestException, ValueError):
		print('-- NETWORK ERROR --')
		return False


def get_python_news():
	html = get_html("https://www.python.org/")
	if html:
		soup = BeautifulSoup(html, 'html.parser')
		all_news = soup.find('div', class_="medium-widget blog-widget")
		all_news = all_news.find('ul', class_="menu").findAll('li')
		result_news = []
		for news in all_news:
			title = news.find('a').text
			url = news.find('a')['href']
			published = news.find('time').text
			try:
				published = datetime.strptime(published, '%Y-%m-%d')
			except ValueError:
				published = datetime.now()
	# 		result_news.append({
	# 			'title': title,
	# 			'url': url,
	# 			'published': published
	# 			})
	# 	return result_news
	# return False
			save_news(title, url, published)


def save_news(title, url, published):
	news_exists = News.query.filter(News.url == url).count()
	print(news_exists)
	if not news_exists:
		news_news = News(title=title, url=url, published=published)
		db.session.add(news_news)				# add to DB
		db.session.commit()						# save in DB