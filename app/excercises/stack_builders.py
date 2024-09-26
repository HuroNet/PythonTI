def invertir_cadena(cadena):
    # cadena = cadena[::-1]
    cadena_inve = ""
    for caracter in cadena:
        cadena_inve = caracter + cadena_inve
    return cadena_inve


# print(invertir_cadena('Hola mi nombre es Carlos'))


def suma_numeros(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


# print(suma_numeros([1,23,4,5]))


# Números únicos en una lista

#     Descripción: Dado un array de números,
# escribe una función que devuelva una nueva
# # lista que contenga solo los números únicos.
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 3, 5]


def num_unicos(lista):
    numeros = {}
    for num in lista:
        if num in numeros:
            numeros[num] += 1
        else:
            numeros[num] = 1
    print("los numeros de la lista", numeros)
    unicos = [clave for clave, valor in numeros.items() if valor == 1]
    # unicos = []
    # for num in lista:
    #     count = lista.count(num)
    #     # add some variables

    #     if count == 1:
    #         unicos.append(num)

    return unicos


# print(num_unicos([1, 2, 2, 3, 4, 4, 5, 8, 8, 2, 3, 4, 1, 1, 7]))


# Contar vocales y consonantes: Escribe una función que cuente el
# número de vocales y consonantes en una cadena.
def count_letters(palabra):
    diccionario = {"vocales": 0, "consonantes": 0}
    vocales = ["a", "e", "i", "o", "u"]
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    palabra = palabra.lower()

    for letra in palabra:
        if letra in alfabeto:
            if letra in vocales:
                diccionario["vocales"] += 1
            else:
                diccionario["consonantes"] += 1

    return diccionario


# print(count_letters("palindromo"))
# Buscar el segundo número más grande

# #     Descripción: Escribe una función que reciba una lista de
# # números y devuelva el segundo número más grande.


def segundo_grande(lista):
    lista = sorted(lista)

    return lista[-2]


# print(segundo_grande([1, 2, 3, 5, 6, 7, 3, 98]))

# lo mismo pero sin funciones


def seg_grande_x(lista):

    n = len(lista)
    for i in range(0, n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista[-2]


# print(seg_grande_x([1, 3, 4, 3, 4, 23, 45, 5]))

# ahora vamos hacer mediante un ingreso como string


def seg_num_string(*numero):
    lista = sorted(set(numero))

    return lista[-2]


# print(seg_num_string(1,5,5,7,4,3,2,6,5))


# 6. Ordenar una lista de strings por longitud

#     Descripción: Dada una lista de cadenas de
# texto, escribe una función que ordene la lista
# por la longitud de las cadenas, de menor a mayor.
#     Ejemplo:


def order_list_string(string):
    max_string = max(string, key=len)
    return max_string, len(max_string)


# print(order_list_string(["Hola", "Mundo", "a", "Python"]))


def ordenar_mayor(string):
    dicc = {}
    for valor in string:
        dicc[valor] = len(valor)
    maximo = max(dicc, key=len)
    return maximo, len(maximo)


# print(ordenar_mayor(["Hola", "Mundo", "a", "Python"]))

# 7. Contar la frecuencia de palabras en un texto

#     Descripción: Escribe una función que tome un
# texto como entrada y devuelva un diccionario con
# la frecuencia de cada palabra en el texto.
#     Ejemplo:


def frecuencia_palabra(palabras):
    diccionario = {}
    palabras = palabras.replace(",", "")
    palabras = palabras.lower()
    pala = palabras.split(" ")
    for palabra in pala:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario


# print(frecuencia_palabra("hola Hola, mundo, como van hola"))


# Subcadena más larga sin caracteres repetidos
def longest_substraing(cadena):
    inicio = 0
    max_longitud = 0
    caracteres = set()
    for fin in range(len(cadena)):
        while cadena[fin] in caracteres:
            caracteres.remove(cadena[inicio])
            inicio += 1
        caracteres.add(cadena[fin])
        print(caracteres)

        max_longitud = max(max_longitud, fin - inicio + 1)
    return max_longitud


# print(longest_substraing("abcabcbb"))
# 1. Invertir una cadena

#     Descripción: Escribe una función que invierta una cadena.
#     Entrada: "Python"
#     Salida: "nohtyP"


# Suma de números en una lista

#     Descripción: Suma todos los números en una lista.
#     Entrada: [1, 2, 3, 4]
#     Salida: 10


def suma_de_numeros(lista):
    suma = 0
    for valor in lista:
        suma += valor
    return suma


# print(suma_de_numeros([1,2,3,4]))


# Palíndromo

#     Descripción: Verifica si una cadena es un palíndromo.
#     Entrada: "radar"
#     Salida: True


def palindromo(frase):
    reves = frase[::-1]
    if frase == reves:
        return True
    else:
        return False


# print(palindromo('radar'))

# Inversa de un arreglo


def inversa_arreglo(arreglo):
    star = 0
    inversa = []
    end = len(arreglo) - 1
    for valor in range(len(arreglo) // 2):
        arreglo[star], arreglo[end] = arreglo[end], arreglo[star]
        star += 1
        end - +1
        inversa = arreglo
    return inversa


# print(inversa_arreglo([1,2,4,6,3,2]))


def inversa_con_funciones(lista):
    inversa = []
    for valor in lista:
        inversa.insert(0, valor)
        print("sec", valor)

    return inversa


# # print(inversa_con_funciones([1,2,4,6,3,2]))

# Buscar el número más grande

#     Descripción: Encuentra el número más grande en una lista.
#     Entrada: [3, 1, 4, 1, 5, 9]
#     Salida: 9


def numero_mas_grande(numeros):
    number = numeros[0]
    for i in numeros:
        if i > number:
            number = i

    return number


# print(numero_mas_grande([2,45,7,34,3]))

# Contar la frecuencia de caracteres

#     Descripción: Cuenta la frecuencia de cada carácter en una cadena.
#     Entrada: "abracadabra"
#     Salida: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}


def frecuencia_caracteres(string):
    palabras = {}
    for letra in string:
        if letra in palabras:
            palabras[letra] += 1
        else:
            palabras[letra] = 1

    return palabras


# print(frecuencia_caracteres("abracadabra"))

# 8. Número primo

#     Descripción: Verifica si un número es primo.
#     Entrada: 7
#     Salida: True


def es_primo(numero):
    if numero > 1:
        for i in range(2, numero):
            if numero % i == 0:
                return False

        return True


# print(es_primo(6))
# 9. Suma de dígitos

#     Descripción: Calcula la suma de los dígitos de un número.
#     Entrada: 1234
#     Salida: 10


def suma_digitos(dijitos):

    suma = 0
    for dijito in str(dijitos):
        suma += int(dijito)
    return suma


# print(suma_digitos(1234))

# 10. Fibonacci

#     Descripción: Genera los primeros n números de la secuencia de Fibonacci.
#     Entrada: 5
#     Salida: [0, 1, 1, 2, 3]


def fibonacci(number):
    fibo = [0, 1]
    for i in range(2, number):
        fibo.append(fibo[-1] + fibo[-2])
    return fibo


# print(fibonacci(5))

# 11. Contar palabras en una cadena

#     Descripción: Cuenta el número de palabras en una cadena.
#     Entrada: "Hola Mundo"
#     Salida: 2


def contar_palabras(palabras):
    count = 0
    palabras = palabras.split()
    print(palabras)
    for i in palabras:
        count += 1
    return count


# print(contar_palabras("Hola Mundo"))

# 12. Encontrar el índice de un elemento


#     Descripción: Encuentra el índice de un elemento en una lista.
#     Entrada: ([1, 2, 3], 2)
#     Salida: 1
def find_index(lista, numero):
    for i in range(len(lista)):
        if lista[i] == numero:
            return i

    return False


# print(find_index([1,2,3],2))

# 13. Eliminar duplicados de una lista

#     Descripción: Elimina los elementos duplicados de una lista.
#     Entrada: [1, 2, 2, 3, 4, 4]
#     Salida: [1, 2, 3, 4]


def eliminar_duplicados(lista):
    numeros = []

    for numero in lista:
        if numero not in numeros:
            numeros.append(numero)
    return numeros


# print(eliminar_duplicados([1,2,2,3,4,4]))

# 14. Suma de pares en una lista

#     Descripción: Suma los números pares en una lista.
#     Entrada: [1, 2, 3, 4]
#     Salida: 6


def suma_pares(lista):
    pares = []
    suma = 0
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
            suma += i
    # suma=sum(pares)
    return suma


# print(suma_pares([1,4,3,4]))

# 15. Multiplicar elementos de una lista

#     Descripción: Multiplica todos los elementos de una lista.
#     Entrada: [1, 2, 3, 4]
#     Salida: 24


def multiplicar(lista):
    resultado = 1
    for i in lista:
        resultado *= i
    return resultado


# print(multiplicar([1,2,34]))

# 17. Sumar dos matrices

#     Descripción: Suma dos matrices del mismo tamaño.
#     Entrada: ([[1, 2], [3, 4]], [[5, 6], [7, 8]])
#     Salida: [[6, 8], [10, 12]]


def sum_matrices(matris1, matris2):
    suma = []
    for i in range(len(matris1)):
        fila = []
        for j in range(len(matris1[i])):
            fila.append(matris1[i][j] + matris2[i][j])
        suma.append(fila)
    return suma


# print(sum_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]))

# Calcular el factorial de un número

#     Descripción: Calcula el factorial de un número.
#     Entrada: 5
#     Salida: 120


def factorial(numero):
    fact = 1
    for i in range(1, numero + 1):
        fact = fact * i
        i += 1

    return fact


# # print(factorial(5))
# Ordenar una lista de cadenas por longitud

#     Descripción: Ordena una lista de cadenas por la longitud de las cadenas.
#     Entrada: ["Hola", "Python", "Mundo"]
#     Salida: ["Hola", "Mundo", "Python"]


def ordenar_cadena(cadenas):
    return sorted(cadenas, key=lambda x: len(x))


# print(ordenar_cadena( ["Hola", "Python", "Mundo"]))

# 23. Calcular la potencia de un número

#     Descripción: Calcula la potencia de un número dado.
#     Entrada: (2, 3)
#     Salida: 8


def potencia(numero1, numero2):
    resultado = 1
    for i in range(1, numero2 + 1):
        resultado = numero1 * resultado
        i += 1
    return resultado
    # reutun numero1 ** numero2 como la mejor ocion
    # return pow(numero1, numero2)


# print(potencia(2,3))

# 24. Dividir una cadena en palabras

# Descripción: Divide una cadena en palabras usando
# espacios como delimitadores.
#     Entrada: "Hola mundo"
#     Salida: ["Hola", "mundo"]


def dividir_cadena(cadena):
    cadena = cadena.split()
    return cadena


# print(dividir_cadena("Hola mundo"))

# 25. Encontrar la longitud de la cadena más larga

#     Descripción: Encuentra la longitud de la cadena
# más larga en una lista de cadenas.
#     Entrada: ["Hola", "Python", "Desarrollador"]
#     Salida: 12


def long_max_string(cadena):
    diccionario = {}
    for valor in cadena:
        diccionario[valor] = len(valor)
    # return max(diccionario.values())
    # return max(len(cadena, key=len)) solo con esta linea


# print(long_max_string(["Hola", "Python", "Desarrollador"]))

# 26. Invertir una lista

#     Descripción: Invierte una lista.
#     Entrada: [1, 2, 3, 4]
#     Salida: [4, 3, 2, 1]


def inverse_list(lista):
    inversa = []
    for valor in lista:
        inversa.insert(0, valor)
    return inversa
    # return lista[::-1]
    # return lista.reverse()


# print(inverse_list([1,2,83,4]))

# usamos punteros para hacer el ejercicio


def inverse_punteros(lista):
    lista = sorted(lista)
    inicio = 0
    fin = len(lista) - 1
    print(fin)
    while inicio < fin:
        lista[inicio], lista[fin] = lista[fin], lista[inicio]
        inicio += 1
        fin -= 1
    return lista


# print(inverse_punteros([1,4,53,2,3]))


# ahora usamos solo while sin punteros
def inverse_while(lista):
    lista = sorted(lista)
    inversa = []
    inicio = 0
    i = len(lista) - 1
    while i >= inicio:
        inversa.append(lista[i])
        print(i)
        i -= 1

    return inversa


# print(inverse_while([1,43,21,232,3]))

# 27. Eliminar elementos nulos de una lista

#     Descripción: Elimina los elementos nulos de una lista.
#     Entrada: [1, None, 2, None, 3]
#     Salida: [1, 2, 3]


def delete_nulls(lista):
    for i in lista:
        lista.remove(None)
    # return lista
    # return [x for x in lista if x is not None]
    return list(filter(lambda x: x is not None, lista))

    # otro.....
    # lista = [1, None, 2, None, 3]
    # lista_sin_none = []
    # for elemento in lista:
    #     if elemento is not None:
    #         lista_sin_none.append(elemento)
    # print(lista_sin_none)  # Salida: [1, 2, 3]


# print(delete_nulls([1, None,2,None]))

# 30. Eliminar los caracteres no alfabéticos

#     Descripción: Elimina los caracteres no alfabéticos de una cadena.
#     Entrada: "H0la, Mundo!"
#     Salida: "HlaMundo"


def delete_no_alfabeticos(string):
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string = string.replace(",", "").replace(" ", "")
    new_string = ""
    # string=[x for x in string if x is not alfabeto]
    for dato in string:
        if dato in alfabeto:
            new_string += dato
    return new_string


print(delete_no_alfabeticos("H0la, Mundo!"))


def no_alph_join(string):
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    palabras = []
    for valor in string:
        if valor in alfabeto:
            palabras.append(valor)

    return "".join(palabras)


# print(no_alph_join("H0la, Mundo!"))

# 31. Encontrar el índice de la primera aparición de
#  un carácter

#     Descripción: Encuentra el índice de la primera
# aparición de un carácter en una cadena.
#     Entrada: ("Python", "t")
#     Salida: 2


def encontrar_incide(palabra, target):
    for i in range(0, len(palabra)):
        if target == palabra[i]:
            return i
    return -1


# print(encontrar_incide("python","t"))

# 32. Sumar los números en un rango

#     Descripción: Suma todos los números en un
#  rango dado.
#     Entrada: (1, 4)
#     Salida: 10


def suma_in_range(number1, number2):
    suma = 0
    for i in range(number1, number2 + 1):
        suma += i
    return suma
    # return sum(range(number1,number2+1))


# print(suma_in_range(1, 4))

# 33. Determinar el número de letras en una cadena

#     Descripción: Cuenta el número de letras en una cadena.
#     Entrada: "Hola Mundo"
#     Salida: 8


def numero_letras(cadena):
    cambio = cadena.replace(" ", "")
    count = 0
    for i in range(0, len(cambio)):
        count += 1
        print(count, i)
    return count


# print(numero_letras("Hola Mundo"))
