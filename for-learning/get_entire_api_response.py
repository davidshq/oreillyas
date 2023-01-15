import requests
import os.path
import json

# Initialize a list we'll store all the item data in.
items = []

per_page = 10 # Use 5 for testing

# The API call we'll be making
url = f'https://learning.oreilly.com/api/v2/search/?query=*&formats=book&limit={per_page}'

# Make the call, store reply from API in response.
response = requests.get(url)

# Store only the JSON portion of the response
json_response = response.json()

# Write the list to a file as JSON.
file = "entire_response.json"
with open(os.path.join(file), 'a+', encoding='utf-8', errors="replace") as outfile:
    json.dump(json_response, outfile, indent=2)
