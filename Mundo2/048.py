soma = 0
for i in range(1, 501, 2):
    if i % 3==0:
        soma = soma + i
print("A soma de todos os números ímpares múltiplos de 3 entre 1 e 500 é igual a {}.".format(soma))
