# 1. Imprime "Hola, mundo"
print( "Hola, mundo" )

# 2. Imprime "Hola, Angelo" con el nombre en una variable
nombre = "Angelo"
print( "Hola,", nombre ) # con una coma
print( "Hola, " + nombre ) # con un +

# 3. Imprimir "Hola 2025!" con el número en una variable
numero = 2025
print( "Hola", numero, "!" ) # con una coma
# print( "Hola " + numero + "!" ) # Esto arrojaría un error!
print( "Hola " + str(numero) + "!" ) # con un + -- corregido con conversión

# 4. Imprimir "Me encanta comer pan con paltas" con las comidas en variables
comida1 = "pan"
comida2 = "paltas"
print( "Me encanta comer {} con {}".format(comida1, comida2) ) # con .format()
print( f"Me encanta comer {comida1} con {comida2}" ) # con una cadena f

# Ejemplo de BONUS NINJA: Otros métodos de cadena
cadena_ejemplo = "hola mundo python"

print(cadena_ejemplo.upper()) # Convierte a mayúsculas: HOLA MUNDO PYTHON
print(cadena_ejemplo.capitalize()) # Pone en mayúscula la primera letra: Hola mundo python
print(cadena_ejemplo.title()) # Pone en mayúscula la primera letra de cada palabra: Hola Mundo Python
print(cadena_ejemplo.replace("python", "programa")) # Reemplaza una subcadena: hola mundo programacion
print("  espacios  ".strip()) # Elimina espacios en blanco al principio y al final: "espacios"
print(cadena_ejemplo.find("python")) # Devuelve el índice de la primera ocurrencia: 11 (la 'p' de mundo está en la posición 11)