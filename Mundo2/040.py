n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2

if media < 5.0:
    print("Sua média foi de {:.1f}, você está REPROVADO!".format(media))
elif 7 > media >= 5:
    print("Sua média foi de {:.1f}, você está de RECUPERAÇÃO!".format(media))
else:
    print("Sua média foi de {:.1f}, você foi APROVADO!".format(media))
