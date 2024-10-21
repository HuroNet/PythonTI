
# Detectar si una cadena es un palíndromo.

#     Enunciado: Verifica si una cadena es la misma 
# al leerla al derecho y al revés. Ignora espacios y mayúsculas.
#     Ejemplo: Entrada: "Amo la paloma" -> Salida: True
def palindromo(string):
    original= string.lower().replace(" ","")
    print("original",original)
    invertida=string[::-1].lower().replace(" ","")
    print("inver",invertida)

    # for i in range(len(string)-1,-1,-1):
    #     invertida += string[i].lower().replace(" ","")
    if original == invertida:
        return True
    else:
        return False
    

# print(palindromo("Amo la paloma"))


def invertir_cadena(cadena):
    cadena_invertida=""
    for valor in cadena:
        cadena_invertida = valor + cadena_invertida
    return cadena_invertida

# print(invertir_cadena("hola mundo"))

# Eliminar caracteres duplicados consecutivos.

#     Enunciado: Dada una cadena, elimina todos
#  los caracteres duplicados consecutivos.
#     Ejemplo: Entrada: "aabbccdde" -> Salida: "abcde"

def eliminar_duplicados(caracteres):
    cadena=""
    for valor in caracteres:
        if valor not in cadena:
            cadena+=valor

    return cadena

# print(eliminar_duplicados("aabbccdde"))

# Contar vocales y consonantes en una cadena.

#     Enunciado: Dada una cadena, cuenta cuántas
#  vocales y cuántas consonantes contiene.
#     Ejemplo: Entrada: "Hola" -> Salida: Vocales: 2, Consonantes: 2