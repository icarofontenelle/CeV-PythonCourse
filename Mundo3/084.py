listaPrinc = []
listaSec = []
maior = menor = 0
while True:
    listaSec.append(input('Nome: '))
    listaSec.append(input('Peso: '))
    if len(listaPrinc) == 0:
        maior = menor = listaSec[1]
    else:
        if listaSec[1] > maior:
            maior = listaSec[1]
        elif listaSec[1] < menor:
            menor = listaSec[1]
    listaPrinc.append(listaSec[:])
    listaSec.clear()
    resposta = input('Coninuar? s/n ').strip().lower()[0]
    while resposta not in 'sn':
        resposta = input('Resposta inválida! s/n: ')
    if resposta == 'n':
        break
print(f'A quantidade de pessoas cadastradas foram de {len(listaPrinc)}')
print(f'O Maior peso é de {maior}Kg e são as pessoas:', end='')
for p in listaPrinc:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'\nO Menor peso é de {menor}Kg e são as pessoas:', end='')
for p in listaPrinc:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
