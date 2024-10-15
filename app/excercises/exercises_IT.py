# Invertir palabras en una oración sin invertir
#  las letras de cada palabra.

#     Enunciado: Dada una cadena de caracteres,
#  invierte las palabras sin modificar el orden
#  de las letras dentro de cada palabra.
#     Ejemplo: Entrada: "Hola mundo" -> Salida: "mundo Hola"


def invertir_palabras(palabras):
    # palabras=palabras[::-1]
    invertidas = ""
    for letra in palabras:
        invertidas = letra + invertidas
    return invertidas


# print(invertir_palabras("Hola Mundo"))

# Palindromo
# Enunciado: Verifica si una cadena es la misma al
#  leerla al derecho y al revés, ignorando espacios y mayúsculas.
# Ejemplo: Entrada: "Anita lava la tina" -> Salida: True


def palindromo(palabra):
    inversa = invertir_palabras(palabra).lower().replace(" ", "")
    palabra = palabra.replace(" ", "").lower()
    print(inversa, palabra)
    if inversa == palabra:
        return True
    else:
        return False


# print(palindromo("Anita lava la tina"))


# Eliminar caracteres duplicados consecutivos.
#     Enunciado: Dada una cadena, elimina todos
#  los caracteres duplicados consecutivos.
#     Ejemplo: Entrada: "aabbccdde" -> Salida: "abcde"
def eliminar_duplicados(string):
    caracteres = []
    for valor in string:
        if valor not in caracteres:
            caracteres.append(valor)

    return "".join(caracteres)


# print(eliminar_duplicados("aabbccdde"))


def eliminar_duplicados_indices(string):
    caracteres = [string[0]]
    for valor in string[1:]:
        if valor != caracteres[-1]:
            caracteres.append(valor)

    return "".join(caracteres)


# print(eliminar_duplicados_indices("aabbccdde"))


def eliminar_dup_mi_indices(cadena):
    caracteres = cadena[0]
    for i in range(1, len(cadena)):
        if cadena[i] not in caracteres:
            caracteres += cadena[i]
    return caracteres


# print(eliminar_dup_mi_indices("aabbccdde"))

# Contar vocales y consonantes en una cadena.

#     Enunciado: Dada una cadena, cuenta cuántas
#  vocales y cuántas consonantes contiene.
#     Ejemplo: Entrada: "Hola" ->
# Salida: Vocales: 2, Consonantes: 2


def count_vowels_consonats(string):
    vowels_dict = ["a", "e", "i", "o", "u"]
    diccionario = {"vowels": 0, "consonants": 0}
    for valor in string:
        if valor in vowels_dict:
            diccionario["vowels"] += 1
        else:
            diccionario["consonants"] += 1
    return diccionario


# print(count_vowels_consonats("Hola"))

# Reemplazar un carácter específico en una cadena.

#     Enunciado: Dada una cadena y un carácter,
#  reemplaza todas las apariciones del carácter por un símbolo #.
#     Ejemplo: Entrada: "banana", "a" -> Salida: "b#n#n#"


def remplace_char(character, dato):
    character = character.replace("a", dato)
    return character


# print(remplace_char("banana","#"))

# Buscar el primer carácter no repetido en una cadena.

#     Enunciado: Encuentra el primer carácter
#  en una cadena que no se repita.
#     Ejemplo: Entrada: "abacabad" -> Salida: "c"


def caracter_no_repeditodo(cadena):
    palabras = {}
    for dato in cadena:
        if dato in palabras:
            palabras[dato] += 1
        else:
            palabras[dato] = 1
    for dato in cadena:
        if palabras[dato] == 1:
            return dato

    return "no existe"


# print(caracter_no_repeditodo("abacabad"))

# Convertir una cadena a camelCase.


#     Enunciado: Convierte una cadena con
#  palabras separadas por espacios o guiones
#  bajos a formato camelCase.
#     Ejemplo: Entrada:
#  "mi_nombre_es_carlos" -> Salida: "miNombreEsCarlos"
def change_capital_letter(string):
    palabras = string.replace("_", " ").split()
    camel_case = palabras[0].lower()
    for palabra in palabras[1:]:
        camel_case += palabra.capitalize()

    return camel_case


# print(change_capital_letter("mi_nombre_es_carlos"))

# Expandir una cadena comprimida.

#     Enunciado: Dada una cadena comprimida en la
#  forma a2b3c1, expándela a su forma original.
#     Ejemplo: Entrada: "a2b3c1" -> Salida: "aabbbcc"


def spand_compressed_string(string):
    resultado = ""
    i = 0

    while i < len(string):
        char = string[i]
        i += 1

        numero = ""

        while i < len(string):
            if string[i].isdigit():
                numero += string[i]
                print(numero)
                i += 1

            else:
                break

        resultado += char * int(numero)
        print(char + numero)
    return resultado


# print(spand_compressed_string("a2b3c1"))

# Contar la frecuencia de cada palabra en una oración.

#     Enunciado: Dada una oración,
# cuenta cuántas veces aparece cada palabra.
#     Ejemplo: Entrada: "el gato y el perro"
# -> Salida: {"el": 2, "gato": 1, "y": 1, "perro": 1}


def frecuencia_palabra(palabras):
    palabras = palabras.split()
    diccionartio_palabras = {}
    for palabra in palabras:
        if palabra in diccionartio_palabras:
            diccionartio_palabras[palabra] += 1
        else:
            diccionartio_palabras[palabra] = 1

    return diccionartio_palabras


# print(frecuencia_palabra("el gato y el perro"))

from collections import Counter


def frecuencia__palabras(palabras):

    return dict(Counter(palabras.split()))


# print(frecuencia__palabras("el gato y el perro"))

# Eliminar duplicados de una lista sin usar set().

#     Enunciado: Dada una lista, elimina los
#  elementos duplicados manteniendo el orden de aparición.
#     Ejemplo: Entrada: [1, 2, 2, 3, 4, 4]
# -> Salida: [1, 2, 3, 4]


def delete_duplicados(lista):
    result = []
    for valor in lista:
        if valor not in result:
            result.append(valor)
    return result


# print(delete_duplicados([1,2,2,3,4,4]))

# Rotar una lista hacia la derecha.

#     Enunciado: Dada una lista, rota sus
# elementos k posiciones hacia la derecha.
#     Ejemplo: Entrada: [1, 2, 3, 4, 5], 2
# -> Salida: [4, 5, 1, 2, 3]


def invertir_lista(lista, objetivo):
    if len(lista) < 2:
        return lista
    dos_ultimos = lista[-objetivo:]
    resultado = dos_ultimos + lista[:-objetivo]
    return resultado


# print(invertir_lista([1,2,3,4,5],2))


def invertir_2_ultimos(lista, objetivo):
    for i in range(objetivo):
        ultimo = lista.pop()
        lista.insert(0, ultimo)  # insert no devuelve el nuevo estado de la lista
    resultado = lista
    return resultado


# print(invertir_2_ultimos([1, 2, 3, 4, 5], 2))

# Dividir una lista en n partes iguales.

#     Enunciado: Dada una lista, divídela
#     en n partes iguales. Si no se puede
#     dividir exactamente, la última parte debe ser más corta.
#     Ejemplo: Entrada: [1, 2, 3, 4, 5, 6, 7, 8], 3
#     -> Salida: [[1, 2, 3], [4, 5, 6], [7, 8]]


def dividir_partes_iguales(lista, divisor):
    tam = len(lista) // divisor  # parte entera
    resto = len(lista) % divisor  # modulo

    partes = []
    indice = 0

    for i in range(divisor):
        if i < resto:
            partes.append(lista[indice : indice + tam + 1])
            indice += tam + 1
        else:
            partes.append(lista[indice : indice + tam + 1])
            indice += tam

    return partes


# print(dividir_partes_iguales([1, 2, 3, 4, 5, 6, 7, 8], 3))

# Encontrar la intersección de dos listas.

#     Enunciado: Dadas dos listas, encuentra los elementos comunes entre ambas.
#     Ejemplo: Entrada: [1, 2, 3], [2, 3, 4] -> Salida: [2, 3]


def interseccion_lista(lista1,lista2):
    interseccion=[]
    for dato in lista1:
        if dato in lista2:
            interseccion.append(dato)
    return interseccion

print(interseccion_lista([1,2,3],[2,3,4]))