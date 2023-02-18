def leiaInt(valor):
    while True:
        try:
            n = int(input(valor))
        except (ValueError, TypeError):
            print('\033[31mErro, digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mPrograma Encerrado!\033[m')
            return 0
        else:
            return n

def leiaFloat(valor):
    while True:
        try:
            n = float(input(valor))
        except (ValueError, TypeError):
            print('\033[31mErro, digite um número real válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mPrograma Encerrado!\033[m')
            return 0
        else:
            return n


num = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {num} e o número real foi {num2}')