# Programa que pida por teclado Nombre, Direccion y Teléfono, los datos deben ser almacenados en una lista y mostrar en consola el mensaje "Los datos personales son"

nombre = input('Ingrese su nombre: ')
direccion = input('Ingrese su dirección: ')
telefono = input('Ingrese su número telefónico: ')

mi_lista = [nombre, direccion, telefono]

print('Los datos personales son: ' + mi_lista[0] + ' ' + mi_lista[1] + ' ' + mi_lista[2])

print('Programa finalizado...')