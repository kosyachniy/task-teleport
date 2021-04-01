import json

import requests


LINK = 'https://api-dev.tport.online/v3/stations'

with open('keys.json', 'r') as file:
	TOKEN = json.loads(file.read())['token']


headers = {'Authorization': 'Token {}'.format(TOKEN)}
res = requests.get(LINK, headers=headers).text
print(res)