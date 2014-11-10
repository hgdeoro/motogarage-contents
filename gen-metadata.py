#!/bin/bash

import copy
import json
import sys

def main():
	full_datos = {
		'forums': [
			{
				'country': 'ar',
				'name': 'ClubNX4 - Argentina',
				'url': 'www.foronx4.com.ar',
				'vehicles': [
					{
						'code': 'moto.honda.nx4',
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
	
	if sys.argv[1] == 'meta':
		metadata = copy.deepcopy(full_datos)
		for forum in metadata['forums']:
			del forum['mobile_msg']
			del forum['image_url']
			for vehicle in forum['vehicles']:
				del vehicle['spec']
				del vehicle['mpt']
		print(json.dumps(metadata))
		return
	else:
		raise("No implementado")

if __name__ == '__main__':
	main()
