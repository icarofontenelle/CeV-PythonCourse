from random import randint
computador = randint(0, 10)
print("\033[1;35mTente acertar o número escolhido pelo computador!\033[m")
num = int(input("Digite um número entre 0 e 10: "))
cont = 1
while num != computador:
    if 0 > num > 10:
        num = int(input("\033[0;31m número inválido! digite um número entre 0 e 10: \033[m"))
    elif computador < num:
        num = int(input("Menos.. tente novamente: "))
        cont += 1
    elif computador > num:
        num = int(input("Mais.. tente novamente: "))
        cont += 1
print("Você acertou! O número que pensei foi {}".format(computador))
print("Você Acertou com {} tentativas!".format(cont))