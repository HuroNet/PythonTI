# basic excersises
# Name: Carlos Paredes
# email:carlos.paredes23@hotmail.com


# Escribir una función que tome un carácter y devuelva True si es una vocal,
# de lo contrario devuelve False.
def verificar_vocal(leter):
    vocales = ["a", "e", "i", "o", "u"]
    leter = leter.lower()
    if leter in vocales:
        return True
    else:
        return False


# print(verificar_vocal("O"))

# Definir una función inversa() que calcule la inversión de una cadena.
# Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa(cadena):
    #palabra=cadena[::-1] ##este es el primer metodo 
    cadena_invertida=""
    for caracter in cadena:
        cadena_invertida = caracter+ cadena_invertida
    return cadena_invertida

#print(inversa("estoy probando"))