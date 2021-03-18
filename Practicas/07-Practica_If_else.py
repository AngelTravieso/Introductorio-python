print('Verificación de acceso')

nota_estudiante = int(input('Introduce tu nota por favor: '))

if nota_estudiante < 5:
	print('Insuficiente')
elif nota_estudiante < 6:
	print('Suficiente')
elif nota_estudiante < 7:
	print('Bien')
elif nota_estudiante < 9:
	print('Notable')
else:
	print('Sobresaliente')

print('Ha finalizado el programa...')