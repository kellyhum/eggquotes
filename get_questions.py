import requests
import json

response = requests.get('https://type.fit/api/quotes')

# output formatted json to new data.json file
with open('data.json', 'w', encoding='utf-8') as d:
    json.dump(response.json(), d, indent=4)