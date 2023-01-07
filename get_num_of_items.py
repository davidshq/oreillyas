import requests


def get_num_of_items():
    """Get the total number of items available from the O'Reilly Search API."""
    url = 'https://learning.oreilly.com/api/v2/search/?query=*&formats=book&limit=200&highlight=0&exclude_fields' \
        '=archive_id&exclude_fields=has_assessment&exclude_fields=chapter_title'
    response = requests.get(url)
    json_results = response.json()
    num_results = json_results['total']
    print(num_results)
    return num_results