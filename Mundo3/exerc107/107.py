import moeda

dinheiro = int(input('Digite um valor: R$'))
print(f'O valor com aumento de 10%: R${moeda.aumentar(dinheiro, 10)}')
print(f'O valor com desconto de 15%: R${moeda.diminuir(dinheiro, 15)}')
print(f'O dobro do valor: R${moeda.dobro(dinheiro)}')
print(f'A metade do valor: R${moeda.metade(dinheiro)}')