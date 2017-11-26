import urllib.request
import json

leagues = [445, 450, 452, 455, 456]
headers = {'X-Auth-Token': '', 'X-Response-Control': 'minified'}
for league in leagues:
    url = 'http://api.football-data.org/v1/competitions/{}/leagueTable'.format(league)
    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as url:
        data = url.read().decode()
    data = json.loads(data)
    teams = sorted(data['standing'], key=lambda x: x['goals'], reverse=True)

    print('\n', data['leagueCaption'])
    print('Pos', 'Team'.ljust(14), 'Goals')
    for pos, row in enumerate(teams, 1):
        if pos < 6:
            print('{}.  {}{}'.format(pos, row['team'].ljust(15), row['goals']))
