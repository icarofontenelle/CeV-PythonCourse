primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print("{} > ".format(termo), end="")
        termo += razao
        c += 1
    print("\033[0;31mPAUSA \033[m")
    mais = int(input(("quantos termos quer mostar a mais? ")))
print("Sua Progressão Aritmética chegou ao fim com {} termos".format(total))