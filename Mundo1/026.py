nome = input("digite um nome: ").upper().strip()
print("A letra 'A' aparece {} vezes".format(nome.count("A")))
print("A letra 'A' aparece a primeira vez na posição {}".format(nome.find("A")+1))
print("A letra 'A' aparece a ultima vez na posição {}".format(nome.rfind("A")+1))