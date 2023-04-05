import sys
import requests
import json

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()

for i in o["results"]:
    print(i["trackName"])