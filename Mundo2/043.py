altura = float(input("digite sua altura: "))
peso = float(input("digite seu peso: "))
imc = peso / (altura * altura)

if imc < 18.5:
    print("Seu IMC tem o valor de {:.2f}, ABAIXO DO PESO.".format(imc))
elif 18.5 <= imc < 25:
    print("Seu IMC tem o valor de {:.2f}, PESO IDEAL.".format(imc))
elif 25 <= imc < 30:
    print("Seu IMC tem o valor de {:.2f}, SOBREPESO.".format(imc))
elif 30 <= imc < 40:
    print("Seu IMC tem o valor de {:.2f}, OBESIDADE.".format(imc))
else:
    print("Seu IMC tem o valor de {:.2f}, OBESIDADE MORBIDA.".format(imc))