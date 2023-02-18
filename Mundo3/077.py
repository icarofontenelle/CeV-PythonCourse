palavras = ('chave', 'lasanha', 'cerveja', 'cafe')
for i in palavras:
    print(f'\nAs vogais na palavra {i.upper()} são: ', end=' ')
    for v in i:
        if v.lower() in 'aeiou':
            print(f'{v}', end=' ')