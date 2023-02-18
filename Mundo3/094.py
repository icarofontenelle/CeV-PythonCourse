pessoas = []
cadastro = {}
continuar = 's'
soma = media = 0
while True:
    cadastro.clear() #limpa o dicionário toda vez que entrar no while.
    cadastro['nome'] = input('nome: ')
    cadastro['idade'] = int(input('idade: '))
    soma += cadastro['idade']
    cadastro['sexo'] = input('sexo: (M/F)').lower().strip()[0]
    pessoas.append(cadastro.copy()) #copia o dicionario que acabou de ser preenchido para dentro da lista.
    while cadastro['sexo'] not in "mf":
        cadastro['sexo'] = input('Valor inválido! digite novamente: (M/F): ')
    continuar = input('Cadastrar nova pessoa? S/N ').lower().strip()[0]
    while continuar not in "sn":
        continuar = input('Resposta inválida, digite novamente: (S/N): ')
    if continuar == 'n':
        break
print(f'O número de pessoas cadastradas foram: {len(pessoas)}')
media = soma/len(pessoas)
print(f'A média de idade das pessoas é de {media:5.2f} anos')
print(f'As mulheres cadastradas foram: ', end='')
for i in pessoas:
    if i['sexo'] in 'f':
        print(f'{i["nome"]}' + ', ', end='')
print()
print('Pessoas que Possuem a idade acima da média: ')
for i in pessoas:
    if i['idade'] >= media:
        for k, v in i.items():
            print(f'{k} = {v}; ', end='')
        print()
