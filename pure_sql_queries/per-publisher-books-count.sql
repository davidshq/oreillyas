SELECT publishers.name, COUNT(*) AS the_count FROM books 
LEFT JOIN publisher_books ON books.pid = publisher_books.book_pid 
LEFT JOIN publishers ON publisher_books.publisher_id = publishers.id
GROUP BY publisher_books.publisher_id
ORDER BY the_count DESC