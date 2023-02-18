def jogador(nome = '<desconhecido>', gols = 0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


n = input('Nome do jogador: ')
gol = input('Número de gols no campeonato: ')
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if len(n) == 0:
    print(jogador(gols=gol))
else:
    print(jogador(n, gol))
