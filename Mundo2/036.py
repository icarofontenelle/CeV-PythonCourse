valorCasa = float(input("digite o valor da casa: "))
salario = float(input("digite o valor do seu salario: "))
tempo = int(input("Em quantos anos deseja pagar essa casa: "))
prestacao = valorCasa / (tempo*12)
if prestacao > (salario * 30/100):
    print("Para pagar uma casa de {:.2f}, em {} meses, a prestação fica no valor de {:.2f}, então será NEGADA!".format
          (valorCasa, (tempo*12), prestacao))
else:
    print("Para pagar uma casa de {:.2f}, em {} meses, a prestação fica no valor de {:.2f}, então será CONCDIDA!".format
          (valorCasa, (tempo*12), prestacao))