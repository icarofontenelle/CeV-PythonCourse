def aumentar(valor=0, taxa=0):
    aumento = valor + (valor * taxa/100)
    return aumento

def diminuir(valor=0, taxa=0):
    desconto = valor - (valor * taxa/100)
    return desconto

def dobro(valor=0):
    Vdobro = valor * 2
    return Vdobro

def metade(valor=0):
    Vmetade = valor / 2
    return Vmetade

def moeda(valor=0, moeda='R$'):
        return f'{moeda}{valor:.2f}'.replace('.',',')

