# Calcular la media aritmetica de 3 numeros ingresados

numero1 = int(input('Ingrese el primer número: '))
numero2 = int(input('Ingrese el segundo número: '))
numero3 = int(input('Ingrese el tercer número: '))

media = round((numero1 + numero2 + numero3) / 3, 2)

print('La media aritmética es: ' + str(media))

print('Programa finalizado...')