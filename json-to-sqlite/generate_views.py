import sqlite3
import re

# Open a connection to oreilly.db
conn = sqlite3.connect('oreilly.db')
cur = conn.cursor()

# Get all the publishers
publishers = cur.execute('SELECT name from publishers').fetchall()

# Create a view for each publisher
for publisher in publishers:
    view_name = re.sub("[&:(),./']", '', publisher[0].replace(' ', '_').replace('&', 'and'))
    view_name = view_name.replace('-', '')
    cur.execute(f"DROP VIEW IF EXISTS {view_name}")
    cur.execute(f"DROP VIEW IF EXISTS {view_name}_view")
    sql = f"""CREATE VIEW {view_name} AS SELECT b.title, group_concat(a.name) AS "author", p.name AS "publisher", 
        b.virtual_pages, b.average_rating, b.report_score, b.popularity, b.issued, b.description, b.url
        FROM publisher_books pb
        LEFT JOIN books b on b.pid = pb.book_pid
        LEFT JOIN publishers p on p.id = pb.publisher_id
        LEFT JOIN author_books ab on ab.book_pid = b.pid
        LEFT JOIN authors a on a.id = ab.author_id
        LEFT JOIN topic_books tb on tb.book_pid = b.pid
        LEFT JOIN topics t on t.id = tb.topic_id
        WHERE p.name = "{publisher[0]}"
        GROUP BY b.title
    """
    print(sql)
    cur.execute(sql)

conn.commit()

# List of publishes with multiple names
publishers = {
    'Elsevier', 
    'McGraw-Hill', 
    'Wiley', 
    'NSA', 
    'MIT',
    'Prentice Hall',
    'Adobe',
    'IBM',
    'CRC Press',
    'Wrox',
    'De Gruyter',
    'Pearson'
    }

# Create a complete view of each publisher with multiple names
for publisher in publishers:
    view_name = re.sub("[&:(),./']", '', publisher.replace(' ', '_').replace('&', 'and'))
    view_name = view_name.replace('-', '')
    cur.execute(f"DROP VIEW IF EXISTS complete_{view_name}")
    sql = f"""CREATE VIEW complete_{view_name} AS SELECT b.title, group_concat(a.name) AS "author", p.name AS "publisher", 
        b.virtual_pages, b.average_rating, b.report_score, b.popularity, b.issued, b.description, b.url
        FROM publisher_books pb
        LEFT JOIN books b on b.pid = pb.book_pid
        LEFT JOIN publishers p on p.id = pb.publisher_id
        LEFT JOIN author_books ab on ab.book_pid = b.pid
        LEFT JOIN authors a on a.id = ab.author_id
        LEFT JOIN topic_books tb on tb.book_pid = b.pid
        LEFT JOIN topics t on t.id = tb.topic_id
        WHERE p.name LIKE "%{publisher}%"
        GROUP BY b.title
    """
    print(sql)
    cur.execute(sql)
conn.close()