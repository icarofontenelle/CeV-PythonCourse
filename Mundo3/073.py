campeoes = ('Zoe', 'TF', 'Ez', 'Taric', 'Lee Sin', 'J4', 'Karma', 'Fizz', 'Lucian', 'Azir', 'Kindred', 'Hecarim',
            'MF', 'Riven', 'LB', 'Shyvana')
print(f'Os 5 primeiros campeões da lista são: \033[1;34m{campeoes[:5]}\033[m')
print(f'Os 4 ultimos campeões da lista são: \033[1;34m{campeoes[-4:]}\033[m')
print(f'Os campeões em ordem alfabética: \033[1;34m{sorted(campeoes)}\033[m')
print(f'O J4 é o {campeoes.index("J4")+1} campeão')

