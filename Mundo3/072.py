tup = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',' \
      ''dezessete', 'dezoito', 'dezenove', 'vinte.'
num = 0
while True:
    num = int(input("Digite o valor de um número entre 0 e 20: "))
    if num < 0 or num > 20:
        num = int(input("Digite o valor de um número entre 0 e 20: "))
    else:
        print(f'O número que você escolheu foi {tup[num]}')
        break
