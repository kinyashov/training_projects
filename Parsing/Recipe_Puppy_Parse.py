import urllib.request
import json
import html.parser


i = input("Enter ingredients (separated by commas): ").replace(' ', '')

if i != '':
    URL = "http://www.recipepuppy.com/api/?i={}".format(i)
    with urllib.request.urlopen(URL) as url:
        data = url.read().decode()
    data = html.unescape(data)
    data = json.loads(data)
    for result in data['results']:
        print(' '.join(result['title'].split()))
else:
    print('Not entered ingredients')
