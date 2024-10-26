# Detectar si una cadena es un palíndromo.


#     Enunciado: Verifica si una cadena es la misma
# al leerla al derecho y al revés. Ignora espacios y mayúsculas.
#     Ejemplo: Entrada: "Amo la paloma" -> Salida: True
def palindromo(string):
    original = string.lower().replace(" ", "")
    print("original", original)
    invertida = string[::-1].lower().replace(" ", "")
    print("inver", invertida)

    # for i in range(len(string)-1,-1,-1):
    #     invertida += string[i].lower().replace(" ","")
    if original == invertida:
        return True
    else:
        return False


# print(palindromo("Amo la paloma"))


def invertir_cadena(cadena):
    cadena_invertida = ""
    for valor in cadena:
        cadena_invertida = valor + cadena_invertida
    return cadena_invertida


# print(invertir_cadena("hola mundo"))

# Eliminar caracteres duplicados consecutivos.

#     Enunciado: Dada una cadena, elimina todos
#  los caracteres duplicados consecutivos.
#     Ejemplo: Entrada: "aabbccdde" -> Salida: "abcde"


def eliminar_duplicados(caracteres):
    cadena = ""
    for valor in caracteres:
        if valor not in cadena:
            cadena += valor

    return cadena


# print(eliminar_duplicados("aabbccdde"))

# Contar vocales y consonantes en una cadena.

#     Enunciado: Dada una cadena, cuenta cuántas
#  vocales y cuántas consonantes contiene.
#     Ejemplo: Entrada: "Hola" -> Salida: Vocales: 2, Consonantes: 2


def contar_vocales_consonantes(palabra):
    vocales = {"a", "e", "i", "o", "u"}
    conteo = {"vocales": 0, "consonantes": 0}
    for letra in palabra:
        if letra in vocales:
            conteo["vocales"] += 1
        else:
            conteo["consonantes"] += 1
    return conteo


# print(contar_vocales_consonantes("carlitos"))

# Reemplazar un carácter específico en una cadena.

#     Enunciado: Dada una cadena y un carácter, reemplaza
#     todas las apariciones del carácter por un símbolo #.
#     Ejemplo: Entrada: "banana", "a" -> Salida: "b#n#n#"


def remplazar_caracter(string, caracter):
    # palabra=string.replace(caracter,"#")
    palabra = []
    for letra in string:
        if letra == caracter:
            # palabra.append("#")
            palabra += "#"
        else:
            # palabra.append(letra)
            palabra += letra

    return "".join(palabra)


# print(remplazar_caracter("banana","a"))


# Buscar el primer carácter no repetido en una cadena.

#     Enunciado: Encuentra el primer carácter en una cadena que no se repita.
#     Ejemplo: Entrada: "abacabad" -> Salida: "c"


def primer_no_repetido(cadena):

    diccionario = {}

    for letra in cadena:
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1

    for letra in diccionario:
        if diccionario[letra] == 1:
            return letra

    return None


# print(primer_no_repetido("abacabad"))


def invertir_cadena(cadena):
    palabras = cadena.split()
    inversa = []
    for palabra in palabras:
        inversa.insert(0, palabra)
    return " ".join(inversa)


# print(invertir_cadena("hola mundo"))

# Convertir una cadena a camelCase.

#     Enunciado: Convierte una cadena con palabras
# separadas por espacios o guiones bajos a formato camelCase.
#     Ejemplo: Entrada: "mi_nombre_es_carlos" -> Salida: "miNombreEsCarlos"


def cadena_camelCase(cadena):
    cadena = cadena.replace("_", " ").split()
    resultado = cadena[0].lower()
    for i in range(1, len(cadena)):
        letra_capital = cadena[i][0].upper() + cadena[i][1:].lower()
        resultado += letra_capital

    return "".join(resultado)


# print(cadena_camelCase("mi_nombre_es_carlos"))

# Expandir una cadena comprimida.

#     Enunciado: Dada una cadena comprimida
#  en la forma a2b3c1, expándela a su forma original.
#     Ejemplo: Entrada: "a2b3c1" -> Salida: "aabbbcc"


def expandir_cadena(cadena):
    resultado = ""
    for i in range(0, len(cadena), 2):
        caracter = cadena[i]
        numero = int(cadena[i + 1])
        resultado += caracter * numero

    return resultado


# print(expandir_cadena("a2b3c1"))

# Rotar una lista hacia la derecha.

#     Enunciado: Dada una lista, rota sus
#     elementos k posiciones hacia la derecha.
#     Ejemplo: Entrada: [1, 2, 3, 4, 5], 2 ->
#     Salida: [4, 5, 1, 2, 3]


def rotar_derecha(lista, numero):
    resultado = []
    # resultado = lista[-numero:] + lista[:-numero]
    longitud = len(lista)

    for i in range(longitud - numero, longitud):
        resultado.append(lista[i])
    for i in range(longitud - numero):
        resultado.append(lista[i])

    return resultado


# print(rotar_derecha([1, 2, 3, 4, 5], 2))

# Dividir una lista en n partes iguales.

#     Enunciado: Dada una lista, divídela en n partes iguales.
#     Si no se puede dividir exactamente, la última parte debe ser más corta.
# Ejemplo: Entrada: [1, 2, 3, 4, 5, 6, 7, 8], 3 -> Salida: [[1, 2, 3], [4, 5, 6], [7, 8]]


def dividir_lista(lista, target):
    tam_parte = len(lista) // target
    print(tam_parte)
    resto = len(lista) % target
    print("rest", resto)

    resultado = []
    inicio = 0
    for i in range(target):
        if resto > 0:
            fin = inicio + tam_parte + 1
            resto -= 1
        else:
            fin = inicio + tam_parte
        resultado.append[inicio:fin]
        inicio = fin
    return resultado


# print(dividir_lista([1, 2, 3, 4, 5, 6, 7, 8],3))

# Agrupar elementos en pares consecutivos.

#     Enunciado: Dada una lista, agrupa sus elementos en pares
#  consecutivos. Si la lista tiene un número impar de elementos, el último elemento queda solo.
#     Ejemplo: Entrada: [1, 2, 3, 4, 5] -> Salida: [(1, 2), (3, 4), (5,)]


def agrupar_elementos(lista):
    result = []
    for i in range(0, len(lista), 2):
        if i + 1 < len(lista):
            result.append((lista[i], lista[i + 1]))
        else:
            result.append((lista[i],))

    return result


print(agrupar_elementos([1, 2, 3, 4, 5]))
