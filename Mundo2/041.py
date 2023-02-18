from datetime import date
ano = date.today().year
anoN = int(input("digite o ano de nascimento do atleta: "))
idade = ano - anoN
if idade <= 9:
    print("O atleta tem {} anos.".format(idade))
    print("Classificação: MIRIM ")
elif 10 <= idade <= 14:
    print("O atleta tem {} anos.".format(idade))
    print("Classificação: INFANTIL ")
elif 15 <= idade <= 19:
    print("O atleta tem {} anos.".format(idade))
    print("Classificação: JUNIOR ")
elif 20 <= idade <= 25:
    print("O atleta tem {} anos.".format(idade))
    print("Classificação: SÊNIOR ")
else:
    print("O atleta tem {} anos.".format(idade))
    print("Classificação: MASTER")