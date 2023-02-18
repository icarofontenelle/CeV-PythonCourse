cont = "s"
qtd = soma = nMaior = nMenor = 0
while cont == "s":
    num = int(input("Digite um número: "))
    soma += num
    qtd += 1
    if qtd == 1:
        nMaior = nMenor = num
    else:
        if num > nMaior:
            nMaior = num
        if num < nMenor:
            nMenor = num
    cont = input("Deseja continuar?: S/N ").lower().strip()[0]
media = soma / qtd
print("Você digitou {} números. A média entres eles é de {}".format(qtd, media))
print("O maior número é {}, e o menor é {}".format(nMaior, nMenor))
