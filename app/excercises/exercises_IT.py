
# Detectar si una cadena es un palíndromo.

#     Enunciado: Verifica si una cadena es la misma 
# al leerla al derecho y al revés. Ignora espacios y mayúsculas.
#     Ejemplo: Entrada: "Amo la paloma" -> Salida: True
def palindromo(string):
    original= string.lower().replace(" ","")
    invertida=""
    for i in range(len(string)-1,-1,-1):
        invertida += string[i].lower().replace(" ","")
    if original == invertida:
        return True
    else:
        return False
    

print(palindromo("Amo la paloma"))


def invertir_cadena(cadena):
    cadena_invertida=""
    for valor in cadena:
        cadena_invertida = valor + cadena_invertida
    return cadena_invertida

# print(invertir_cadena("hola mundo"))
