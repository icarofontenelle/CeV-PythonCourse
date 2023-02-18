soma = qtd =0
while True:
    n = int(input("Valor: "))
    if n == 999:
        break
    soma += n
    qtd += 1
print(f'A soma dos {qtd} números é igual a {soma}')
