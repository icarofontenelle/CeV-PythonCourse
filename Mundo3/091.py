from random import randint
from time import sleep
from operator import itemgetter
jogos = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
ranking = []
print('Valores Sorteados: ')
for k, v in jogos.items():
    print(f'{k} tirou {v} nos dados')
    sleep(1)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True) #itemgetter = 0 representa chave , = 1 representa valor
print('-'*30)
print('-- Ranking dos Jogadores --')
for i, v in enumerate(ranking):
    print(f'  {i+1} lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)