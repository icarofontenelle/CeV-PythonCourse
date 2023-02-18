lista = []
comparar = 0
for i in range(0, 5):
    num = int(input('número: '))
    if i == 0 or num > lista[-1]:
        lista.append(num)
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                break
            posicao += 1
print(f'A lista em ordem é {lista}')

