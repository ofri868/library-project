from flask import render_template,redirect, Blueprint, request
from project.customers.models import Customer
from project.loans.models import Loan
from project.core.helper import check_customer_loans
from project import db

customers = Blueprint('customers', __name__, template_folder='templates', url_prefix='/customers')

# displays customers
@customers.route("/<ind>")
@customers.route("/")
def display_customers(ind =0):
    #inactive customers
    if int(ind) == -1:
        return render_template('All_Customers.html',customers= Customer.query.filter_by(active = False), inactive = True)
    # one customer
    if int(ind) > 0:
        customer=Customer.query.get(int(ind))
        return render_template('Customer.html',customer=customer) 
    # all customers
    return render_template('All_Customers.html',customers= Customer.query.filter_by(active = True))

# add a new customer
@customers.route("/add/", methods=['POST','GET'])
def add_customer():
    if request.method == "POST":
        name= request.form.get("customername")
        city= request.form.get("city")
        age= request.form.get("age")
        newCustomer= Customer(name, city, age)
        db.session.add (newCustomer)
        db.session.commit()
        return render_template('All_Customers.html',customers= Customer.query.all())
    if request.method == "GET":
        return render_template('add_customer.html')

#delete a customer
@customers.route("/delete/<ind>", methods=['DELETE','GET'])
def del_customer(ind=0):
    customer=Customer.query.get(int(ind))
    if customer:
        if(check_customer_loans(customer, Loan.query.filter_by(returned = False))):
            return render_template('All_Customers.html',customers= Customer.query.all(), cant_delete = True)
        else:
            customer.active = False
            db.session.commit()
            return render_template('All_Customers.html',customers= Customer.query.all(), deleted = True)
    else:
        return render_template('All_Customers.html',customers= Customer.query.all(), not_found = True)

@customers.route("/find/", methods=['POST'])
def find_customer():
    customer_name = request.form.get("customername")
    customer=Customer.query.filter_by(customer_name=customer_name).first()
    if customer:
        return redirect(f"/customers/{customer.customer_id}")
    else:
        customer_name = customer_name.title()
        customer=Customer.query.filter_by(customer_name=customer_name).first()
        if customer:
            return redirect(f"/customers/{customer.customer_id}")        
    return render_template('All_Customers.html',customers= Customer.query.all(), not_found = True)