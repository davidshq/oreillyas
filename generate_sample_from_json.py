# Extract the first four hundred records from oreilly-pid.json and copy them into a new file called oreilly_sample.json

import json

with open('oreilly-pid.json') as f:
    records = json.load(f)

with open('oreilly_sample.json', 'w') as f:
    json.dump(records[:400], f, indent=2)
