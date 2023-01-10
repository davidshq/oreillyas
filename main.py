import requests
import os.path
import json
from get_num_of_items import get_num_of_items

"""
Little baby version of Python script that grabs a list of books available from O'Reilly Learning.

It works but not best practices.
"""


start_page = 0
current_page = start_page
# Get the total number of items available for our query from the O'Reilly Search API.
end_page = 2 # int(get_num_of_items() / 200)

# Initialize a list we'll store all the item data in.
items = []

while current_page is not end_page + 1:
    # The API call we'll be making
    url = 'https://learning.oreilly.com/api/v2/search/?query=*&formats=book&limit=10&highlight=0&exclude_fields' \
      '=archive_id&exclude_fields=has_assessment&exclude_fields=chapter_title'

    # Make the call, store reply from API in response.
    response = requests.get(url)

    # Store only the JSON portion of the response
    json_response = response.json()

    # We only need results portion of the JSON
    json_items = json_response['results']

    # Add each book to our list
    for item in json_items:
        items.append(item)

    # So we can see progress
    current_page += 1
    print(f'Current Page: {current_page}')

# Write the list to a file as JSON.
file = "oreilly.json"
with open(os.path.join(file), 'a+', encoding='utf-8', errors="replace") as outfile:
    json.dump(items, outfile, indent=2)
