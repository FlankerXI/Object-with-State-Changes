import os
import json


# Opening JSON file
f = open('data/seen.json')

# returns JSON object as
# a dictionary
data = json.load(f)
for item in data['results']:
    with open('seen_lines.json', 'a+', encoding='utf-8') as f:
        line = json.dumps(item, ensure_ascii=False)
        f.write(line + '\n')