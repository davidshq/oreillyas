# Takes the oreilly.json file and adds a pid field to each book
# Built using GitHub Copilot

import json

# Load the json into Python
fname = '../oreilly-pid.json'
str_data = open(fname).read()
data = json.loads(str_data)

# Add a unique integer pid field to each book in the data list
for (pid, book) in enumerate(data):
    book['pid'] = pid

# Write the data list back to the oreilly.json file
str_data = json.dumps(data)
open(fname, 'w').write(str_data)