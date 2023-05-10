from getpass import getpass
import sys

from webapp import create_app
from webapp.model import db, User


app = create_app() # create object for DB

with app.app_context(): 									# open DB
	username = input('Enter name: ')

	if User.query.filter(User.username == username).count(): # check DB
		print("This name is used, enter enother name...")
		sys.exit(0)

	password1 = getpass("Enter password: ")
	password2 = getpass("Repeat password: ")

	if not password1 == password2:              			# check password
		print("Passwords are different...")
		sys.exit(0)

	new_user = User(username=username, role='admin')		# create user
	new_user.set_password(password1)						# hash password

	db.session.add(new_user)								# add user to DB
	db.session.commit()										# close DB
	print("User with id {} added !".format(new_user.id))



