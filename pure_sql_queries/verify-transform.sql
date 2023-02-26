-- Returns 10 results that joins the tables making it easy to check if the data
-- has been correctly added to the database, including relationships.
-- To run this query open the db for querying:
-- sqlite3 ../oreilly.db
select * from author_books 
    left join books on author_books.book_pid = books.pid 
    left join authors on author_books.author_id = authors.id
    limit 10;
