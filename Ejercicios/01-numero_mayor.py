# Programa que pida dos numeros por teclado, se devolvera el numero mas alto de los dos introducidos

print('Número mayor')

numero1 = int(input('Ingresa el primer número: '))
numero2 = int(input('Ingresa el segundo número: '))

def devuelveMax(numero1, numero2):
	if numero1 > numero2:
		print('El número ' + str(numero1) + ' es mayor')
	elif numero2 > numero1:
		print('El número ' + str(numero2) + ' es mayor')
	else:
		print('Los números son iguales')

devuelveMax( numero1, numero2 )

print('Programa finalizado...')