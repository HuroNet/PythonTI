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


# print(inversa("[1,3,4,56,6]"))


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

# Definir una función generar_n_caracteres() que tome un entero
# n y devuelva el caracter multiplicado por n.
# Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx"


def generar_caracteres(m, n):
    for i in range(0, m + 1):
        caracteres = i * n
        print("los caracteres son:", caracteres)
    return caracteres


# print(generar_caracteres(5, "x"))


# ----------------------------------------
# Definir una función que calcule la longitud de una lista o una cadena dada.\
#  (Es cierto que python tiene la función len()  incorporada, pero escribirla
#  por nosotros mismos resulta un muy buen ejercicio.
def longitud(dato):
    long = 0
    for i in dato:
        long += 1
    return long


# print(longitud([1,2,3,5,4]))
# print(longitud("Hola mundo "))
# new excercise
# inversa de un numero
def inversa2(cadena):
    index = -1
<<<<<<< HEAD


##inversa de una cadena


def string_inverse(lista):
    inicio = 0
    fin = len(lista) - 1
    print(fin)
    while inicio < fin:
        lista[inicio], lista[fin] = lista[fin], lista[inicio]
        inicio = inicio + 1
        fin = fin - 1
    return lista


# print(string_inverse([1,2,43,9,73]))


# con el bucle for cambio


def string_for(lista):
    inicio = 0
    fin = len(lista) - 1
    for _ in range(len(lista) // 2):
        lista[inicio], lista[fin] = lista[fin], lista[inicio]
        inicio += 1
        fin -= 1
    return lista
=======
>>>>>>> main


##inversa de una cadena


<<<<<<< HEAD
# print(fun_sum([1,3,5]))
=======
def string_inverse(lista):
    inicio = 0
    fin = len(lista) - 1
    print(fin)
    while inicio < fin:
        lista[inicio], lista[fin] = lista[fin], lista[inicio]
        inicio = inicio + 1
        fin = fin - 1
    return lista


# print(string_inverse([1,2,43,9,73]))


# con el bucle for cambio


def string_for(lista):
    inicio = 0
    fin = len(lista) - 1
    for _ in range(len(lista) // 2):
        lista[inicio], lista[fin] = lista[fin], lista[inicio]
        inicio += 1
        fin -= 1
    return lista


#Esto es una prueba 
def inversaLista(lista):
    inicio=0
    fin = longitud(lista)-1
    for valor in range(longitud(lista)//2):
        lista[inicio]=lista[fin]
        inicio +=1
        fin -= 1
    return lista
print(inversaLista([1,2,3,4,5]))
>>>>>>> main
