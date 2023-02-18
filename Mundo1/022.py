nome = str(input(" digite seu nome completo: ")).strip()
print("O nome com letras maiusculas: {}".format(nome.upper()))
print("O nome com letras minusculas: {}".format(nome.lower()))
espacos = nome.count(" ")
nomeSespaco = len(nome) - espacos
print("A quantidade de letras que possui o nome completo: {}".format(nomeSespaco))
nome = nome.split()
print("A quantidade de letras que possui o primeiro nome: {}".format(len(nome[0])))
