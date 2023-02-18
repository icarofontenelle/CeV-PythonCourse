from random import randint
from time import sleep
qtd = int(input('Quantidade de vezes que deseja jogar? '))
total = 0
lista = []
jogos = []
while total <= qtd-1:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)