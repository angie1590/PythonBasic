# Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:
#
# • Imprima los dos primeros caracteres.
#
# • Imprima los tres últimos caracteres.
#
# • Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca
#
# • Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh
#
# • Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.
cadena = "Te quiero solo como amigo"
print(f"Los dos primeros caracteres: {cadena[0:2]}")
print(f"Tres últimos caracteres: {cadena[-3:]}")
print(f"Cada dos caracteres: {cadena[ : : 2]}")
print(f"Cadena inversa: {cadena[: : -1]}")
print(f"Cadena en un sentido y luego en inverso: {cadena}{cadena[: : -1]}")

