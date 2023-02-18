'''from math import pow, sqrt
cat1 = float(input("digite o valor do cateto oposto: "))
cat2 = float(input("digite o valor do cateto adjacente: "))
hip = sqrt((pow(cat1, 2)) + (pow(cat2, 2)))
print("o valor da hipotenusa é = {:.2f}".format(hip))'''
from math import hypot
op = float(input("digite o valor do cateto oposto: "))
ad = float(input("digite o valor do cateto adjacente: "))
hi = hypot(op, ad)
print("o valor da hipotenusa é igual a {:.2f}".format(hi))
