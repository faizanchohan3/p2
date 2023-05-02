from urllib.request import urlopen

import json

url="https://dummyjson.com/posts"
response=urlopen(url)

jsonobj=json.loads(response.read())
test=jsonobj['posts']

for a in test:
    print(a['title'])