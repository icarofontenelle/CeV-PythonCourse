ficha = []
while True:
    nome = input('Nome: ')
    nota1 = int(input('Nota1: '))
    nota2 = int(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = input('Continuar? s/n ').strip().lower()[0]
    while resp not in 'sn':
        resp = input('Respota inválida: s/n ')
    if resp == 'n':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    opc = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(ficha)-1:
        print(f'As notas de {ficha[opc][0]} são {ficha[opc][1]}')