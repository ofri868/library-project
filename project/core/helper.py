import datetime
# gets loan date and book type and returns return date
def get_return_date(book,loandate):
    if book.type == 1:
        return loandate + datetime.timedelta(days=10)
    if book.type == 2:
        return loandate + datetime.timedelta(days=5)
    if book.type == 3:
        return loandate + datetime.timedelta(days=2)

def check_if_free(book, loans):
    for loan in loans:
        if loan.book_id == book.book_id:
            return False
    return True
def check_customer_loans(customer, loans):
    for loan in loans:
        if customer.customer_id == loan.customer_id:
            return True
    return False

def check_active_book(book, loans):
    for loan in loans:
        if book.book_id == loan.book_id:
            return True
    return False