import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = {'X-Auth-Token': '', 'X-Response-Control': 'minified'}
connection.request('GET', '/v1/competitions', None, headers)
response = json.loads(connection.getresponse().read().decode())

print(response)
