from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()                                   # create db's object

class News(db.Model):                                       # class News inheritans with .Model (DB SQLite)
    id = db.Column(db.Integer, primary_key=True)            # id news (number)
    title = db.Column(db.String, nullable=False)            # column title
    url = db.Column(db.String, unique=True, nullable=False) # column url
    published = db.Column(db.DateTime, nullable=False)      # column published
    text = db.Column(db.Text, nullable=True)                # text news (nullable=True -> None)

    def __repr__(self):
        return '<News {} {}>'.format(self.title, self.url)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'
    

    def __repr__(self):
        return '<User name: {} id: {}>'.format(self.username, self.id)


