sexo = input("Digite seu sexo: F/M ").lower().strip()[0]
while sexo not in "mf":
    sexo = input("Sexo inválido, digite novamente: F/M ").lower().strip()[0]
print("O sexo {} foi registrado com sucesso".format(sexo))


