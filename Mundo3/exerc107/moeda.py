def aumentar(valor, taxa):
    aumento = valor + (valor * taxa/100)
    return aumento

def diminuir(valor, taxa):
    desconto = valor - (valor * taxa/100)
    return desconto

def dobro(valor):
    Vdobro = valor * 2
    return Vdobro

def metade(valor):
    Vmetade = valor / 2
    return Vmetade
