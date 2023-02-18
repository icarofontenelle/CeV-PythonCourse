somatorio = 0
contador = 0
inicio = 1
while inicio != 999:
    valor = int(input("Digite um valor: [999 para PARAR]-> "))
    if valor != 999:
        somatorio = somatorio + valor
        contador += 1
        inicio = valor
    else:
        break
print("A soma dos {} números foi igual à: {}".format(contador, somatorio))
