import urllib.request
import json
import format_coord


URL = 'http://api.open-notify.org/iss-now.json'

with urllib.request.urlopen(URL) as url:
    data = url.read().decode()
data = json.loads(data)

dddddd_lat = data['iss_position']['latitude']
dddddd_long = data['iss_position']['longitude']
ddmmss_lat, ddmmss_long = format_coord.ddmmss_format(float(dddddd_lat), float(dddddd_long))

with open('output', 'w') as output_file:
    print('DDDDDD format: {} {}'.format(dddddd_lat, dddddd_long), file=output_file)
    print('DDMMSS format: {} {}'.format(ddmmss_lat, ddmmss_long), file=output_file)
