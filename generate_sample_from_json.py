# Extract the first ten records from oreilly-pid.json and copy them into a new file called oreilly_sample.json

import json

with open('oreilly-pid.json') as f:
    records = json.load(f)

with open('oreilly_sample.json', 'w') as f:
    json.dump(records[:10], f, indent=2)
