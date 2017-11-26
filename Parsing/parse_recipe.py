import urllib.request
import json
import html.parser


ingredients = input("Enter ingredients (separated by commas): ").replace(' ', '')

if ingredients != '':

    URL = "http://www.recipepuppy.com/api/?i={}".format(ingredients)

    with urllib.request.urlopen(URL) as url:
        data = url.read().decode()
    data = html.unescape(data)
    data = json.loads(data)

    if len(data['results']) == 0:
        print('Recipes not found')
    else:
        for recipe in data['results']:
            print('\x1b[1m{}\x1b[0m: {}'.format(' '.join(recipe['title'].split()),
                                                recipe['ingredients']))

else:
    print('Not entered ingredients')
