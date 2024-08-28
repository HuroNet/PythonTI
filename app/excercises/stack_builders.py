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


def numeros_unicos(lista):
    numeros = {}
    for valor in lista:
        if valor in numeros:
            numeros[valor] += 1
        else:
            numeros[valor] = 1

    unicos = [valor for valor, cantidad in numeros.items() if cantidad == 1]

    return unicos


print(numeros_unicos([1, 2, 3, 3, 4, 1, 5]))
