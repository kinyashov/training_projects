import urllib.request
import json

pokename = input('Pokemon: ')

proxies = {'https': '51.15.202.250:3128'}
headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokename)

req = urllib.request.Request(url, headers=headers)
proxy = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)

try:
    with urllib.request.urlopen(req) as url:
        response = url.read().decode()
    response = json.loads(response)

    abilities = []
    for ab in response['abilities']:
        if not ab['is_hidden']:
            abilities.append(ab['ability']['name'])

    hidden_abilities = []
    for ab in response['abilities']:
        if ab['is_hidden']:
            hidden_abilities.append(ab['ability']['name'])

    print('id: {}'.format(response['id']),
          '\nweight: {}'.format(response['weight']),
          '\nheight: {}'.format(response['height']),
          '\nbase experience: {}'.format(response['base_experience']),
          '\nabilities: {}'.format(', '.join(abilities)),
          '\nhidden abilities: {}'.format(', '.join(hidden_abilities)))

except urllib.error.HTTPError:
    print('Pokemon not found')
