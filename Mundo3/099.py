from time import sleep

def maior(*numeros):
    cont = maior = 0
    print('-'*20)
    print('Analisando os valores...')
    for i in numeros:
        print(f'{i}' + ', ', end='')
        sleep(0.5)
        if cont == 0:
            maior = i
        else:
            if i > maior:
                maior = i
        cont +=1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor informado foi {maior}.')


maior(5, 10, 1, 3)
maior()
maior(8, 2, 6, 17, -1)