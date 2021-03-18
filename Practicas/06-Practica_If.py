print('Programa de Evaluación de Notas de Estudiantes')

# Lee el input como string
nota_estudiante = input('Introduce la nota del estudiante: ')

def evaluacion(nota):
	valoracion = 'aprobado'

	if nota < 5:
		valoracion = 'suspenso'
	return valoracion

# int para convertir string a int
print(evaluacion(int(nota_estudiante)))


