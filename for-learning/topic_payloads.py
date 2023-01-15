import json
import sqlite3

fname = 'oreilly-pid.json'
str_data = open(fname).read()
data = json.loads(str_data)

for book in data:
    for topics_payload in book:
        topics_payload = book.get('topics_payload', '')
        print(topics_payload)

# Iterate through the topics_payload and parse out the uuid, slug, name, and score
# and add them to a set
topics = set()
for book in data:
    for topics_payload in book:
        topics_payload = book.get('topics_payload', '')
        for topic_payload in topics_payload:
            uuid = topic_payload[0]
            slug = topic_payload[1]
            name = topic_payload[2]
            score = topic_payload[3]
            topics.add((uuid, slug, name, score))
print(topics)