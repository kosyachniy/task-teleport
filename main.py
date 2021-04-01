import json

import requests


LINK = 'https://api-dev.tport.online/v3/stations'

with open('keys.json', 'r') as file:
	TOKEN = json.loads(file.read())['token']


# 1. Получить список постаматов с эндпоинта
headers = {'Authorization': 'Token {}'.format(TOKEN)}
res = requests.get(LINK, headers=headers).json()


# 2. Выявить среди полученных постаматы с address_struct.fias_id редко встречающимся в базе (<10 раз)
k = {}

for postamat in res['results']:
	id_ = postamat['id']
	fias_id = postamat['location']['address_struct']['fias_id']

	if fias_id not in k:
		k[fias_id] = {id_}
	else:
		k[fias_id].add(id_)

for postamat in k:
	if len(k[postamat]) < 10:
		print(*k[postamat], sep=' ', end=' ')

print()