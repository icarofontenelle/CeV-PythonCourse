import moeda

dinheiro = float(input('Digite um valor: R$'))
print(f'O valor de {moeda.moeda(dinheiro)} com aumento de 10%: {moeda.moeda(moeda.aumentar(dinheiro, 10))}')
print(f'O valor de {moeda.moeda(dinheiro)} desconto de 15%: {moeda.moeda(moeda.diminuir(dinheiro, 15))}')
print(f'O dobro de {moeda.moeda(dinheiro)}: {moeda.moeda(moeda.dobro(dinheiro))}')
print(f'A metade de {moeda.moeda(dinheiro)}: {moeda.moeda(moeda.metade(dinheiro))}')