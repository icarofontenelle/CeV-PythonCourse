frase = input("digite uma frase: ").strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for i in range(len(junto)-1, -1, -1):
    inverso += junto[i]
print("A frase é {}, e ela invertida fica {}".format(junto, inverso))
if junto == inverso:
    print("Temos um palíndromo")
else:
    print("Não temos um palíndromo")
