import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("You forgot something")

respone = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(json.dumps(respone.json(), indent=2))

o = respone.json()
for result in o["results"]:
    print(result["trackName"])