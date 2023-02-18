total = prodCaros = cont = menor = 0
prodBarato = ' '
while True:
    nome = input("Produto: ")
    preco = float(input("Preço: R$"))
    cont += 1
    resp = ' '
    while resp not in "SN":
        resp = input(("Continuar? S/N: ")).strip().upper()[0]
    total += preco
    if preco > 1000:
        prodCaros += 1
    if cont == 1 or preco < menor:
       menor = preco
       prodBarato = nome
    if resp == "N":
        break
print(f''' Total gasto na compra: R${total:.2f}
Quantidade de produtos +R$1000: {prodCaros}
O produto mais barato: {prodBarato}
''')

