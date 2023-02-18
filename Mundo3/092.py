from datetime import datetime
dados = {}
dados['nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['Ctps'] = int(input('Carteira de trabalho: (0 se não possui) '))
if dados['Ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-'*30)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')