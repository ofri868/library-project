from flask import render_template, Blueprint, request
from project.customers.models import Customer
from project.loans.models import Loan
from project.books.models import Book
from project.core.helper import get_return_date, check_if_free
from project import db
import datetime
from datetime import date

loans = Blueprint('loans', __name__, template_folder='templates', url_prefix='/loans')

# displays active loans
@loans.route("/<ind>")
@loans.route("/")
def display_loans(ind =0):
    # loan history
    if int(ind) == -1:
        return render_template('All_Loans.html',loans = Loan.query.filter_by(returned = True),history = True)
    # one loan
    if int(ind) > 0:
        loan=Loan.query.get(int(ind))
        return render_template('Loan.html',loan=loan) 
    # all loans
    return render_template('All_Loans.html',loans = Loan.query.filter_by(returned = False))

# displays all late loans
@loans.route("/late_loans/")
def display_late_loans():
    late_loans = []
    loans = Loan.query.filter_by(returned = False)
    for loan in loans:
        if loan.returndate < datetime.date.today():
            late_loans.append(loan)
    return render_template('Late_loans.html',late_loans=late_loans)

#create a new loan
@loans.route("/add/", methods=['POST','GET'])
def new_loan():
    if request.method == "POST":
        customer_id= request.form.get("customerid")
        book_id= int(request.form.get("bookid"))
        loandate = datetime.datetime.strptime(request.form.get("loandate"), '%Y-%m-%d')
        if Customer.query.get(customer_id):
            if Book.query.get(book_id):
                returndate = get_return_date(Book.query.get(book_id),loandate)
                if not (Customer.query.get(customer_id).active):
                    return render_template('All_Loans.html', loans = Loan.query.filter_by(returned = False), customer_inactive = True)
                if check_if_free(Book.query.get(book_id),Loan.query.filter_by(returned = False)):
                    newLoan= Loan(int(customer_id), int(book_id), loandate, returndate)
                    db.session.add (newLoan)
                    db.session.commit()
                    return render_template('All_Loans.html', loans = Loan.query.filter_by(returned = False), created = True)
                else:
                    return render_template('All_Loans.html', loans = Loan.query.filter_by(returned = False), created = False)
            else:
               return render_template('All_Loans.html', loans = Loan.query.filter_by(returned = False), b_not_found = True)    
        else:
            return render_template('All_Loans.html', loans = Loan.query.filter_by(returned = False), c_not_found = True)

    if request.method == "GET":
        return render_template('new_loan.html')

# return a loan
@loans.route("/return/<loan_id>", methods=['POST','GET'])
def return_loan(loan_id):
    loan = Loan.query.filter_by(loan_id=loan_id).first()
    loan.returned = True
    db.session.commit()
    return render_template('All_Loans.html', loans = Loan.query.filter_by(returned = False),returned_loan = True)
