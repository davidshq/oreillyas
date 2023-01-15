# Takes the oreilly.json file and transforms it into a SQLite database
# Created with GitHub Copilot
# Note: This is step 4 in the process. Make sure you've already completed the previous steps:
#   Step 1. Download the JSON using main.py
#   Step 2. Add a pid field to each book using add_pid_to_json.py
#   Step 3. Create the database and tables using create_db.py

import json
import sqlite3

# Load the json into Python
fname = '../oreilly-pid.json'
str_data = open(fname).read()
data = json.loads(str_data)

# Open a connection to oreilly.db
conn = sqlite3.connect('../oreilly.db')
cur = conn.cursor()

# For each book in the data list add a row to the books table
for book in data:
    cur.execute('INSERT INTO books (pid, id, title) VALUES (?, ?, ?)', (book['pid'], book['id'], book['title']))

# For each unique author in the data list add a row to the authors table with a unique 
# id and the author's name

# Create a set of all the authors in the data list
authors = set()
for book in data:
    for author in book['authors']:
        authors.add(author)

# Add a row to the authors table for each author in the set
for (id, author) in enumerate(authors):
    cur.execute('INSERT INTO authors (id, name) VALUES (?, ?)', (id, author))

# For each book in the data list add a row to the author_books table
# for each author of the book

# Create a dictionary of authors where the key is the author's name and the value is the0
# author's id
author_ids = {}
for (id, author) in enumerate(authors):
    author_ids[author] = id

# Add a row to the author_books table for each author of each book
for book in data:
    for author in book['authors']:
        cur.execute('INSERT INTO author_books (author_id, book_pid) VALUES (?, ?)', (author_ids[author], book['pid']))

# Commit the changes and close the connection
conn.commit()
conn.close()
