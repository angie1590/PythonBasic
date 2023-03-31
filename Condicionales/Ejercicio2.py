# Ejercicio 2
#
# Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su
# valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos,
# su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).

num = int(input('Ingrese un número entero: '))

if num < 0:
    print(f"El valor absoluto es {num} es {abs(num)}")
else:
    print(f"El valor absoluto es {num} es {num}")
