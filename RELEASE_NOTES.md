
0.0.3 - 3/8/2024
- Adds script to convert JSON to Neo4j graph db.
- Adds `.editorconfig`, updates README, update `.env-example`.
- Removes outdated `dolt-schema.sql` (dolt not used).
- Adds `neo4j` as a dependency.

0.0.2 - 11/25/2023
- Added `.python-version` for pyenv; minor update to README.

0.0.1 - 2/26/2023
- Can generate views if desired, see `./json-to-sqlite/generate_views.py`
- Can update publishers to include a count of books by each publisher, see `./json-to-sqlite/add_count_to_publishers.py`
- Includes a `migration-publishs-add-book_count.sql` file to allow existing databases to be updated with the new column
