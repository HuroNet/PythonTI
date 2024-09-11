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
    # unicos= [valor for valor, clave in numeros.items() if clave == 1 ]
    unicos = []
    for num in lista:
        count = lista.count(num)
        # add some variables

        if count == 1:
            unicos.append(num)

    return unicos


print(num_unicos([1, 2, 2, 3, 4, 4, 5, 8, 8, 2, 3, 4]))


# Contar vocales y consonantes: Escribe una función que cuente el
# número de vocales y consonantes en una cadena.

# def count_letters(palabra):
#     count=0
#     for letra in palabra:
#         count += letra
#     return count

# print(count_letters("palindromo"))

#  Crear un diccionario con la longitud de palabras como valores:

# Puedes crear un diccionario donde las claves sean palabras y
# los valores la longitud de cada palabra.
