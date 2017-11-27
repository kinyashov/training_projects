"""Functions for conversion coordinates from DDDDDD format to DDMMSS format"""


def format_coord(a):
    d = int(a)
    m = int((a % 1) * 60)
    s = round((((a % 1) * 60) % 1) * 60, 4)
    if not s % 1:
        s = int(s)
    return d, m, s


def ddmmss_format(lat, long):

    cardinal_direction = 'N' if lat > 0 else 'S'
    d_lat, m_lat, s_lat = format_coord(abs(lat))
    ddmmss_lat = '{}\xB0{}\x27{}\x22{}'.format(d_lat, m_lat, s_lat, cardinal_direction)

    cardinal_direction = 'E' if long > 0 else 'W'
    d_long, m_long, s_long = format_coord(abs(long))
    ddmmss_long = '{}\xB0{}\x27{}\x22{}'.format(d_long, m_long, s_long, cardinal_direction)

    return ddmmss_lat, ddmmss_long