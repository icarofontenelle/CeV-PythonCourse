time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for i in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {i+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['tot'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = input('Quer continuar? (S/N) ').lower().strip()[0]
        if resp in 'sn':
            break
        print('Responda apenas S/N!')
    if resp == 'n':
        break
print('='*40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*30)
for k, v in enumerate(time):
    print(f' {k:>5} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('='*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 encerra) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Error! não existe jogador com código {busca}!')
    else:
        print(f'-- Levantamento do jogador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')
    print('-'*40)
print("ENCERRADO!!")