import moeda

dinheiro = float(input('Digite um valor: R$'))

print(f'O valor de {moeda.moeda(dinheiro)} com aumento de 10%: {moeda.aumentar(dinheiro, 10, True)}')
print(f'O valor de {moeda.moeda(dinheiro)} desconto de 15%: {moeda.diminuir(dinheiro, 15, True)}')
print(f'O dobro de {moeda.moeda(dinheiro)}: {moeda.dobro(dinheiro, True)}')
print(f'A metade de {moeda.moeda(dinheiro)}: {moeda.metade(dinheiro, True)}')