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
