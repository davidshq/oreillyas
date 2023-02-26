0.0.1 - 2/26/2023
- Can generate views if desired, see `./json-to-sqlite/generate_views.py`
- Can update publishers to include a count of books by each publisher, see `./json-to-sqlite/add_count_to_publishers.py`
- Includes a `migration-publishs-add-book_count.sql` file to allow existing databases to be updated with the new column
