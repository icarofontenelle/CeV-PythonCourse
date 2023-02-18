from math import sin, cos, tan, radians
ang = int(input("digite o valor do angulo: "))
sen = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print("O seno é {:.2f}, o cosseno é {:.2f} e a tangente {:.2f}.".format(sen, coss, tang))


