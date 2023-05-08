
from webapp import db, create_app


app=create_app()          	# object DB SQLite from function create_app
with app.app_context():
	db.create_all()			# create ampty DB (name from config.py 'webapp.db')
