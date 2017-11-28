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
yandex_map = 'https://yandex.ru/maps/?mode=whatshere&whatshere%5Bpoint%5D=' \
             '{}%2C{}&whatshere%5Bzoom%5D=NaN'.format(dddddd_long, dddddd_lat)
google_map = 'https://www.google.ru/maps/place/{}+{}/'.format(ddmmss_lat, ddmmss_long)

with open('output', 'w') as output_file:
    print('DDDDDD format: {} {} \
          \nDDMMSS format: {} {} \
          \nYandex Map: {} \
          \nGoogle Map: {}'.format(dddddd_lat, dddddd_long,
                                   ddmmss_lat, ddmmss_long,
                                   yandex_map,
                                   google_map),
          file=output_file)
