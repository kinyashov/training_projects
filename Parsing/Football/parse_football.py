import urllib.request
import json


try:
    with open('api_token', 'r') as api_token:
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

        count_team = 5  # number of team in request
        print('\n{}\n{:<4}{:<15}{}'.format(data['leagueCaption'], 'Pos', 'Team', 'Goals'),
              file=output_file)
        for pos, row in enumerate(teams, 1):
            if pos <= count_team:
                print('{:<4}{:<15}{}'.format(str(pos) + '.', row['team'], row['goals']),
                      file=output_file)
