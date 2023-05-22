from datetime import datetime, timedelta
import locale
import platform

from bs4 import BeautifulSoup

from webapp.db import db
from webapp.news.models import News
from webapp.news.parsers.utils import get_html, save_news


# for date formating local
if platform.system() == 'Windows':
	locale.setlocale(locale.LC_ALL, "russian")
else:
	locale.setlocale(locale.LC_TIME, 'ru_RU')


# formation date "сегодня в 02:32" to '19 05 2023 02:32'
def parse_habr_date(date_str):
	if 'сегодня' in date_str:
		today = datetime.now()
		date_str = date_str.replace('сегодня', today.strftime('%d %B %Y'))
	elif 'вчера' in date_str:
		yesterday = datetime.now() - timedelta(days=1)
		date_str = date_str.replace('вчера', yesterday.strftime('%d %B %Y'))
	# print(date_str)
	try:
		return datetime.strptime(date_str, '%d %b %Y в %H:%M')
	except ValueError:
		return datetime.now()


# news from habr.com (title, ulr, date)
def get_news_snippets():
	html = get_html("https://habr.com/ru/search/?target_type=posts&q=python&order_by=date")
	if html:
		soup = BeautifulSoup(html, 'html.parser')
		all_news = soup.find('div', class_="tm-articles-list").findAll('article', class_='tm-articles-list__item')
		# all_news = all_news.findAll('ul', class_="menu").findAll('li')
		result_news = []
		for news in all_news:
			title = news.find('a', class_="tm-title__link").text
			url = news.find('a', class_="tm-title__link")['href']
			url = 'https://habr.com' + url
			published = news.find('span', class_="tm-article-datetime-published").text
			published = parse_habr_date(published)
			save_news(title, url, published)
			# print('----------------------------')
			# print(title, url, published)
			# print('++++++++++++++++++++++++++++')


# text for news (take content from site)
def get_news_content():
	news_without_text = News.query.filter(News.text.is_(None))
	for news in news_without_text:
		html = get_html(news.url)
		if html:
			soup = BeautifulSoup(html, 'html.parser')
			news_text = soup.find('div', class_='article-formatted-body').decode_contents()
			# print(news_text)
			if news_text:
				news.text = news_text
				db.session.add(news)
				db.session.commit()

