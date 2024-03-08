import os
import json
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

# Load the json into Python
fname = 'oreilly.json'
str_data = open(fname).read()
data = json.loads(str_data)

# Initiate the connection to the Neo4j database
uri = os.getenv('NEO4J_HOST') or ''
auth = (os.getenv('NEO4J_USERNAME'), os.getenv('NEO4J_PASSWORD'))
driver = GraphDatabase.driver(uri, auth=auth)

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
    
def merge_author(tx, author):
    query = """
    MERGE (a:Author {
        name: $name
    })
    """
    if isinstance(author, dict):
        author_name = author.get("name", "")
    else:
        author_name = author

    tx.run(query,
        name=author_name)

def merge_publisher(tx, publisher):
    query = """
    MERGE (a:Publisher {
        name: $name
    })
    """
    if isinstance(publisher, dict):
        publisher_name = publisher.get("name", "")
    else:
        publisher_name = publisher

    tx.run(query,
        name=publisher_name)
    
def merge_topic(tx, topic):
    query = """
    MERGE (t:Topic {name: $name, slug: $slug, uuid: $uuid, score: coalesce($score, 0)})
    """
    if isinstance(topic, dict):
        topic_name = topic.get("name", "")
    else:
        topic_name = topic

    if isinstance(topic, dict):
        topic_uuid = topic.get("uuid", "")
    else:
        topic_uuid = ""
    
    if isinstance(topic, dict):
        topic_slug = topic.get("slug", "")
    else:
        topic_slug = ""

    if isinstance(topic, dict):
        topic_score = topic.get("score", "")
    else:
        topic_score = ""

    tx.run(query,
        name = topic_name,
        slug = topic_slug,
        uuid=topic_uuid,
        score = topic_score)
    
# Create relationships between books and authors
def create_relationships_book(tx, book):
    for author in book.get("authors", []):
        tx.run("MATCH (a:Book {isbn: $isbn}) "
               "MATCH (b:Author {name: $name}) "
               "MERGE (a)-[:WRITTEN_BY]->(b)",
               isbn=book.get("isbn", ""),
               name=author)
        print(f"Creating relationship between {book.get('title', '')} and {author}")
        
# Create relationships between books and publishers
def create_relationships_publisher(tx, book):
    for publisher in book.get("publishers", []):
        tx.run("MATCH (a:Book {isbn: $isbn}) "
               "MATCH (b:Publisher {name: $name}) "
               "MERGE (a)-[:PUBLISHED_BY]->(b)",
               isbn=book.get("isbn", ""),
               name=publisher)
        print(f"Creating relationship between {book.get('title', '')} and {publisher}")
    
# Create relationships between books and topics
def create_relationships_topic(tx, book):
    for topic in book.get("topics_payload", []):
        tx.run("MATCH (a:Book {isbn: $isbn}) "
               "MATCH (b:Topic {name: $name}) "
               "MERGE (a)-[:TAGGED_WITH]->(b)",
               isbn=book.get("isbn", ""),
               name=topic)
        print(f"Creating relationship between {book.get('title', '')} and {topic}")

with driver.session() as session:
    for book in data:
        try:
            session.execute_write(merge_book, book)
            for author in book.get("authors", []):
                session.execute_write(merge_author, author)
            for publisher in book.get("publishers", []):
                session.execute_write(merge_publisher, publisher)
            for topic in book.get("topics_payload", []):
                print(topic)
                session.execute_write(merge_topic, topic)
            session.execute_write(create_relationships_book, book)
            session.execute_write(create_relationships_publisher, book)
            session.execute_write(create_relationships_topic, book)
        except Exception as e:
            print(e)
            print(f"Error adding {book.get('title', '')} to the database.")

# Close the driver
driver.close()

