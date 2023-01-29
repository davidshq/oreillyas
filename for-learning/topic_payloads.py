# Saves a list of deduplicated topics to a file
import json
import os.path

fname = 'oreilly-pid.json'
str_data = open(fname).read()
data = json.loads(str_data)
all_topics = set()

# Iterate through the topics_payload and parse out the uuid, slug, name, and score
# and add them to a set, print the set to the display
for book in data:
    for topics_payload in book:
        topics = book.get('topics_payload', '')
        for topic in topics:
            uuid = topic.get('uuid', '')
            slug = topic.get('slug', '')
            name = topic.get('name', '')
            score = topic.get('score', '')
            all_topics.add((uuid, slug, name, score))

file = 'all_topics.txt'
with open(os.path.join(file), 'a+', encoding='utf-8', errors='replace') as outfile:
    outfile.write(str(all_topics))