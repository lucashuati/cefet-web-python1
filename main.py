from functions import maior, soma, media, valores_iguais, indice_prim_valor_igual
import random

def main():
    valores1 = [random.randint(0, x + 10) for x in range(10)]
    valores2 = [random.randint(0, x + 10) for x in range(10)]
    valor_a = random.randint(0, 100)
    valor_b = random.randint(0, 100)

    print(f'Lista A: {valores1}')
    print(f'Lista B: {valores2}')
    print(f'Valor A: {valor_a}')
    print(f'Valor B: {valor_b}')
    print(f'Result: maior: {maior(valor_a, valor_b)}')
    print(f'Result: soma: {soma(valores1, valor_b)}')
    print(f'Result: valores_iguais: {valores_iguais(valores1, valores2)}')
    print(f'Result: indice_prim_valor_igual: {indice_prim_valor_igual(valores1, valores2)}')

if __name__ == '__main__':
    main()
