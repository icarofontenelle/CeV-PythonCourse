aluno = {}
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado!'
    print(f'Aluno: {aluno["nome"]}\nMédia: {aluno["media"]}\nSituação: {aluno["situação"]}')
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
    print(f'Aluno: {aluno["nome"]}\nMédia: {aluno["media"]}\nSituação: {aluno["situação"]}!')
elif aluno['media'] < 5:
    aluno['situação'] = 'Reprovado'
    print(f'Aluno: {aluno["nome"]}\nMédia: {aluno["media"]}\nSituação: {aluno["situação"]}')
