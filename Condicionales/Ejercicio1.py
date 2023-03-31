# Ejercicio 1
#
# Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al
# usuario que no es vocal

letra = input('Ingrese una letra: ')

if letra.lower() in 'aeiou':
    print(f"{letra} es vocal")
else:
    print(f"{letra} no es vocal")