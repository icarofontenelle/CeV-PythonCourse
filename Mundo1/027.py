nome = input("digite seu nome completo: ").strip()
n = nome.split()
print("seu primeiro nome é: {}".format(n[0]))
print("Seu ultimo nome é: {}".format(n[len(n)-1]))
