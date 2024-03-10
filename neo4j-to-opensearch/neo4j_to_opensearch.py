import os

from opensearchpy import OpenSearch
from neo4j import GraphDatabase
from dotenv import load_dotenv


load_dotenv()

# Initiate the connection to OpenSearch
opensearch_host = os.getenv("OPENSEARCH_HOST")
opensearch_port = os.getenv("OPENSEARCH_PORT")
opensearch_auth = (os.getenv("OPENSEARCH_USERNAME"), os.getenv("OPENSEARCH_PASSWORD"))

client = OpenSearch(
    hosts=[{'host': opensearch_host, 'port': opensearch_port}],
    http_compress=True,
    http_auth=opensearch_auth,
    use_ssl=True,
    verify_certs=True,
    ssl_assert_hostname=False,
    ssl_show_warn=True
)

# Initiate the connection to Neo4j
uri = os.getenv('NEO4J_HOST') or ''
auth = (os.getenv('NEO4J_USERNAME'), os.getenv('NEO4J_PASSWORD'))
driver = GraphDatabase.driver(uri, auth=auth)

# Get data from Neo4j and index it into OpenSearch
with driver.session() as session:
    pass
