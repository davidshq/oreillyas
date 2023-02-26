import sqlite3

conn = sqlite3.connect('oreilly.db')
cur = conn.cursor()

# Get all the publishers
publishers = cur.execute('SELECT name from publishers').fetchall()

# Update the count column for each publisher
for publisher in publishers:
    count = cur.execute(f'SELECT COUNT(*) FROM publisher_books WHERE publisher_id = (SELECT id FROM publishers WHERE name = "{publisher[0]}")').fetchone()[0]
    cur.execute(f'UPDATE publishers SET book_count = {count} WHERE name = "{publisher[0]}"')

conn.commit()

