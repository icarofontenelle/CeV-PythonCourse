soma = 0
cont = 0
for i in range(0, 6):
    num = int(input("digite um numero inteiro: "))
    if num % 2 == 0:
        soma += num
        cont += 1
print("Você informou {} número(s) pares e a soma dele(s) é igual a {}".format(cont, soma))