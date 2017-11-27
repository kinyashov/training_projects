import urllib.request
import json

file = 'api_token'
try:
    with open(file, 'r') as api_token:
        token = api_token.readline()
except FileNotFoundError:
    token = ''

leagues = [445, 450, 452, 455, 456]  # id leagues in database
headers = {'X-Auth-Token': token, 'X-Response-Control': 'minified'}  

with open('output', 'w') as output_file:
    for league in leagues:
        url = 'http://api.football-data.org/v1/competitions/{}/leagueTable'.format(league)
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as url:
            data = url.read().decode()
        data = json.loads(data)
        teams = sorted(data['standing'], key=lambda x: x['goals'], reverse=True)

        print('\n{}'.format(data['leagueCaption']), file=output_file)
        print('{:<4}{:<15}{}'.format('Pos', 'Team', 'Goals'), file=output_file)
        for pos, row in enumerate(teams, 1):
            if pos < 6:
                print('{:<4}{:<15}{}'.format(pos, row['team'], row['goals']), file=output_file)
