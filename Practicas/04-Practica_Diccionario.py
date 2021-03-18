mi_diccionaro = {
	'Alemania': 'Berlin',
	'Francia': 'Paris',
	'Reino Unido': 'Londres',
	'España': 'Madrid'
}

# Imprimir valor
# print(mi_diccionaro['Francia']);

# Acceder a un diccionario entero
# print(mi_diccionaro);

# Agregar elementos a un diccionario ya construido
mi_diccionaro['Italia'] = 'Lisboa'

# Modificar valor de una clave
mi_diccionaro['Italia'] = 'Roma'

# Eliminar elementos (se elimina el key/value)
del mi_diccionaro['Reino Unido']

# print(mi_diccionaro)

mi_diccionaro2 = {
	'Alemania': 'Berlin',
	23: 'Jordan',
	'Mosqueteros': 3
}

# print(mi_diccionaro2)

# Utilizar tupla para imprimir claves del diccionario
mi_tupla = ['España', 'Francia', 'Reino Unido', 'Alemania']

mi_diccionaro3 = {
	mi_tupla[0]: 'Madrid',
	mi_tupla[1]: 'Paris',
	mi_tupla[2]: 'Londres',
	mi_tupla[3]: 'Berlin'
}

# print(mi_diccionaro3)
# print(mi_diccionaro3['Francia'])

# Que un diccionario almacene una tupla de valores
mi_diccionaro4 = {
	23: 'Jordan',
	'Nombre': 'Michael',
	'Equipo': 'Chicago',
	'Anillos': [1991, 1992, 1993, 1996, 1997, 1998]
}

# print(mi_diccionaro4)
# print(mi_diccionaro4['Equipo'])
# print(mi_diccionaro4['Anillos'])
# print(mi_diccionaro4['Anillos'][2])

# Guardar un diccionario en otro diccionario
mi_diccionaro5 = {
	23: 'Jordan',
	'Nombre': 'Michael',
	'Equipo': 'Chicago',
	'Anillos': {
		'temporadas': [1991, 1992, 1993, 1996, 1997, 1998]
		}
}

# print(mi_diccionaro5['Anillos'])
# print(mi_diccionaro5['Anillos']['temporadas'])

# Imprimir keys del diccionario
print(mi_diccionaro5.keys())

# Imprimir values del diccionario
print(mi_diccionaro5.values())

# Longitud del diccionario
print(len(mi_diccionaro5))