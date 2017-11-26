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

with urllib.request.urlopen(req) as url:
    response = url.read().decode()
response = json.loads(response)

print('id: {}\nweight: {}\nheight: {}\nbase experience: {}'.format(response['id'],
                                                                   response['weight'],
                                                                   response['height'],
                                                                   response['base_experience']))
