from flask import Flask, render_template
from repositories import author_repository
from repositories import book_repository
from models.book import Book
from models.author import Author
from flask import Blueprint



books_blueprint = Blueprint("books", __name__)

# @books_blueprint.route('/')
# def books():
#     books = book_repository.select_all()
#     return render_template("tasks/index.html", all_books=books)

# NEW
# GET '/books/new'


# CREATE
# POST '/books'

# SHOW
# GET '/books/<id>'

# EDIT
# GET '/books/<id>/edit'

# UPDATE
# PUT '/books/<id>'

# DELETE
# DELETE '/books/<id>'

