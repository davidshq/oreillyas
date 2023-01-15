# Create a new sqlite database oreilly.db
# Created using GitHub Copilot

import sqlite3

conn = sqlite3.connect('oreilly.db')
cur = conn.cursor()

# Create a table books with the columns pid, id, title
cur.execute('DROP TABLE IF EXISTS books')
cur.execute('CREATE TABLE books (pid INTEGER, isbn TEXT, title TEXT, virtual_pages INTEGER, average_rating INTEGER, popularity INTEGER, report_score INTEGER, issued TEXT, description TEXT, url TEXT, minutes_required INTEGER, date_added TEXT, last_modified_time TEXT, language TEXT, timestamp TEXT, cover_url TEXT, id INTEGER, ourn TEXT)')

# Create a table authors with the columns id (primary key) and name
cur.execute('DROP TABLE IF EXISTS authors')
cur.execute('CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT)')

# Create a table author_books with the columns author_id, book_id
cur.execute('DROP TABLE IF EXISTS author_books')
cur.execute('CREATE TABLE author_books (id INTEGER PRIMARY KEY AUTOINCREMENT, author_id INTEGER, book_pid INTEGER)')

# Create a table publishers with the columns id (primary key) and name
cur.execute('DROP TABLE IF EXISTS publishers')
cur.execute('CREATE TABLE publishers (id INTEGER PRIMARY KEY, name TEXT)')

# Create a table publisher_books with the columns publisher_id, book_id
cur.execute('DROP TABLE IF EXISTS publisher_books')
cur.execute('CREATE TABLE publisher_books (id INTEGER PRIMARY KEY AUTOINCREMENT, publisher_id INTEGER, book_pid INTEGER)')

# Create a table topics with the columns id (primary key) and name
cur.execute('DROP TABLE IF EXISTS topics')
cur.execute('CREATE TABLE topics(id INTEGER PRIMARY KEY, uuid TEXT, slug TEXT, name TEXT, score INTEGER)')

# Create a table topic_books with the columns topic_id, book_id
cur.execute('DROP TABLE IF EXISTS topic_books')
cur.execute('CREATE TABLE topic_books (id INTEGER PRIMARY KEY AUTOINCREMENT, topic_id INTEGER, book_pid INTEGER)')

# Commit the changes and close the connection
conn.commit()
conn.close()