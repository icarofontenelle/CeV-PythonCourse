valores = (int(input('Valor 1: ')), int(input('Valor 2: ')),
           int(input('Valor 3: ')), int(input('Valor 4: ')))
print(f'Você digitou os valores {valores}')
print(f'O número 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O número 3 apareceu primeiro na posição {valores.index(3)+1}')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram: ', end='')
for i in valores:
    if i % 2 == 0:
        print(i, end=' ')