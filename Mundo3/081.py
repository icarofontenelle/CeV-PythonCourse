lista = []
resposta = 's'
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    resposta = input('Continuar? s/n: ').strip().lower()[0]
    while resposta not in 'sn':
        resposta = input('Resposta invalida! digite novamente: s/n ')
    if resposta == 'n':
        break
print(f'A quantidade de elementos digitados foi de: {len(lista)}')
lista.sort(reverse=True)
print(f'Os números em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
