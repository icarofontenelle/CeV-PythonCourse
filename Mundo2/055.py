maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input("digite o peso da {}º pessoa: ".format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("A pessoa mais pesada tem {}Kg".format(maior))
print("A pessoa mais leve tem {}Kg".format(menor))
