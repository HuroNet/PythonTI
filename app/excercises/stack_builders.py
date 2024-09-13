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


print(seg_grande_x([1, 3, 4, 3, 4, 23, 45, 5]))
