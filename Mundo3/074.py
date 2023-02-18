from random import randint
valores = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números gerados foram: {valores}')
print(f'O maior valor foi {max(valores)} e o menor foi {min(valores)}')