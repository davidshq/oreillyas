# Takes the oreilly.json file and transforms it into a SQLite database
# Created with GitHub Copilot
# Note: This is step 4 in the process. Make sure you've already completed the previous steps:
#   Step 1. Download the JSON using main.py
#   Step 2. Add a pid field to each book using add_pid_to_json.py
#   Step 3. Create the database and tables using create_db.py

import json
import sqlite3

# Load the json into Python
fname = 'oreilly-pid.json'
str_data = open(fname).read()
data = json.loads(str_data)

# Open a connection to oreilly.db
conn = sqlite3.connect('oreilly.db')
cur = conn.cursor()

# For each book in the data list add a row to the books table
for book in data:
    pid = book.get('pid', '')
    isbn = book.get('isbn', '')
    title = book.get('title', '')
    virtual_pages = book.get('virtual_pages', '')
    average_rating = book.get('average_rating', '')
    popularity = book.get('popularity', '')
    report_score = book.get('report_score', '')
    issued = book.get('issued', '')
    description = book.get('description', '')
    url = book.get('url', '')
    minutes_required = book.get('minutes_required', '')
    date_added = book.get('date_added', '')
    last_modified_time = book.get('last_modified_time', '')
    language = book.get('language', '')
    timestamp = book.get('timestamp', '')
    cover_url = book.get('cover_url', '')
    id = book.get('id', '')
    ourn = book.get('ourn', '')
    cur.execute('INSERT INTO books (pid, isbn, title, virtual_pages, average_rating, popularity, report_score, issued, description, url, minutes_required, date_added, last_modified_time, language, timestamp, cover_url, id, ourn) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (pid, isbn, title, virtual_pages, average_rating, popularity, report_score, issued, description, url, minutes_required, date_added, last_modified_time, language, timestamp, cover_url, id, ourn))

# For each unique author in the data list add a row to the authors table with a unique 
# id and the author's name

# Create a set of all the authors in the data list
authors = set()
for book in data:
    book_authors = book.get('authors', '')
    for author in book_authors:
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
    authors = book.get('authors', '')
    for author in authors:
        cur.execute('INSERT INTO author_books (author_id, book_pid) VALUES (?, ?)', (author_ids[author], book['pid']))

# For each unique publisher in the data list add a row to the publishers table with a unique
# id and the publisher's name

# Create a set of all the publishers in the data list
publishers = set()
for book in data:
    book_publishers = book.get('publishers', '')
    for publisher in book_publishers:
        publishers.add(publisher)

# Add a row to the publishers table for each publisher in the set   
for (id, publisher) in enumerate(publishers):
    cur.execute('INSERT INTO publishers (id, name) VALUES (?, ?)', (id, publisher))

# For each book in the data list add a row to the publisher_books table
# for each publisher of the book

# Create a dictionary of publishers where the key is the publisher's name and the value is the
# publisher's id
publisher_ids = {}
for (id, publisher) in enumerate(publishers):
    publisher_ids[publisher] = id

# Add a row to the publisher_books table for each publisher of each book
for book in data:
    publishers = book.get('publishers', '')
    for publisher in publishers:
        if publisher != '':
            cur.execute('INSERT INTO publisher_books (publisher_id, book_pid) VALUES (?, ?)', (publisher_ids[publisher], book['pid']))

# For each unique topic in the data list add a row to the topics table with a unique
# id and the topic's name

# Create a set of all the topics_payload in the data list
all_topics = set()
for book in data:
    for topics_payload in book:
        topics = book.get('topics_payload', '')
        for topic in topics:
            uuid = topic.get('uuid', '')
            slug = topic.get('slug', '')
            name = topic.get('name', '')
            score = topic.get('score', '')
            all_topics.add((uuid, slug, name, score))
        
# Add a row to the topics table for each topic in the set
for (id, topic) in enumerate(all_topics):
    cur.execute('INSERT INTO topics (id, uuid, slug, name, score) VALUES (?, ?, ?, ?, ?)', (id, topic[0], topic[1], topic[2], topic[3]))

# For each book in the data list add a row to the topic_books table
# for each topic of the book

# Create a dictionary of topics where the key is the topic's name and the value is the
# topic's id
topic_ids = {}
for (id, topic) in enumerate(all_topics):
    topic_ids[topic] = id

# Add a row to the topic_books table for each topic of each book
for book in data:
    topics = book.get('topics_payload', '')
    for topic in topics:
        uuid = topic.get('uuid', '')
        slug = topic.get('slug', '')
        name = topic.get('name', '')
        score = topic.get('score', '')
        cur.execute('INSERT INTO topic_books (topic_id, book_pid) VALUES (?, ?)', (topic_ids[(uuid, slug, name, score)], book['pid']))

# Commit the changes and close the connection
conn.commit()
conn.close()
