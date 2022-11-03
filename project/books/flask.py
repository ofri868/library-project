from flask import render_template,redirect, Blueprint, request
from project.books.models import Book
from project.loans.models import Loan
from project.core.helper import check_active_book
from project import db

books = Blueprint('books', __name__, template_folder='templates', url_prefix='/books')

# displays books
@books.route("/<ind>")
@books.route("/")
def display_books(ind =0):
    # one book
    if int(ind) > 0:
        book=Book.query.get(int(ind))
        return render_template('Book.html',book=book) 
    # all books
    return render_template('All_Books.html',books= Book.query.all())

# add a new book
@books.route("/add/", methods=['POST','GET'])
def add_book():
    if request.method == "POST":
        book_name= request.form.get("bookname")
        author= request.form.get("author")
        year_published = int(request.form.get("yearpublished"))
        type = int(request.form.get("type"))
        newBook= Book(book_name, author, year_published, type)
        db.session.add (newBook)
        db.session.commit()
        return render_template('All_Books.html',books= Book.query.all())
    if request.method == "GET":
        return render_template('add_book.html')

# delete a book
@books.route("/delete/<ind>", methods=['DELETE','GET'])
def del_book(ind=0):
    book=Book.query.get(int(ind))
    if book:
        if(check_active_book(book, Loan.query.filter_by(returned = False))):
            return render_template('All_Books.html',books= Book.query.all(), cant_delete = True)
        else:
            db.session.delete(book)
            db.session.commit()
            return render_template('All_Books.html',books= Book.query.all(), deleted = True)
    else:
        return render_template('All_Books.html',books= Book.query.all(), not_found = False)

@books.route("/find/", methods=['POST'])
def find_book():
    book_name = request.form.get("bookname")
    book=Book.query.filter_by(book_name=book_name).first()
    if book:
        return redirect(f"/books/{book.book_id}")
    else:
        book_name = book_name.title()
        book=Book.query.filter_by(book_name=book_name).first()
        if book:
            return redirect(f"/books/{book.book_id}")
    return render_template('All_books.html',books= Book.query.all(), not_found = True)