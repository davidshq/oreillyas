# Load the data from oreilly_sample.json into a variable called records.

import json

with open('oreilly_sample.json') as f:
    records = json.load(f)

    # Create a schema of all the fields that are of type object or array

    schema = {}

    for record in records:
        for key, value in record.items():
            if isinstance(value, dict):
                schema[key] = 'object'
            elif isinstance(value, list):
                schema[key] = 'array'

    # Print the schema
    
    print(schema)