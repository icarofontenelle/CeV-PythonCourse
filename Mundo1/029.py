velocidade = float(input("Digite a velocidade do carro: "))
multa = (velocidade-80)*7
if velocidade <= 80:
    print("Nice, continue assim!")
else:
    print("Você está quase matando alguém e vai ter que pagar uma multa equivalente a R${:.2f}".format(multa))
