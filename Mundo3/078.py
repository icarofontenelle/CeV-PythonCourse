lista = []
menor = maior = 0
for i in range(0, 5):
    num = int(input('Número: '))
    lista.append(num)
    if i == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'Na lista: \033[1;34m{lista}\033[m')
print(f'Maior valor: {maior}, nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'-> {i}', end=' ')
print(f'\nMenor valor: {menor}, nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'-> {i}', end=' ')


