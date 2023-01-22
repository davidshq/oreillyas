import requests
import os
import os.path
import json
from time import sleep
from dotenv import load_dotenv
from get_num_of_items import get_num_of_items

"""
Little baby version of Python script that grabs a list of books available from O'Reilly Learning.

It works but not best practices.
"""

# Load the API key from .env file
load_dotenv()
OREILLY_API_KEY = os.getenv('OREILLY_API_KEY')

start_page = 0
current_page = start_page
# Get the total number of items available for our query from the O'Reilly Search API.
end_page = int(get_num_of_items() / 200) # Use 1 for testing, don't hammer the API

# Initialize a list we'll store all the item data in.
items = []

per_page = 200 # Use 5 for testing
highlight = 0

# Provide a list of fields you want the API NOT TO return.
exclude_fields = [
    'academic_excluded',
    'archive_id',
    'chapter_title',
    'duration_seconds',
    'has_assessment',
    'source']

# Create a string of query params using the exclude fields above
exclude_field_string = ''
for field in exclude_fields:
    exclude_field_string += f'&exclude_fields={field}'

# Our initial API call 
url = f'https://learning.oreilly.com/api/v2/search/?query=*&formats=book&limit={per_page}&highlight={highlight}&{exclude_field_string}' # &page={current_page}

# Add the API key to the header
header = {
    'Authorization': 'Token {}'.format(OREILLY_API_KEY),
}

while current_page is not end_page + 1:
    # Make the call, store reply from API in response.
    response = requests.get(url, headers=header)

    # Store only the JSON portion of the response
    json_response = response.json()

    # Get the next url to pull
    next_url = json_response['next']
    print(next_url)
    if next_url is None:
        print("No more pages to pull.")
        break

    # We only need results portion of the JSON
    json_items = json_response['results']

    # Add each book to our list
    for item in json_items:
        items.append(item)

    # So we can see progress
    current_page += 1
    print(f'Current Page: {current_page}')

    # Update URL for next call
    url = next_url

    # Don't hammer the API
    sleep(1)

# Write the list to a file as JSON.
file = "oreilly.json"
with open(os.path.join(file), 'a+', encoding='utf-8', errors="replace") as outfile:
    json.dump(items, outfile, indent=2)
