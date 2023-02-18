from random import randint
vitorias = soma = 0
while True:
    valor = int(input("Digite um valor: "))
    escolha = input("Deseja par ou impar? [P/I]: ").upper().strip()[0]
    comp = randint(0, 10)
    soma = valor + comp
    if escolha == "P":
        if soma % 2 == 0:
            print(f'Você jogou {valor} e o computador jogou {comp}, você ganhou essa!')
            vitorias += 1
        elif soma % 2 == 1:
            print(f'Você jogou {valor} e o computador jogou {comp}, você perdeu!')
            break
    if escolha == "I":
        if soma % 2 == 1:
            print(f'Você jogou {valor} e o computador jogou {comp}, você ganhou essa!')
            vitorias += 1
        elif soma % 2 == 0:
            print(f'Você jogou {valor} e o computador jogou {comp}, você perdeu!')
            break
print(f"\nGame Over! você obteve o total de {vitorias} vitórias!")
