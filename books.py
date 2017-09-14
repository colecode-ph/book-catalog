from flask import Flask, request, render_template, redirect, url_for, flash
app = Flask(__name__)

from sqlalchemy import create_engine, func, update
from sqlalchemy.orm import sessionmaker
from book_db_setup import Base, Category, Book

engine = create_engine('sqlite:///books.db')
Base.metadata.bind = engine
# binds the engine to the Base class
# makes the connections between class definitions & corresponding tables in db
DBSession = sessionmaker(bind = engine)
# creates sessionmaker object, which establishes link of
# communication between our code executions and the engine we created
session = DBSession()
# create an instance of the DBSession  object - to make a changes
# to the database, we can call a method within the session

@app.route('/')
def indexPage():
    """ Shows a list of books """
    books = session.query(Book).order_by(Book.title)
    return render_template('index.html', books = books)

# category stuff

@app.route('/categories')
def listCategories():
    return "This is the page which lists all the categories!"

@app.route('/categories/create')
def createCategory():
    return "This is the page to create a new category!"

@app.route('/categories/edit')
def editCategory():
    return "This is the page to edit a category!"

@app.route('/categories/delete')
def deleteCategory():
    return "This is the page to delete a category!"

# book stuff

@app.route('/categories/books')
def listBooks():
    return "This is page which lists the books within a category!"

@app.route('/categories/books/create')
def createBook():
    return "This is the page to create a new book!"

@app.route('/categories/books/edit')
def editBooks():
    return "This is the page to edit info for an existing book!"

@app.route('/categories/books/delete')
def deleteBook():
    return "This is the page to delete a book from the db!"

# Oauth stuff

@app.route('/login')
def gconnect():
    return "This is the URL for authentication via Google+ OAuth 2"

@app.route('/disconnect')
def gdisconnect():
    return "This is the URL for disconnecting from Google OAuth 2"

# JSON stuff

@app.route('/json')
def indexPageJSON():
    return "This is the JSON data for the index page!"

@app.route('/categories/books/JSON')
def listBooksJSON():
    return "This is the JSON data for the books list page for a particular category!"










if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)




