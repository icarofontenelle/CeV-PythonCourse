dias = int(input("quantos dias o carro foi alugado: "))
km = float(input("kilometros rodados: "))
preco = (dias * 60) + (km * 0.15)
print("O valor total a se pagar é de R${:.2f}".format(preco))
