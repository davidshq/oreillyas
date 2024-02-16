# Instead of ending up with a JSON file and a SQLite database, this alternative
# allows us to import the data into a Neo4j database.

import os
from time import sleep

import requests
from neo4j import GraphDatabase
from dotenv import load_dotenv
from get_num_of_items import get_num_of_items

load_dotenv()

URI = os.getenv('NEO4J_URI')
AUTH = (os.getenv('NEO4J_USERNAME'), os.getenv('NEO4J_PASSWORD'))

header = ''

if 'OREILLY_API_KEY' in os.environ:
    OREILLY_API_KEY = os.getenv('OREILLY_API_KEY')

    # Add the API key to the header
    header = {
        'Authorization': 'Token {}'.format(OREILLY_API_KEY),
    }

start_page = 0
current_page = start_page
end_page = 2 # int(get_num_of_items() / 200)

items = []

per_page = 5 # 200 for production
highlight = 0

exclude_fields = [
    'academic_excluded',
    'archive_id',
    'chapter_title',
    'duration_seconds',
    'has_assessment',
    'source']

exclude_field_string = ''
for field in exclude_fields:
    exclude_field_string += f'&exclude_fields={field}'

url = f'https://learning.oreilly.com/api/v2/search/?query=*&formats=book&limit={per_page}&highlight={highlight}&{exclude_field_string}'

def merge_book(tx, book):
    query = """
    MERGE (a:Book {
        isbn: $isbn,
        title: $title,
        virtual_pages: $virtual_pages,
        average_rating: $average_rating,
        popularity: $popularity,
        report_score: $report_score,
        issued: $issued,
        description: $description,
        url: $url,
        minutes_required: $minutes_required,
        date_added: $date_added,
        last_modified_time: $last_modified_time,
        language: $language,
        timestamp: $timestamp,
        cover_url: $cover_url,
        id: $id,
        ourn: $ourn
    })
    """
    tx.run(query,
        isbn=book.get("isbn", ""),
        title=book.get("title", ""),
        virtual_pages=book.get("virtual_pages", ""),
        average_rating=book.get("average_rating", ""),
        popularity=book.get("popularity", ""),
        report_score=book.get("report_score", ""),
        issued=book.get("issued", ""),
        description=book.get("description", ""),
        url=book.get("url", ""),
        minutes_required=book.get("minutes_required", ""),
        date_added=book.get("date_added", ""),
        last_modified_time=book.get("last_modified_time", ""),
        language=book.get("language", ""),
        timestamp=book.get("timestamp", ""),
        cover_url=book.get("cover_url", ""),
        id=book.get("id", ""),
        ourn=book.get("ourn", ""))

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    while current_page is not end_page + 1:
        if header:  # If we have an API key, use it.
            response = requests.get(url, headers=header)
        else:
            response = requests.get(url)

        json_response = response.json()

        next_url = json_response["next"]
        print(next_url)
        if next_url is None:
            print("No more pages to pull.")
            break

        json_items = json_response["results"]

        # Add to Neo4J database
        with driver.session() as session:
            for book in json_items:
                session.execute_write(merge_book, book)

        current_page += 1
        print(f"Current Page: {current_page}")

        # Update URL for next call
        url = next_url

        # Don't hammer the API
        sleep(1)

