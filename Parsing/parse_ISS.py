import urllib.request
import json


def format_coord(a):
    d = int(a)
    m = int((a % 1) * 60)
    s = round((((a % 1) * 60) % 1) * 60, 4)
    return d, m, s


def google_format(lat, long):

    cardinal_direction = 'N' if lat > 0 else 'S'
    d_lat, m_lat, s_lat = format_coord(abs(lat))
    google_lat = '{}\xB0{}\x27{}\x22{}'.format(d_lat, m_lat, s_lat, cardinal_direction)

    cardinal_direction = 'E' if long > 0 else 'W'
    d_long, m_long, s_long = format_coord(abs(long))
    google_long = '{}\xB0{}\x27{}\x22{}'.format(d_long, m_long, s_long, cardinal_direction)

    return google_lat, google_long


URL = 'http://api.open-notify.org/iss-now.json'

with urllib.request.urlopen(URL) as url:
    data = url.read().decode()
data = json.loads(data)

yandex_lat = data['iss_position']['latitude']
yandex_long = data['iss_position']['longitude']
google_lat, google_long = google_format(float(yandex_lat), float(yandex_long))

print('For Yandex: {} {}'.format(yandex_lat, yandex_long))
print('For Google: {} {}'.format(google_lat, google_long))
