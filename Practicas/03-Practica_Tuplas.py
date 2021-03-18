mi_tupla = ("Angel", "Gustavo", 2, "Gustavo")

print(mi_tupla)
print(mi_tupla[2])

# convertir tupla en lista
mi_lista = list(mi_tupla)
print(mi_lista)

# convertir lista en tupla
mi_tupla2 = tuple(mi_lista)
print(mi_tupla2)

# Encontrar elemento en tupla, imprime true o false
print("Gustavo" in mi_tupla)

# Averiguar cuantos veces se se encuentran ese elemento en una tupla
print(mi_tupla.count("Gustavo"))

# Cuantos elementos tiene la tupla
print(len(mi_tupla))

# Tuplas unitarias (unico elemento)
tupla_unitaria = ("Angel",)
print(len(tupla_unitaria))

# Tupla sin parentesis (empaquetado de tupla)
mi_tupla3 = "Angel", 2, 433, "Pedro"
print(mi_tupla3)

# desempaquetado de tupla, asigna valores
mi_tupla4 = ("Angel", 1, 24, 1999)
nombre, mes, dia, agno = mi_tupla4

print(nombre)
print(dia)
print(agno)
print(mes)