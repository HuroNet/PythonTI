def invertir_cadena(cadena):
    # cadena = cadena[::-1]
    cadena_inve = ""
    for caracter in cadena:
        cadena_inve = caracter + cadena_inve
    return cadena_inve


# print(invertir_cadena('Hola mi nombre es Carlos'))


def suma_numeros(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


# print(suma_numeros([1,23,4,5]))


# Números únicos en una lista

#     Descripción: Dado un array de números,
# escribe una función que devuelva una nueva
# # lista que contenga solo los números únicos.
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 3, 5]


def num_unicos(lista):
    numeros = {}
    for num in lista:
        if num in numeros:
            numeros[num] += 1
        else:
            numeros[num] = 1
    print("los numeros de la lista", numeros)
    unicos = [clave for clave, valor in numeros.items() if valor == 1]
    # unicos = []
    # for num in lista:
    #     count = lista.count(num)
    #     # add some variables

    #     if count == 1:
    #         unicos.append(num)

    return unicos


# print(num_unicos([1, 2, 2, 3, 4, 4, 5, 8, 8, 2, 3, 4, 1, 1, 7]))


# Contar vocales y consonantes: Escribe una función que cuente el
# número de vocales y consonantes en una cadena.
def count_letters(palabra):
    diccionario = {"vocales": 0, "consonantes": 0}
    vocales = ["a", "e", "i", "o", "u"]
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    palabra = palabra.lower()

    for letra in palabra:
        if letra in alfabeto:
            if letra in vocales:
                diccionario["vocales"] += 1
            else:
                diccionario["consonantes"] += 1

    return diccionario


# print(count_letters("palindromo"))
# Buscar el segundo número más grande

# #     Descripción: Escribe una función que reciba una lista de
# # números y devuelva el segundo número más grande.


def segundo_grande(lista):
    lista = sorted(lista)

    return lista[-2]


# print(segundo_grande([1, 2, 3, 5, 6, 7, 3, 98]))

# lo mismo pero sin funciones


def seg_grande_x(lista):

    n = len(lista)
    for i in range(0, n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista[-2]


# print(seg_grande_x([1, 3, 4, 3, 4, 23, 45, 5]))

# ahora vamos hacer mediante un ingreso como string


def seg_num_string(*numero):
    lista = sorted(set(numero))

    return lista[-2]


# print(seg_num_string(1,5,5,7,4,3,2,6,5))


# 6. Ordenar una lista de strings por longitud

#     Descripción: Dada una lista de cadenas de
# texto, escribe una función que ordene la lista
# por la longitud de las cadenas, de menor a mayor.
#     Ejemplo:


def order_list_string(string):
    max_string = max(string, key=len)
    return max_string, len(max_string)


# print(order_list_string(["Hola", "Mundo", "a", "Python"]))


def ordenar_mayor(string):
    dicc = {}
    for valor in string:
        dicc[valor] = len(valor)
    maximo = max(dicc, key=len)
    return maximo, len(maximo)


# print(ordenar_mayor(["Hola", "Mundo", "a", "Python"]))

# 7. Contar la frecuencia de palabras en un texto

#     Descripción: Escribe una función que tome un
# texto como entrada y devuelva un diccionario con
# la frecuencia de cada palabra en el texto.
#     Ejemplo:


def frecuencia_palabra(palabras):
    diccionario = {}
    palabras = palabras.replace(",", "")
    palabras = palabras.lower()
    pala = palabras.split(" ")
    for palabra in pala:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario


# print(frecuencia_palabra("hola Hola, mundo, como van hola"))


# Subcadena más larga sin caracteres repetidos
def longest_substraing(cadena):
    inicio = 0
    max_longitud = 0
    caracteres = set()
    for fin in range(len(cadena)):
        while cadena[fin] in caracteres:
            caracteres.remove(cadena[inicio])
            inicio += 1
        caracteres.add(cadena[fin])
        print(caracteres)

        max_longitud = max(max_longitud, fin - inicio + 1)
    return max_longitud


# print(longest_substraing("abcabcbb"))
# 1. Invertir una cadena

#     Descripción: Escribe una función que invierta una cadena.
#     Entrada: "Python"
#     Salida: "nohtyP"


def invertir_cadena(cadena):
    # cadena=cadena[::-1]
    caracteres = []
    for letra in cadena:
        caracteres[letra] = caracteres + caracteres[letra]
    return cadena


# print(invertir_cadena("HolaMundo"))


# Suma de números en una lista

#     Descripción: Suma todos los números en una lista.
#     Entrada: [1, 2, 3, 4]
#     Salida: 10


def suma_de_numeros(lista):
    suma = 0
    for valor in lista:
        suma += valor
    return suma


# print(suma_de_numeros([1,2,3,4]))
