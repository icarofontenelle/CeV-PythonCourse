def aumentar(valor=0.0, taxa=0, formato=False):
    aumento = valor + (valor * taxa/100)
    return aumento if formato is False else moeda(aumento)

def diminuir(valor=0.0, taxa=0, formato=False):
    desconto = valor - (valor * taxa/100)
    return desconto if formato is False else moeda(desconto)

def dobro(valor=0.0, formato=False):
    Vdobro = valor * 2
    return Vdobro if formato is False else moeda(Vdobro)

def metade(valor=0.0, formato=False):
    Vmetade = valor / 2
    return Vmetade if formato is False else moeda(Vmetade)

def moeda(valor=0.0, moeda='R$'):
        return f'{moeda}{valor:.2f}'.replace('.',',')

def resumo(valor=0.0, taxaA=0, taxaD=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'preço analisado: \t{moeda(valor)}')
    print(f'dobro do preço: \t{dobro(valor, True)}')
    print(f'metade do preço: \t{metade(valor, True)}')
    print(f'{taxaA}% de aumento: \t\t{aumentar(valor, taxaA, True)}')
    print(f'{taxaD}% de redução: \t\t{diminuir(valor, taxaD, True)}')
    print('-'*30)