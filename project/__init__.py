from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
############ DATABASE SETUP ##############

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_library.sqlite3'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)
Migrate(app, db)

######### REGISTER BLUEPRINTS ############
from project.core.flask import core
from project.books.flask import books
from project.customers.flask import customers
from project.loans.flask import loans

app.register_blueprint(core)
app.register_blueprint(customers)
app.register_blueprint(books)
app.register_blueprint(loans)

with app.app_context():
    db.create_all()