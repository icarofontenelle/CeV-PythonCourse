from time import sleep
n1 = float(input("Digite o valor do primeiro número: "))
n2 = float(input("Digite o valor do segundo número: "))
opcao = 0
while opcao != 5:
    sleep(2)
    print("---- MENU ----")
    print('''    [1]- Soma
    [2]- Multiplicação
    [3]- Maior número
    [4]- Novos números
    [5]- Sair''')
    opcao = int(input("Digite sua opção: "))
    if opcao == 1:
        valor = n1+n2
        print("A soma dos valores é: {:.2f} ".format(valor))
        print("="*10)
    elif opcao == 2:
        valor = n1*n2
        print("A multiplicação dos valores é: {:.2f} ".format(valor))
        print("="*10)
    elif opcao == 3:
        if n1 > n2:
            valor = n1
            print("O maior número é: {:.2f} ".format(n1))
            print("="*10)
        elif n1 < n2:
            print("O maior número é: {:2.f} ".format(n2))
            print("="*10)
        else:
            print("Os valores são iguais")
            print("=" * 10)
    elif opcao == 4:
        n1 = float(input("Digite um novo número: "))
        n2 = float(input("Digite um novo número: "))
        print("números trocados com sucesso!")
        print("=" * 10)

print("você saiu do programa!")
