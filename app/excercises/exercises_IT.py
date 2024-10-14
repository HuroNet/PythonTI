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
    palabras={}
    for dato in cadena:
        if dato in palabras:
            palabras[dato] += 1
        else:
            palabras[dato] = 1
    for dato in cadena:
        if palabras[dato]==1:
            return dato

    return "no existe"

print(caracter_no_repeditodo("abacabad"))