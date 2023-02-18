from time import sleep
while True:
    sleep(1)
    print('-'*20)
    n = int(input("Quer ver a tabuada de qual valor?(Negativo para sair) "))
    print('-'*20)
    if n < 0:
        break
    else:
        for i in range(1, 11):
            print(f'{n} x {i} = {n*i}')
print("FIM")


