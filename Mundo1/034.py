salario = float(input("digite o valor do salário: "))
if salario > 1250:
    Nsalario = salario + (salario * 10/100)
else:
    Nsalario = salario + (salario * 15/100)

print("O valor do salario com aumento foi de: R${:.2f}".format(Nsalario))