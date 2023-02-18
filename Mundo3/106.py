c = ('\033[m',
     '\033[0;30;41m')


def ajuda(com):
    help(com)


def titulo(msg, cor=0):
    tam = len(msg)
    print('-'*tam)
    print(msg)
    print('-'*tam)



comando = ''
while True:
    comando = input('Função ou biblioteca -> ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)