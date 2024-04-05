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


print(verificar_vocal("O"))
