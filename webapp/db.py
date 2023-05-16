from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()                                   # create db's object


# class News(db.Model):                                       # class News inheritans with .Model (DB SQLite)
#     id = db.Column(db.Integer, primary_key=True)            # id news (number)
#     title = db.Column(db.String, nullable=False)            # column title
#     url = db.Column(db.String, unique=True, nullable=False) # column url
#     published = db.Column(db.DateTime, nullable=False)      # column published
#     text = db.Column(db.Text, nullable=True)                # text news (nullable=True -> None)

#     def __repr__(self):
#         return '<News {} {}>'.format(self.title, self.url)




