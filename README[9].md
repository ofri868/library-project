# Library Project

Welcome to my library project.

In order to make the most out of this website, please read this document fully, its not that long ;)

## Deployment

To deploy this project run

```bash
  py .\main.py
```
In order to populate the database, use the init_db.py file: 

```bash
  py .\init_db.py
```

## The main features of my website

- Add, view, delete and search for books
- Add, view, search for and manage active/inactive customers
- Create new loans and view all active loans
- See all late loans

## A few extra features 

- All returned loans are saved and can be viewed by clicking the loan history button
- Searching for books and customers is not caps sensitive
- Books or customers cannot be deleted if they are a part of an active loan
- If an action (add, delete, search) failed, a message will detail why the action failed

## Guidelines

- To create a standart, when adding new books/customers please capitalize
- when searching for books/customers, use the full name of the book/customer
## Authors

- The project was created by [Ofri Gal](https://www.github.com/ofri868)

