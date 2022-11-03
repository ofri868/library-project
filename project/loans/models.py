from project import db, app

class Loan(db.Model):
    loan_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))
    loandate = db.Column(db.Date, nullable=False)
    returndate = db.Column(db.Date, nullable=False)
    returned = db.Column(db.Boolean, nullable=False)


    def __init__(self, customer_id, book_id, loandate, returndate):
        self.customer_id=customer_id
        self.book_id = book_id
        self.loandate = loandate
        self.returndate = returndate
        self.returned = False
