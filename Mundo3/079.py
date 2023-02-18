lista = []
while True:
    valor = int(input('valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor já existente!')
    resp = input('Deseja continuar? s/n: ').lower().strip()[0]
    while resp not in 'sn':
        print('\033[1;31mResposta inválida!\033[m')
        resp = input('Deseja continuar? s/n: ').lower().strip()[0]
    if resp == 'n':
        break
lista.sort()
print(f'Os valores digitados foram: \033[1;34m{lista}\033[m')