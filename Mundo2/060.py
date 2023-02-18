n = int(input("Digite um numero: "))
cont = n
fat = 1
while cont >= 1:
    fat *= cont
    cont -= 1
print("O fatorial de {} é {}".format(n, fat))
