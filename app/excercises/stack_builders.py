def invertir_cadena(cadena):
    # cadena = cadena[::-1]
    cadena_inve=""
    for caracter in cadena:
        cadena_inve =  caracter + cadena_inve
    return cadena_inve

# print(invertir_cadena('Hola mi nombre es Carlos'))
