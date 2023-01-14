# Create a new sqlite database oreilly.db
# Created using GitHub Copilot

import sqlite3

conn = sqlite3.connect('../oreilly.db')
cur = conn.cursor()

# Create a table books with the columns pid, id, title
cur.execute('CREATE TABLE books (pid INTEGER, id INTEGER, title TEXT)')

# Create a table authors with the columns id (primary key) and name
cur.execute('CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT)')

# Create a table author_books with the columns author_id, book_id
cur.execute('DROP TABLE IF EXISTS author_books')
cur.execute('CREATE TABLE author_books (author_id INTEGER, book_pid INTEGER)')

# Commit the changes and close the connection
conn.commit()
conn.close()