lista = []
pares = []
impares = []
#resposta = 's'
while True:
    numero = int(input('número: '))
    lista.append(numero)
    resposta = input('Continuar? s/n: ').strip().lower()[0]
    while resposta not in 'sn':
        resposta = input('Resposta Inválida! s/n: ')
    if resposta == 'n':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A Lista completa é: {lista}')
print(f'Os números pares são: {pares}')
print(f'Os números impares são: {impares}')
