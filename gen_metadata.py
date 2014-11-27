#!/usr/bin/python
# -*- coding: utf8 -*-
import copy
import json

def check_ids(datos):
	_forum_ids = set()
	_vehicles_ids = set()
	_mpt_ids = set()
	for forum in datos['forums']:
		assert forum['id'] not in _forum_ids, "Forum ID duplicado: " + str(forum['id'])
		_forum_ids.add(forum['id'])
		for vehicle in forum['vehicles']:
			assert vehicle['id'] not in _vehicles_ids, "Vehicle ID duplicado: " + str(vehicle['id'])
			_vehicles_ids.add(vehicle['id'])
			for a_mpt in vehicle['mpt']:
				assert a_mpt['id'] not in _mpt_ids, "Id duplicado: " + str(a_mpt['id'])
				_mpt_ids.add(a_mpt['id'])

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
							{'name': 'Aceite - Tipo', 				'value': 'Mineral - SAE 20W-50', },
							{'name': 'Aceite - Capacidad maxima', 	'value': '2,2 litros', },
							{'name': 'Aceite - Marcas', 			'value': 'Mobil Supermoto 4T Multigrado SAE 20W50 API-SF, Castrol Actevo 20W50', },
						],
						'mpt': [
							{'id': 101, 	'name': 'Cambio de aceite', 			'distance': 3000, },
							{'id': 102, 	'name': 'Cambio de filtro de aceite', 	'distance': 3000, },
							{'id': 103, 	'name': 'Cambio de filtro de aire', 	'distance': 6000, },
							{'id': 104, 	'name': 'Control luz de válvulas', 		'distance': 3000, },
						],
					},
				],
				'forumLinks': [
					{'name': 'Deposito de bienvenida',
						'url': 'http://www.foronx4.com.ar/index.php?topic=4479'},
					{'name': 'Viajes largos, consejos, preparativos',
						'url': 'http://www.foronx4.com.ar/index.php?topic=1520'},
					{'name': 'Kits de emergencia',
						'url': 'http://www.foronx4.com.ar/index.php?topic=3410'},
					{'name': 'Cómo se mide el nivel de aceite',
						'url': 'http://www.foronx4.com.ar/index.php?topic=12'},
				],
				'mobileMessages': [
				],
				'imageUrl': '',
			},
# 			{
# 				'id': 2,
# 				'country': 'ar',
# 				'name': 'Los Cuises - Moteros Cordobeses',
# 				'url': 'moteroscordobeses.com.ar',
# 				'vehicles': [
# 					{
# 						'id': 2,
# 						'name': 'Honda Falcon NX4',
# 						'spec': [
# 							{'name': 'Aceite - Tipo', 				'value': 'Mineral - SAE 20W-50', },
# 							{'name': 'Aceite - Capacidad maxima', 	'value': '2,2 litros', },
# 							{'name': 'Aceite - Marcas', 			'value': 'Mobil Supermoto 4T Multigrado SAE 20W50 API-SF, Castrol Actevo 20W50', },
# 						],
# 						'mpt': [
# 							{'id': 105, 	'name': 'Cambio de aceite', 			'distance': 3000, },
# 							{'id': 106, 	'name': 'Cambio de filtro de aceite', 	'distance': 3000, },
# 							{'id': 107, 	'name': 'Cambio de filtro de aire', 	'distance': 6000, },
# 							{'id': 108, 	'name': 'Control luz de válvulas', 		'distance': 3000, },
# 						],
# 					},
# 				],
# 				'forumLinks': [
# 				],
# 				'mobileMessages': [
# 				],
# 				'imageUrl': '',
# 			},
			{
				'id': 4,
				'country': 'ar',
				'name': 'Club Twister',
				'url': 'www.clubtwister.com.ar',
				'vehicles': [
					{
						'id': 4,
						'name': 'Honda Twister',
						'spec': [
							{'name': 'Aceite - Tipo', 				'value': 'Mineral - SAE 20W-50', },
							{'name': 'Aceite - Capacidad maxima', 	'value': '1,5 litros', },
							{'name': 'Aceite - Marcas', 			'value': 'Mobil Supermoto 4T Multigrado SAE 20W50 API-SF', },
						],
						'mpt': [
							{'id': 113, 	'name': 'Cambio de aceite', 			'distance': 3000, },
							{'id': 114, 	'name': 'Cambio de filtro de aceite', 	'distance': 6000, },
							{'id': 115, 	'name': 'Cambio de filtro de aire', 	'distance': 18000, },
							{'id': 116, 	'name': 'Control luz de válvulas', 		'distance': 3000, },
						],
					},
				],
				'forumLinks': [
					{'name': 'Descargas (manuales, etc.)',
						'url': 'http://www.clubtwister.com.ar/foro/descargas.php'},
					{'name': 'Tutorial cambio de aceite',
						'url': 'http://www.clubtwister.com.ar/foro/viewtopic.php?f=51&t=74'},
				],
				'mobileMessages': [
				],
				'imageUrl': '',
			},
			{
				'id': 3,
				'country': 'ar',
				'name': 'General - Sin foro',
				'url': '',
				'vehicles': [
					{
						'id': 3,
						'name': 'Honda Falcon NX4',
						'spec': [
							{'name': 'Aceite - Tipo', 				'value': 'Mineral - SAE 20W-50', },
							{'name': 'Aceite - Capacidad maxima', 	'value': '2,2 litros', },
							{'name': 'Aceite - Marcas', 			'value': 'Mobil Supermoto 4T Multigrado SAE 20W50 API-SF, Castrol Actevo 20W50', },
						],
						'mpt': [
							{'id': 109, 	'name': 'Cambio de aceite', 			'distance': 3000, },
							{'id': 110, 	'name': 'Cambio de filtro de aceite', 	'distance': 3000, },
							{'id': 111, 	'name': 'Cambio de filtro de aire', 	'distance': 6000, },
							{'id': 112, 	'name': 'Control luz de válvulas', 		'distance': 3000, },
						],
					},
				],
				'forumLinks': [
				],
				'mobileMessages': [
				],
				'imageUrl': '',
			},
		]
	}

	indent = 2

	# CHECK
	check_ids(full_datos)

	# METADATA
	metadata = copy.deepcopy(full_datos)
	for forum in metadata['forums']:
		del forum['forumLinks']
		del forum['mobileMessages']
		del forum['imageUrl']
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
