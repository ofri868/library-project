import datetime
from project.books.models import Book
from project.customers.models import Customer
from project.loans.models import Loan
from project import db, app
with app.app_context():
    
    # Adding books
    db.session.add(Book("Harry Potter", "J.K Rowling", 2000, 1))
    db.session.add(Book("The Hobbit", "J.R.R Tolkein", 2000, 2))
    db.session.add(Book("Percy Jackson", "Rick Riordan", 2010, 2))
    db.session.add(Book("Nicholas Flamel", "Michael Scott", 2005, 3))

    # Adding customers
    db.session.add(Customer("Ofri Gal", "Modiin", 21))
    db.session.add(Customer("Matan Tarif", "Modiin", 24))
    db.session.add(Customer("Or Smadga", "Lod", 21))
    db.session.add(Customer("Niv Malichi", "Kfar Saba", 23))

    # Creating loans
    db.session.add(Loan(1, 3, datetime.date(2022,11,1),datetime.date(2022,11,6)))
    db.session.add(Loan(2, 2, datetime.date(2022,11,3),datetime.date(2022,11,8)))
    db.session.add(Loan(4, 1, datetime.date(2022,11,2),datetime.date(2022,11,4)))
    db.session.add(Loan(2, 4, datetime.date(2022,11,3),datetime.date(2022,11,13)))

    db.session.commit()
