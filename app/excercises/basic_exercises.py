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
text = "Hola mi nombre es s, entonces "


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



def frecuencia_palabra(texto):
    frecuencia = {}
    texto = texto.lower().split(" ")
    for palabra in texto:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia


# print(frecuencia_palabra(texto))


# Verificicar si es  palindromo


def palindromo(palabra):
    inversa = palabra[::-1]
    for letra in range(len(palabra) // 2):
        if palabra[letra] != palabra[len(palabra) - letra - 1]:
            return False

    return True, inversa


# print(palindromo("reconocer"))


# factorial un numero dado calcular de forma recursiva
def factorial(numero):
    facto = 1
    for i in range(1, numero + 1):
        facto = i * facto
    return facto


def factorial_recursivo(numero):
    facto = 1
    if numero == 0 or numero == 1:
        facto = 1
    else:
        facto = numero * factorial_recursivo(numero - 1)
    return facto


# print(factorial_recursivo(5))
# print(factorial(5))


# transformar a Mayuscula la primera letra
def mayuscula_primera(palabra):
    capitalize = palabra.capitalize()
    palabra = palabra[0][0].upper() + palabra[1:]
    return palabra, capitalize


# print(mayuscula_primera("carlos"))


# encontrar valor menor cercano
def valor_menor(lista):
    valor = lista[0]
    for i in lista:
        if valor > i:
            valor = i
    return valor


# print(valor_menor([34,54,32,18,45,32,43]))

# Escribir un programa en python que de solución al problema del FizzBuzz


def FizzBuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        if i % 3 == 0:
            print("fizz")
        if i % 5 == 0:
            print("buzz")
        else:
            print(i)


# print(FizzBuzz())

# Saludar con clase


class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.passwprd = password

    def saluda(self) -> str:
        return f"Hola {self.username}"


cody = User("Cody", "axel29")
# print(cody.saluda())

# Escribe una función que determine si dos cadenas de texto
# son anagramas (tienen las mismas letras en diferente orden).


def anagrama(palabra1, palabra2):
    palabra1 = sorted(palabra1.lower())
    palabra2 = sorted(palabra2.lower())

    if palabra2 == palabra1:
        return "son anagrmas"
    else:
        return False


# print(anagrama('roma','amor'))

# Escribe una función que genere los primeros n números
# de la secuencia de Fibonacci.


def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
        print(fib[-1] + fib[-2])

    return fib


# print(fibonacci(5))
# Escribe una función que tome una oración y devuelva
# la misma oración con las palabras en orden inverso.
def invertir_oracion(oracion):
    oracion1 = oracion[::-1]
    oracion2 = ""
    print(oracion1)
    for letra in oracion:
        oracion2 = letra + oracion2

    return oracion2


# print(invertir_oracion('Mi nombre es carlos paredes'))


# Escribe una función que tome una lista de números y
# la ordene de menor a mayor sin usar la función sorted() de Python.
def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
    return lista


# # print(ordenar_lista([3,5,21,34,5,2,3,45,66]))
# Escribe una función que cuente el número de veces
# que cada palabra aparece en un texto.
texto = "hOLA como estas esta carga la, para carga de material y la TE"


def contar_palabra_text(texto):
    palabras = {}
    texto = texto.split()
    for palabra in texto:
        if palabra in palabras:
            palabras[palabra] += 1
        else:
            palabras[palabra] = 1

    return palabras


# print(contar_palabra_text(texto))

# Escribe una función que tome una lista de números
# y devuelva la suma de todos los números pares en la lista.


def return_pares(lista):
    pares = []
    for valor in lista:
        if valor % 2 == 0:
            pares.append(valor)
    return pares


# print(return_pares([1,2,3,4,5,6,7,8,9,0]))

# Escribe una función que tome una lista de números
# y devuelva el valor máximo.


def valor_maximo(lista):
    maximo = lista[0]
    for valor in lista:
        if valor > maximo:
            maximo = valor
    return maximo


# print(valor_maximo([1, 45, 93, 4]))

# Escribe una función que implemente la búsqueda binaria para
# encontrar la posición de un número en una lista ordenada.


def busqueda_binaria(target, lista):
    positions = []
    for valor in lista:
        if valor == target:
            positions = lista[valor]

    return positions


# # print(busqueda_binaria(3,[8,5,3,2,45,6,7]))
# Escribe una función que elimine los elementos duplicados
# de una lista y devuelva una lista con los elementos únicos.


def eliminar_duplicados(lista):
    vistos = set()
    lista_unica = []
    for elemento in lista:
        if elemento not in vistos:
            lista_unica.append(elemento)
            vistos.add(elemento)

    return lista_unica


# print(eliminar_duplicados([3,5,7,8,3,7,6,8]))

# Comprimir Cadena

# Escribe una función que comprima una cadena de texto usando
# el conteo de caracteres repetidos. Por ejemplo, la cadena
# "aabcccccaaa" debería convertirse en "a2b1c5a3".


def comprimir_cadena(cadena):
    comprimida = []
    conteo = 1

    for i in range(1, len(cadena)):
        if cadena[i] == cadena[i - 1]:
            conteo += 1
        else:
            comprimida.append(cadena[i - 1] + str(conteo))
            conteo = 1
    comprimida.append(cadena[-1] + str(conteo))
    return "".join(comprimida)


# # print(comprimir_cadena("aabcccccaaa"))
# Factorial

# Escribe una función que calcule el factorial de un número entero no negativo.


def factorial(numero):
    fact = 1
    if numero > 0:
        for i in range(numero, 0, -1):
            fact = i * fact
            print(fact)
    return fact


# print(factorial(89))


# hacer el minimo comun multipli de un numero
def prime_factors(n):
    i = 2
    factors = {}
    while i * i <= n:
        while (n % i) == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = 1
    return factors


def merge_factors(factors1, factors2):
    merged_factors = factors1.copy()
    for factor, count in factors2.items():
        if factor in merged_factors:
            merged_factors[factor] = max(merged_factors[factor], count)
        else:
            merged_factors[factor] = count
    return merged_factors


def calculate_mcm_from_factors(factors):
    mcm = 1
    for factor, count in factors.items():
        mcm *= factor**count
    return mcm


# Calcula el MCM de dos números
a = 12
b = 18

factors_a = prime_factors(a)
factors_b = prime_factors(b)

merged_factors = merge_factors(factors_a, factors_b)
mcm = calculate_mcm_from_factors(merged_factors)

# print(f"El MCM de {a} y {b} es {mcm}")\

# Intersección de Listas

# Escribe una función que tome dos listas y devuelva una nueva
# lista con los elementos que están en ambas listas.


def interseccion_listas(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    interseccion = set1.intersection(set2)
    return list(interseccion)


# Ejemplo de uso
lista1 = [1, 2, 2, 3, 4]
lista2 = [3, 4, 4, 5, 6]

# print(interseccion_listas(lista1, lista2))  # Salida: [3, 4]


# Número Perfecto

# Escribe una función que determine si un
# número es un número perfecto (la suma de sus divisores propios es igual al número).


def es_numero_perfecto(n):
    if n <= 0:
        return False

    suma_divisores = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            suma_divisores += i

    return suma_divisores == n


# print(es_numero_perfecto(6))   # True
# print(es_numero_perfecto(12))  # False

#  Generar una Secuencia de Números Fibonacci


# Escribe una función que genere una secuencia de
# números Fibonacci de longitud n.
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence


# Ejemplo de uso
n = 10
# # print(fibonacci_sequence(n))
# Generar un Triángulo de Pascal


# Escribe una función que genere un triángulo
# de Pascal de altura n.
def generar_triangulo_de_pascual(n):
    triangulo = []

    for i in range(n):
        fila = [1] * (i + 1)
        for j in range(1, i):
            fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
        triangulo.append(fila)

    return triangulo


# Ejemplo de uso:
altura = 5
triangulo_de_pascual = generar_triangulo_de_pascual(altura)

for fila in triangulo_de_pascual:
    print(fila)
