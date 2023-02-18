print("\033[4;31;40m{:-^20}\033[m".format(" LOJA MamaEU "))

valor = float(input("\nDigite o valor da compra: "))
print('''\nDigite a forma de pagamento:
[1] À Vista Dinheiro/Cheque
[2] À Vista no Cartão
[3] Em até 2x no Cartão
[4] 3x ou mais no Cartão''')
pag = int(input("\nDigite a forma de pagamento: "))

if pag == 1:
    total = (valor - valor * (10/100))
elif pag == 2:
    total = (valor - valor * (5/100))
elif pag == 3:
    total = valor
    parcela = valor/2
    print("Sua compra parcelada em 2x vai ficar no valor de R${:.2f}".format(parcela))
elif pag == 4:
    total = (valor + valor * (20/100))
    Tparcela = int(input("Em quantas parcelas deseja pagar? "))
    parcela = total / Tparcela
    print("Sua compra parcelada em {}x vai ficar no valor de R${:.2f}".format(Tparcela, parcela))
else:
    total = valor
    print("\033[1;31m Opção de pagamento invalida\033[m")

print("Sua compra de R${:.2f} vai sair no valor total de R${:.2f}".format(valor, total))