from db.run_sql import run_sql
from models.author import Author
from models.book import Book


def save(author):
    sql = "INSERT INTO authors (title, author_id) VALUES (%s, %s) RETURNING *"
    values = [author.nam, author.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book


def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], author, row['id'] )
        authors.append(author)
    return authors