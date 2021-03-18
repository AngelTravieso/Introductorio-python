mi_lista = ["Maria", "Angel", "Pedro", "Carlos"]

# Imprimir toda la lista
print(mi_lista[:])

# Imprimir elemento de la lista
print(mi_lista[1])

# Se genera una excepcion si el elemento no existe
# print(mi_lista[6]) #  list index out of range

# Leer el array desde el final, empieza en 1
print(mi_lista[-1])

# Acceder a una porcion de la lista, excluye el 2do numero
print(mi_lista[0:3])

 # al omitir el primer indice, se sobreentiende que es 0
print(mi_lista[:2])

# del indice 2 hasta el final
print(mi_lista[2:])

# agregar elemento al final de la lista
mi_lista.append("Gustavo")

# agregar elemento en un punto intermedio
mi_lista.insert(2, "Sandra")

# agregar varios elementos a una lista
mi_lista.extend(["Ana", "Ivan", "Alejandro"])

# indice de un elemento
print(mi_lista.index("Sandra"))

# Imprime true o false para saber si el elemento esta en la lista
print("Pepe" in mi_lista)

# eliminar elemento de lista
mi_lista.remove("Ana")

# eliminar ultimo elemento de la lista
mi_lista.pop()

# unir dos listas (alternativa a extends)
mi_lista2 = ["Cleo", "Sasha"]
mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)

# repetir lista
print(mi_lista2 * 2)