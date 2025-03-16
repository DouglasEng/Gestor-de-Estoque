from time import sleep
import os

def limpar_tela():
    os.system("cls" if os.name=="nt" else "clear")

def mostrar_menu():
    print('''
------------------------------
|    CONTROLE DE ESTOQUE     |
------------------------------
| 1 - Adicionar Estoque      |
| 2 - Consultar Estoque      |
| 3 - Remover Estoque        |
| 4 - Sair                   |
------------------------------
    ''')


def adicionar_produto():
    limpar_tela()
    produto_nome = input('Produto: ').strip().upper()
    while True:
        try:
            quantidade = float(input('Quantidade: '))
            break
        except:
            print('Valor inválido!\n')

    produto_existe = False
    for produtos in estoque:
        if produtos[0] == produto_nome:
            produtos[1] += quantidade  
            produto_existe = True
            break

    if not produto_existe:
        estoque.append([produto_nome, quantidade])
        print('Produto cadastrado com sucesso!')
    cont = str(input('\nAperte enter para continuar.'))
    limpar_tela()

def consultar_produto():
        limpar_tela()
        if len(estoque) == 0:
            print('\nEstoque vazio.')
        else:
            print('=-'*17)
            print(f'{'Nº':<5} {'Produtos':<15} {'Quantidade':<5}')
            print('=-'*17)
            for indice, produtos in enumerate(estoque, start= 1):
                print(f'{indice:<5} {produtos[0]:<15} {produtos[1]:<5}')
            print('=-'*17,'\n')
        cont = str(input('\nAperte enter para continuar.'))
        limpar_tela()
        
def remover_produto():
    limpar_tela()
    print('=-'*17)
    print(f'{'Nº':<5} {'Produtos':<15} {'Quantidade':<5}')
    print('=-'*17)
    for indice, produtos in enumerate(estoque, start= 1):
        print(f'{indice:<5} {produtos[0]:<15} {produtos[1]:<5}')
    print('=-'*17)
    remover = int(input('Indice do produto: '))
    if remover > len(estoque) or remover <= 0:
        print('ERRO! Valor invalido!')
    else:
        quantidade_remocao = float(input('Quantidade de remoção: '))
        if quantidade_remocao > estoque[remover-1][1]:
            print('ERRO! Valor de remoção maior que de estoque')
        elif quantidade_remocao == estoque[remover-1][1]:
            estoque.pop(remover-1)
            print('Produto removido!')
        else:
            estoque[remover-1][1] -= quantidade_remocao
            print(f'Foi removido {quantidade_remocao} de {estoque[remover-1][0]} totalizando {estoque[remover-1][1]}')
    cont = str(input('\nAperte enter para continuar.'))
    limpar_tela()

def saida():
    limpar_tela()
    for palavra in range(0,3):
        print('Saindo do programa',end='',flush=True)
        for ponto in range(0,3):
            print('.',end='',flush=True)
            sleep(1.3)
        limpar_tela()
    print('Saindo do programa...')
    print('\nPrograma encerrado!')
            
estoque = []

while True:
    mostrar_menu()
    opcoes = input('Escolha uma opção: ')
    while opcoes not in ('1', '2', '3', '4'):
        print('Valor incorreto! TENTE NOVAMENTE')
        opcoes = input('\nEscolha uma opção: ')

    if opcoes == '1':
        adicionar_produto()
    elif opcoes == '2':
        consultar_produto()
                
    elif opcoes == '3':
        remover_produto()
    else:
        saida()
        break

        


