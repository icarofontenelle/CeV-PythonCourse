lista = [[], []]
for i in range (1, 8):
    num = int(input('Número: '))
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 == 1:
        lista[1].append(num)
lista[0].sort() # Coloca a lista em ordem.
lista[1].sort()
print(f'Os números pares -> {lista[0]}')
print(f'Os números impares -> {lista[1]}')