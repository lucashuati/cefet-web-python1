def maior(a, b):
    return a if a > b else b

def soma(valores, x=0):
    aux = 0
    for valor in valores:
        aux += valor
    return aux + x

def media(valores):
    total = soma(valores)
    return total / len(valores)

def valores_iguais(valores1 , valores2):
    comum = []
    for el1 in valores1:
        for el2 in valores2:
            if el1 == el2 and el1 not in comum:
                comum.append(el1)
                break

    return comum

def indice_prim_valor_igual(valores1,valores2):
    for i in range(len(valores1)):
        for j in range(len(valores2)):
            if valores1[i] == valores2[j]:
                return i
