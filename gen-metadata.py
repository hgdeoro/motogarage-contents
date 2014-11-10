#!/usr/bin/python

import copy
import json
import sys

def main():
	full_datos = {
		'forums': [
			{
				'id': 1,
				'country': 'ar',
				'name': 'ClubNX4 - Argentina',
				'url': 'www.foronx4.com.ar',
				'vehicles': [
					{
						'id': 1,
						'name': 'Honda Falcon NX4',
						'spec': [
							{'name': 'Aceite - Tipo',				'value': 'Mineral - SAE 20W-50',},
							{'name': 'Aceite - Capacidad maxima',	'value': '2,2 litros',},
							{'name': 'Aceite - Marcas',				'value': 'Mobil Supermoto 4T Multigrado SAE 20W50 API-SF, Castrol Actevo 20W50',},
						],
						'mpt': [
							{'code': 'cambio-aceite',			'name': 'Cambio de aceite',				'km': 3000,},
							{'code': 'cambio-filtro-aceite',	'name': 'Cambio de filtro de aceite',	'km': 3000,},
						],
					},
				],
				'mobile_msg': [
				],
				'image_url': '',
			},
			{
				'id': 2,
				'country': 'ar',
				'name': 'Los Cuises - Moteros Cordobeses',
				'url': 'moteroscordobeses.com.ar',
				'vehicles': [
					{
						'id': 2,
						'name': 'Honda Falcon NX4',
						'spec': [
							{'name': 'Aceite - Tipo',				'value': 'Mineral - SAE 20W-50',},
							{'name': 'Aceite - Capacidad maxima',	'value': '2,2 litros',},
							{'name': 'Aceite - Marcas',				'value': 'Mobil Supermoto 4T Multigrado SAE 20W50 API-SF, Castrol Actevo 20W50',},
						],
						'mpt': [
							{'code': 'cambio-aceite',			'name': 'Cambio de aceite',				'km': 3000,},
							{'code': 'cambio-filtro-aceite',	'name': 'Cambio de filtro de aceite',	'km': 3000,},
						],
					},
				],
				'mobile_msg': [
				],
				'image_url': '',
			},
		]
	}

	indent = 2

	# METADATA
	metadata = copy.deepcopy(full_datos)
	for forum in metadata['forums']:
		del forum['mobile_msg']
		del forum['image_url']
		for vehicle in forum['vehicles']:
			del vehicle['spec']
			del vehicle['mpt']
	with open("metadata.json", "w") as metadata_file:
		metadata_file.write(json.dumps(metadata, encoding='utf-8', indent=indent))

	# FORUMS
	for forum in full_datos['forums']:
		with open("forum_{0}.json".format(forum["id"]), "w") as forum_file:
			forum_file.write(json.dumps(forum, encoding='utf-8', indent=indent))

if __name__ == '__main__':
	main()
