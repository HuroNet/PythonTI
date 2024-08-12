# 1. Two Sum
def two_sum(nums, target):
    for i in range(len(nums) - 1):
        # print(nums[i])
        for j in range(i + 1, len(nums)):
            # print(nums[j])
            # print(nums[i],"+",nums[j],"=",nums[i]+nums[j])
            if i != j and nums[i] + nums[j] == target:
                return i, j
    return False


# print(two_sum([7,44,2,6],8))
# --------------------------------------------------------------------
def inversa_de_una_cadena(cadena):
    # inversa=cadena[::-1]
    inversa = ""
    for valor in cadena:
        inversa = valor + inversa
    return inversa


# print(inversa_de_una_cadena("inversa"))

# Inversa de un arreglo


def list_inverse(lista):
    # inversa_lista = []
    # for i in lista:
    #     inversa_lista = [i] + inversa_lista
    # return inversa_lista
    start = 0
    fin = len(lista) - 1
    for i in range(len(lista) // 2):
        lista[start], lista[fin] = lista[fin], lista[start]
        start += 1
        fin -= 1
    return lista


print(list_inverse([1, 2, 3, 4, 5, 6, 9, 8]))
