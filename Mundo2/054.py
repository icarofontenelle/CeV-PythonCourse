from datetime import date
ano = date.today().year
p = 1
maior = 0
menor = 0
for i in range(1, 8):
    nasc = int(input("Em que ano a {}º pessoa nasceu? ".format(p)))
    p += 1
    idade = ano - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print("A quantidade de pessoas maiores de idade na lista é de {}".format(maior))
print("A quantidade de pessoas menores de idade na lista é de {}".format(menor))
