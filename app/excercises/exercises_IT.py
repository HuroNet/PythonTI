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

    diccionario={}

    for letra in cadena:
        if letra in diccionario:
            diccionario[letra]+=1
        else:
            diccionario[letra]=1
    
    for letra in diccionario:
        if diccionario[letra]==1:
            return letra
        
    return None


# print(primer_no_repetido("abacabad"))

def invertir_cadena(cadena):
    return 0

print(invertir_cadena("hola mundo"))