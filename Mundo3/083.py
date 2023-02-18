expressao = input('expressao: ')
pilha = []
for i in expressao:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('Sua expressão foi válida!')
elif len(pilha) > 0:
    print('Sua expressão foi inválida!')
