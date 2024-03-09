# Connects to an OpenSearch instance and creates a non-default index: "python-test-index" with 4 shards.
import os

from opensearchpy import OpenSearch
from dotenv import load_dotenv

load_dotenv()

opensearch_host = os.getenv("OPENSEARCH_HOST")
opensearch_port = os.getenv("OPENSEARCH_PORT")
opensearch_auth = (os.getenv("OPENSEARCH_USERNAME"), os.getenv("OPENSEARCH_PASSWORD"))
print(opensearch_host, opensearch_port)

client = OpenSearch(
    hosts = [{'host':opensearch_host, 'port':opensearch_port}],
    http_compress = True,
    http_auth = opensearch_auth,
    use_ssl = True,
    verify_certs = True,
    ssl_assert_hostname = False,
    ssl_show_warn = True
)

# Create an index with non-default settings.
index_name = 'python-test-index'
index_body = {
    'settings': {
        'index': {
           'number_of_shards': 4
        }
    }
}

response = client.indices.create(index=index_name, body=index_body)
print('\nCreating index:')
print(response)
