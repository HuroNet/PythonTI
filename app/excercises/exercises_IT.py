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
    inversa= invertir_palabras(palabra).lower().replace(" ","")
    palabra=palabra.replace(" ","").lower()
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
    caracteres=[]
    for valor in string:
        if valor not in caracteres:
            caracteres.append(valor)

    return "".join(caracteres)
# print(eliminar_duplicados("aabbccdde"))

def eliminar_duplicados_indices(string):
    caracteres=[string[0]]
    tam=len(string)
    for valor in string[1:]:
        if valor != caracteres[-1]:
            caracteres.append(valor)
        
    return "".join(caracteres)

# print(eliminar_duplicados_indices("aabbccdde"))

def eliminar_dup_mi_indices(cadena):
    
    return 0

print(eliminar_dup_mi_indices("aabbccdde"))