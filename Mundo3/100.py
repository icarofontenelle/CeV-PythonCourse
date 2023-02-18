from random import randint
from time import sleep

def sortear(lista):
    for i in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ' + '-> ', end='')
        sleep(0.5)
    print('Lista preenchida!')

def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos valores pares da lista é {soma}')


numeros = []
sortear(numeros)
somaPar(numeros)