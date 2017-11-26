import urllib.request
import json

file = 'api_token'
try:
    with open(file, 'r') as api_token:
        token = api_token.readline()
except FileNotFoundError:
    token = ''

leagues = [445, 450, 452, 455, 456]
headers = {'X-Auth-Token': token, 'X-Response-Control': 'minified'}

for league in leagues:
    url = 'http://api.football-data.org/v1/competitions/{}/leagueTable'.format(league)
    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as url:
        data = url.read().decode()
    data = json.loads(data)
    teams = sorted(data['standing'], key=lambda x: x['goals'], reverse=True)

    print('\n\x1b[32m{}\x1b[0m'.format(data['leagueCaption']))
    print('\x1b[4m{:<4}{:<15}{}\x1b[0m'.format('Pos', 'Team', 'Goals'))
    for pos, row in enumerate(teams, 1):
        if pos < 6:
            print('{:<4}{:<15}{}'.format(pos, row['team'], row['goals']))
