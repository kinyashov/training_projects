import urllib.request
import json
import html.parser

try:
    with open('ingredients_for_test', 'r') as test_file:
        ingredients = test_file.readlines()
except FileNotFoundError:
    ingredients = input("Enter ingredients (separated by commas): ").replace(' ', '')

if ingredients != '':

    URL = "http://www.recipepuppy.com/api/?i={}".format(''.join(ingredients))

    with urllib.request.urlopen(URL) as req:
        data = req.read().decode()
    data = html.unescape(data)
    data = json.loads(data)

    with open('output', 'w') as output_file:
        if len(data['results']) == 0:
            print('Recipes not found', file=output_file)
        else:
            for recipe in data['results']:
                print('{}'.format(' '.join(recipe['title'].split())),
                      file=output_file)

else:
    print('Not entered ingredients')
