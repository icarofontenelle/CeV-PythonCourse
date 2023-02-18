from random import randint
from time import sleep
itens = ("pedra", "papel", "tesoura")
print(''' 
[0]PEDRA
[1]PAPEL
[2]TESOURA ''')
jogada = int(input("Faça sua escolha: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("POO!!")
computador = randint(0, 2)
print("\033[1;36m-=\033[m"*11)
print("Você escolheu {}".format(itens[jogada]))
print("O computador escolheu {}".format(itens[computador]))
print("\033[1;36m-=\033[m"*11)
if computador == 0:
    if jogada == 0:
        print("O Jogo Empatou!")
    elif jogada == 1:
        print("Você Ganhou!")
    elif jogada == 2:
        print("Você Perdeu!")
    else:
        print("Jogada inválida.")
elif computador == 1:
    if jogada == 0:
        print("Você Perdeu!")
    elif jogada == 1:
        print("O Jogo Empatou!")
    elif jogada == 2:
        print("Você Ganhou!")
    else:
        print("Jogada inválida.")
elif computador == 2:
    if jogada == 0:
        print("Você Ganhou!")
    elif jogada == 1:
        print("Você Perdeu!")
    elif jogada == 2:
        print("O Jogo Empatou!")
    else:
        print("Jogada inválida.")
print("\033[1;31mFIM DE JOGO!\033[m")

