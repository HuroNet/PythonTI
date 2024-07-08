# basic excersises
# Name: Carlos Paredes
# email:carlos.paredes23@hotmail.com


# from app.excercises.delete import delete
# from app.excercises.delete import delete


def verificar_si_es_vocal(leter):
    vocales = ["a", "e", "i", "o", "u"]
    leter = leter.lower()
    if leter in vocales:
        return True
    else:
        return False


def inversa_de_una_cadena(cadena):
    # palabra=cadena[::-1] ##este es el primer metodo
    cadena_invertida = ""
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida


# print(inversa("[1,3,4,56,6]"))


def sum(a):
    suma = 0
    for i in a:
        suma = suma + i
    return suma


def multi(b):
    multi = 1
    for i in b:
        multi *= i
    return multi


# print(sum([1,2,3,4]))
# print(multi([1,2,3,4]))


def generar_n_caracteres(entero, caracter):
    for i in range(1, entero + 1):
        caracteres = i * caracter
    return caracteres


# print(generar_n_caracteres(5, "x"))

# Definir una función generar_n_caracteres() que tome un entero
# n y devuelva el caracter multiplicado por n.
# Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx"


def generar_caracteres(m, n):
    for i in range(0, m + 1):
        caracteres = i * n
        print("los caracteres son:", caracteres)
    return caracteres


# print(generar_caracteres(5, "x"))


def longitud(dato):
    long = 0
    for i in dato:
        long += 1
    return long


# print(longitud([1,2,3,5,4]))
# print(longitud("Hola mundo "))
# new excercise
# inversa de un numero
def string_inverse(lista):
    inicio = 0
    fin = len(lista) - 1
    print(fin)
    while inicio < fin:
        lista[inicio], lista[fin] = lista[fin], lista[inicio]
        inicio = inicio + 1
        fin = fin - 1
    return lista


# print(string_inverse([1,2,43,9,73]))


# con el bucle for cambio new change
def string_for(lista):
    inicio = 0
    fin = len(lista) - 1
    for _ in range(len(lista) // 2):
        lista[inicio], lista[fin] = lista[fin], lista[inicio]
        inicio += 1
        fin -= 1
    return lista


# -------------------------------------
# convertir cadena de numeros a list
def stringToList(cadena):
    lista = []
    numeros = cadena.split(",")
    for numero in numeros:
        print(numero)
        numero_entero = int(numero)
        lista.append(numero_entero)
    return lista


# print(stringToList("1,2,3,4,5"))

# forma mas sencilla de hacer un cambio de
# numero en cadena a lista
# ejercico de entrevista


def cadena_a_lista(cadena):
    numeros = cadena.split(",")
    lista = [int(numero) for numero in numeros]
    return lista


# print(cadenaALista("1,34,4,5,3,3"))


def superposition(lista1, lista2):
    for valor in lista1:
        print(valor)
        if valor in lista2:
            return True

    return False


# print(superposition([1, 2, 3, 4], [5, 6, 2, 4]))
# print(superposition([1, 2, 3, 4], [5, 6, 2, 4]))

# delete.py


# Subcadena más larga sin caracteres repetidos
def longest_substraing(cadena):
    charset = set()  # actualizar la lista -- se crea un diccionario
    longitud = 0  # calculo  de la longitud
    left = 0
    for right in range(0, len(cadena)):
        while cadena[right] in charset:
            charset.remove(cadena[left])
            left += 1
        charset.add(cadena[right])
        longitud = max(longitud, right - left + 1)

    return longitud


# print(longest_substraing("abcdabca"))


# another fuction
def cadena_larga(cadena):
    longitud_cadena = 0
    lista_cadena = list(cadena)
    new_list = []
    for valor in lista_cadena:
        if valor not in new_list:
            new_list.append(valor)
            longitud_cadena += 1
    return longitud_cadena


# print(cadena_larga("abcdabcd"))


# problema de entrevista---
# devolver cuantas evces se repite
text = "Hola mi nombre es Carlos, entonces yo decir Hola esta bien decir hola"


def minusculas(text):
    text = text.lower()
    return text


def modificar(text):
    text = text.replace(",", "").replace(".", "")
    text = text.split()
    return text


def repetitions(text):
    palabras = {}
    for palabra in text:
        if palabra in palabras:
            palabras[palabra] += 1
        else:
            palabras[palabra] = 1
    return palabras


def mayores(text):
    repeticiones = repetitions(text)
    max_repeticiones = repeticiones.values()

    return max_repeticiones


# print(repetitions(modificar(minusculas(text))))
# print(mayores(modificar(minusculas(text))))
# print(modificar(minusculas(text)))


def fizzbuzz(num):
    for i in range(1, num + 1):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


# print(fizzbuzz(15))


def inversa_arrglo(arreglo):
    start = 0
    end = len(arreglo) - 1
    for i in range(len(arreglo) // 2):
        arreglo[start], arreglo[end] = arreglo[end], arreglo[start]
        start += 1
        end -= 1

    return arreglo


# print(inversa_arrglo([1, 3, 5, 7, 8, 3]))

# convertir cadena de numeros a list


def aLista(cadena):
    lista = []
    numeros = cadena.split(",")

    for i in numeros:
        enteros = int(i)
        lista.append(enteros)
    return lista


# print(aLista("1,2,3,9,5"))


# Subcadena más larga sin caracteres repetidos
def subcadena(cadena):
    charset = set()
    longitud = 0
    left = 0
    for right in range(0, len(cadena)):
        while cadena[right] in charset:
            charset.remove(cadena[left])
            left += 1
        charset.add(cadena[right])
        longitud = max(longitud, right - left + 1)
    return longitud


# print(subcadena("abcabca"))


# Escribe una función en Python que invierta una cadena dada.
def cadena_dada(cadena):
    cadena_invertida = ""
    for dato in cadena:
        cadena_invertida = dato + cadena_invertida

    return cadena_invertida


# print(cadena_dada("hola mundo"))


# Escribe una función que cuente el número de palabras en una cadena.
def contar_palabras(cadena):
    count = 0
    cadena = cadena.split(" ")
    for palabra in cadena:
        count += 1
    return count


# print(contar_palabras("hola soy Carlos para ustedes"))

# Escribe una función que reciba una lista de números y devuelva una
# nueva lista con los números pares.


def numeros_pares(lista):
    pares = []
    suma = 0
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        suma = numero + suma
    return pares, suma


# print(numeros_pares([1,3,5,6,8,9,2]))

# Escribe una función que reciba una lista de números y devuelva el
# número máximo y el número mínimo de la lista.


def num_max_min(lista):
    maximo = lista[0]
    minimo = lista[0]
    for numero in lista:

        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero

    return maximo, minimo


# print(num_max_min([2, 9, 5, 3, 2, 49]))

# Escribe una función que reciba una lista de números y elimine los
# duplicados, devolviendo una lista con elementos únicos.


def numeros_duplicados(lista):
    unicos = []
    for numero in lista:
        print(numero)
        if numero not in unicos:
            unicos.append(numero)
    return unicos


# print(numeros_duplicados([1, 3, 4, 4, 5, 7, 4]))

# Escribe un programa en Python que lea un archivo de texto
# y cuente la frecuencia de cada palabra.

texto = "hOLA como estas, te escribo esta carga la para carga de material y la TE"


def frecuencia_palabra(texto):
    frecuencia = {}
    texto = texto.lower().split(" ")
    for palabra in texto:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia


print(frecuencia_palabra(texto))
