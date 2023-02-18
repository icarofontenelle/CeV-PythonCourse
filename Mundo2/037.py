num = int(input("digite o numero que deseja converter: "))
print('''escolha uma das bases para conversão: 
[1]: Binário
[2]: Octal
[3]: Hexadecimal''')
escolha = int(input("Digite sua escolha: "))
if escolha == 1:
    print("O número {} convertido para Binário é igual a {}".format(num, bin(num)[2:]))
elif escolha == 2:
    print("O número {} convertido para Octal é igual a {}".format(num, oct(num)[2:]))
elif escolha == 3:
    print("O número {} convertido para Hexadecial é igual a {}".format(num, hex(num)[2:]))
else:
    print("Opção Inválida!")