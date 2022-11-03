from project import db, app

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    loans = db.relationship('Loan', backref='customer', lazy=True)


    def __init__(self, customer_name, city, age):
        self.customer_name=customer_name
        self.city = city
        self.age = age
        self.active = True
