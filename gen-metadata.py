#!/bin/bash

import json

def main():
	metadata = {
		'forums': [
			{
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
	print(json.dumps(metadata))

if __name__ == '__main__':
	main()

