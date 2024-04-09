# basic excersises
# Name: Carlos Paredes
# email:carlos.paredes23@hotmail.com


# Escribir una función que tome un carácter y devuelva True si es una vocal,
# de lo contrario devuelve False.
def verificar_vocal(leter):
    vocales = ["a", "e", "i", "o", "u"]
    leter = leter.lower()
    if leter in vocales:
        return True
    else:
        return False


# Definir una función inversa() que calcule la inversión de una cadena.
# Por ejemplo la cadena "estoy probando" debería
#  devolver la cadena "odnaborp yotse"


def inversa(cadena):
    # palabra=cadena[::-1] ##este es el primer metodo
    cadena_invertida = ""
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida


# print(inversa("estoy probando"))


# Escribir una función sum() y una función multip() que sumen y
# multipliquen respectivamente todos los números de una lista.
# Por ejemplo: sum([1,2,3,4]) debería devolver 10 y
# multip([1,2,3,4]) debería devolver 24.


def sum(a):
    suma = 0
    for i in a:
        suma = suma + i
    return suma


def multi(b):
    multi = 1
    for i in b:
        multi *= i
    return multi


# print(sum([1,2,3,4]))
# print(multi([1,2,3,4]))


# Definir una función generar_n_caracteres() que tome un entero
#  n y devuelva el caracter multiplicado por n.
# Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx"
def generar_n_caracteres(entero, caracter):
    for i in range(1, entero + 1):
        caracteres = i * caracter
    return caracteres


# print(generar_n_caracteres(5, "x"))
