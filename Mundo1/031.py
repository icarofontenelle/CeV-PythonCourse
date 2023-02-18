distancia = float(input("digite a distancia da sua viagem (Km): "))
p1 = distancia * 0.5
p2 = distancia * 0.45
if distancia <= 200:
    print("O valor da sua viagem é: R${:.2f}".format(p1))
else:
    print("O valor da sua viagem é: R${:.2f}".format(p2))
