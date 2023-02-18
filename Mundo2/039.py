from datetime import date
ano = date.today().year
nascimento = int(input("Digite o ano do seu nascimento: "))
idade = (ano - nascimento)
print("Quem nasceu em {}, tem {} anos em {}.".format(nascimento, idade, ano))
if idade == 18:
    print("Você deve se alistar esse ano!")
elif idade < 18:
    tempo = 18 - idade
    print("Ainda faltam {} anos para o seu alistamento!".format(tempo))
    alist = ano + tempo
    print("Seu alistamento será no ano de {}".format(alist))
else:
    tempo = idade - 18
    print("Você deveria ter se alistado à {} anos atrás".format(tempo))
    alist = ano - tempo
    print("Seu alistamento foi no ano de {}".format(alist))


