# basic excersises
# Name: Carlos Paredes
# email:carlos.paredes23@hotmail.com


# from app.excercises.delete import delete
# from app.excercises.delete import delete


def verificar_si_es_vocal(leter):
    vocales = ["a", "e", "i", "o", "u"]
    leter = leter.lower()
    if leter in vocales:
        return True
    else:
        return False


def inversa_de_una_cadena(cadena):
    # palabra=cadena[::-1] ##este es el primer metodo
    cadena_invertida = ""
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida


# print(inversa("[1,3,4,56,6]"))


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


# con el bucle for cambio new change
def string_for(lista):
    inicio = 0
    fin = len(lista) - 1
    for _ in range(len(lista) // 2):
        lista[inicio], lista[fin] = lista[fin], lista[inicio]
        inicio += 1
        fin -= 1
    return lista


# -------------------------------------
# convertir cadena de numeros a list
def stringToList(cadena):
    lista = []
    numeros = cadena.split(",")
    for numero in numeros:
        print(numero)
        numero_entero = int(numero)
        lista.append(numero_entero)
    return lista


# print(stringToList("1,2,3,4,5"))

# forma mas sencilla de hacer un cambio de
# numero en cadena a lista
# ejercico de entrevista


def cadena_a_lista(cadena):
    numeros = cadena.split(",")
    lista = [int(numero) for numero in numeros]
    return lista


# print(cadenaALista("1,34,4,5,3,3"))


def superposition(lista1, lista2):
    for valor in lista1:
        print(valor)
        if valor in lista2:
            return True

    return False


# print(superposition([1, 2, 3, 4], [5, 6, 2, 4]))
# print(superposition([1, 2, 3, 4], [5, 6, 2, 4]))

# delete.py


# Subcadena más larga sin caracteres repetidos
def longest_substraing(cadena):
    charset = set()  # actualizar la lista -- se crea un diccionario
    longitud = 0  # calculo  de la longitud
    left = 0
    for right in range(0, len(cadena)):
        while cadena[right] in charset:
            charset.remove(cadena[left])
            left += 1
        charset.add(cadena[right])
        longitud = max(longitud, right - left + 1)

    return longitud


# print(longest_substraing("abcdabca"))


# another fuction
def cadena_larga(cadena):
    longitud_cadena = 0
    lista_cadena = list(cadena)
    new_list = []
    for valor in lista_cadena:
        if valor not in new_list:
            new_list.append(valor)
            longitud_cadena += 1
    return longitud_cadena


# print(cadena_larga("abcdabcd"))


# problema de entrevista---
# devolver cuantas evces se repite
text = "Hola mi nombre es Carlos, entonces yo creo que carlos tiene un bonito nombre para decir hola."


def minusculas(text):
    text = text.lower()
    return text


def modificar(text):
    text = text.replace(",", "").replace(".", "")
    text = text.split()
    return text


def repetitions(text):
    palabras = {}
    for palabra in text:
        if palabra in palabras:
            palabras[palabra] += 1
        else:
            palabras[palabra] = 1
    return palabras


def mayores(text):
    repeticiones = repetitions(text)
    max_repeticiones = repeticiones.values()

    return max_repeticiones


print(repetitions(modificar(minusculas(text))))
print(mayores(modificar(minusculas(text))))
print(modificar(minusculas(text)))
