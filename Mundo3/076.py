produtos = ('cerveja', 5.00, 'Pitú', 1.99, 'Gasolina', 42.36)
print('\033[1;31m--------Lista de Produtos--------\033[m')
for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<30}', end=' ')
    else:
        print(f'R${produtos[i]:5.2f}')
print('-'*35)