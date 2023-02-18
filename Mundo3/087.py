matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Número: '))
        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A Soma dos valores pares é {sum(pares)}')
print(f'A Soma dos elementos da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O Maior número da segunda linha é {maior}')
