# Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que
# decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

palabra1 = input('Ingrese la primera palabra: ')
palabra2 = input('Ingrese la segunda palabra: ')

if palabra1[-3:] == palabra2[-3:]:
    print(f"{palabra1} y {palabra2} riman")
elif palabra1[-2:] == palabra2[-2:]:
    print(f"{palabra1} y {palabra2} riman un poco")
else:
    print(f"{palabra1} y {palabra2} no riman")
