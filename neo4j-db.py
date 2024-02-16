# Instead of ending up with a JSON file and a SQLite database, this alternative
# allows us to import the data into a Neo4j database.

import os

import requests
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

URI = os.getenv('NEO4J_URI')
AUTH = (os.getenv('NEO4J_USERNAME'), os.getenv('NEO4J_PASSWORD'))

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()