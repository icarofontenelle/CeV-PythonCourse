from exerc115.lib.Menu import cabeçalho
from exerc115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Cadastrar', 'Listar', 'Sair'])
    if resposta == 1:
        cabeçalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 2:
        lerArquivo(arq)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...')
        break
    else:
        print('ERRO, opção inválida!')
    sleep(1)
