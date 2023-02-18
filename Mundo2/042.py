r1 = float(input("Digite o valor do primeiro segmento: "))
r2 = float(input("Digite o valor do segundo segmento: "))
r3 = float(input("Digite o valor do terceiro segmento: "))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r2+r1:
    print("Esses Segmentos PODEM formar um triangulo ", end="")
    if r1 == r2 == r3:
        print("EQUILÁTERO")
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print("ISÓSCELES")
    else:
        print("ESCALENO")
else:
    print("Esses Segmentos NÃO PODEM formar um triangulo")

