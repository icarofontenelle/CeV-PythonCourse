r1 = float(input("Digite o valor do primeiro segmento:  "))
r2 = float(input("Digite o valor do segundo segmento: "))
r3 = float(input("Digite o valor do terceiro segmento: "))

if r1 >= r2+r3 or r2 >= r1+r3 or r3 >= r2+r1:
    print("Esses segmentos NÂO podem formar um triangulo.")
else:
    print("Esses segmentos PODEM formar um triangulo.")
