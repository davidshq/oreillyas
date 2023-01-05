import requests
import os.path
import json

"""
Little baby version of Python script that grabs a list of books available from O'Reilly Learning.

It works but not best practices.
"""

# result_formats = 'book'
# per_page = '200'
# highlight = 0
# exclude_fields = [
#     'archive_id',
#     'has_assessment',
#     'chapter_title',
#     'content_format',
#     'events'
# ]
# exclude_fields_str = ''
# for field in exclude_fields:
#     exclude_fields_str += '&exclude_fields=' + field


def get_num_of_items():
    """Get the total number of items available from the O'Reilly Search API."""
    url = 'https://learning.oreilly.com/api/v2/search/?query=*&formats=book&limit=200&highlight=0&exclude_fields' \
        '=archive_id&exclude_fields=has_assessment&exclude_fields=chapter_title'
    response = requests.get(url)
    json_results = response.json()
    num_results = json_results['total']
    print(num_results)
    return num_results


current_page = 0
end_page = int(get_num_of_items() / 200)
items = {}

while current_page is not end_page + 1:
    url = 'https://learning.oreilly.com/api/v2/search/?query=*&formats=book&limit=200&highlight=0&exclude_fields' \
      '=archive_id&exclude_fields=has_assessment&exclude_fields=chapter_title'

    # Make the call, story reply from API in response.
    response = requests.get(url)

    # Store only the JSON portion of the response
    json_response = response.json()

    # Store only the items portion of the JSON data
    json_items = json_response['results']

    # Get URL for next page of results
    url = json_response['next']

    # For each JSON object in, add an object to our items dictionary
    for id, item in enumerate(json_items):
        items[id] = item
    current_page += 1
    print(current_page)

# Write the dictionary to a file as JSON.
file = "oreilly.json"
with open(os.path.join(file), 'a+', encoding='utf-8', errors="replace") as outfile:
    json.dump(items, outfile, indent=2)
