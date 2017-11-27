import urllib.request
import json

try:
    with open('pokename_for_test', 'r') as test_file:
        pokename = test_file.readline()
except FileNotFoundError:
    pokename = input('Pokemon: ')

# not working without headers and proxies
proxies = {'https': '51.15.202.250:3128'}
headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokename)

req = urllib.request.Request(url, headers=headers)
proxy = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)

try:
    with urllib.request.urlopen(req) as file:
        response = file.read().decode()
    response = json.loads(response)

    abilities = []
    hidden_abilities = []
    for ab in response['abilities']:
        if ab['is_hidden']:
            hidden_abilities.append(ab['ability']['name'])
        else:
            abilities.append(ab['ability']['name'])

    with open('output', 'w') as output_file:
        print('pokemon: {}'.format(pokename),
              '\nid: {}'.format(response['id']),
              '\nheight: {}'.format(response['height']),
              '\nweight: {}'.format(response['weight']),
              '\nbase experience: {}'.format(response['base_experience']),
              '\nabilities: {}'.format(', '.join(abilities)),
              '\nhidden abilities: {}'.format(', '.join(hidden_abilities)),
              file=output_file)

except urllib.error.HTTPError:
    print('Pokemon not found')
