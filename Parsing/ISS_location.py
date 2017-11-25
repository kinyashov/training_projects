import urllib.request
import json


URL = 'http://api.open-notify.org/iss-now.json'

with urllib.request.urlopen(URL) as url:
    data = url.read().decode()

data = json.loads(data)

print(data['iss_position']['latitude'], data['iss_position']['longitude'])
