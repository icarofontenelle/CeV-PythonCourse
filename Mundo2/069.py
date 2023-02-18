qtdMaior18 = homens = qtdMmenor20 = 0
resp = "S"
while resp == "S":
    print("CADASTRO DE PESSOAS")
    print('-'*15)
    idade = int(input("Digite a idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input("Digite o sexo: [M/F] ").strip().upper()[0]
    print('-'*15)
    resp = ' '
    while resp not in 'SN':
        resp = input("Quer continuar? [S/N] ").strip().upper()[0]
    if idade > 18:
        qtdMaior18 += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        qtdMmenor20 += 1
    if resp == "N":
        break
print(f'''Pessoas maiores de 18 anos: {qtdMaior18}
Quantidade de homens: {homens}
Quantidade de mulheres com menos de 20 anos: {qtdMmenor20}''')
