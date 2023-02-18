from random import randint
numero = randint(0, 5)
n = int(input("Digite um numero entre 0 e 5: "))
if numero == n:
    print("parabens, você acertou!")
else:
    print("você errou! o número sorteado foi o {}".format(numero))

