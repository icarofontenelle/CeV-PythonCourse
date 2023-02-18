media = 0
Hvelho = " "
HvelhoIdade = 0
qtdM = 0
for i in range(1, 5):
    print("----- {}ºPessoa -----".format(i))
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("M/F: ").upper().strip()
    media += idade
    if sexo == "M" and idade > HvelhoIdade:
        Hvelho = nome
        HvelhoIdade = idade
    if sexo == "F" and idade < 20:
        qtdM += 1
media = media/4

print("A média de idade do grupo é de {:.2f} anos".format(media))
print("O Homem mais velho do grupo tem {} anos e se chama {}".format(HvelhoIdade, Hvelho))
print("A quantidade de mulheres com menos de 20 anos no grupo é de {}".format(qtdM))
