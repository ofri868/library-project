from project import db, app

class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    year_published = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    loans = db.relationship('Loan', backref='book', lazy=True)


    def __init__(self, book_name, author, year_published, type):
        self.book_name=book_name
        self.author = author
        self.year_published = year_published
        self.type = type
