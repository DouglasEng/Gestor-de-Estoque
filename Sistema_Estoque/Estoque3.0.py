import tkinter as tk
from tkinter import messagebox

class SistemaEstoque:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Sistema de Estoque')
        self.janela.geometry('500x400+100+40')
        self.janela.maxsize(500,400)
        self.janela.minsize(500,400)
        self.janela['bg'] = '#2E2E2E'

        self.estoque = []

        self.label_titulo = tk.Label(text='Sistema de Estoque', font=('Impact',30), bg='#2E2E2E' , fg='White', width=100)
        self.label_titulo.pack(pady='0') 

        self.but_adicionar = tk.Button(text='Adicionar', font=('Impact',18), bg='Red', fg='White', width=50, cursor='Hand2', border=10, command=self.adicao)
        self.but_adicionar.pack(pady=10)

        self.but_listar = tk.Button(text='Listar', font=('Impact',18), bg='Red', fg='White', width=50, cursor='Hand2', border=10, command=self.listar)
        self.but_listar.pack(pady=10)

        self.but_remover = tk.Button(text='Remover', font=('Impact',18), bg='Red', fg='White', width=50, cursor='Hand2', border=10, command=self.remover)
        self.but_remover.pack(pady=10)

        self.but_sair = tk.Button(text='Sair', font=('Impact',18), bg='Red', fg='White', width=50, cursor='Hand2', border=10, command=self.sair)
        self.but_sair.pack(pady=10)

    def adicao(self):
        print(self.estoque)
        JanelaAdicionar(self.estoque)
    def listar(self):
        JanelaListar(self.estoque)

    def remover(self):
        JanelaRemover(self.estoque)
    
    def sair(self):
        janela.destroy()

class JanelaAdicionar:
    def __init__(self, estoque):
        self.estoque = estoque
        self.janela_adicionar = tk.Toplevel()
        self.janela_adicionar.title('Adicionar')
        self.janela_adicionar.geometry('240x300+640+40')
        self.janela_adicionar.minsize(240,300)
        self.janela_adicionar.maxsize(240,300)
        self.janela_adicionar['bg'] = '#2E2E2E'

        self.rotulo_titulo = tk.Label(self.janela_adicionar, text='Adicionar Produto', font=('Impact',20), bg='#2E2E2E', fg='#FFD700')
        self.rotulo_titulo.grid(row=0, column=0, columnspan=3, pady=20)

        self.rotulo_produto = tk.Label(self.janela_adicionar, text='Produto:', font=('Impact',14), bg='#2E2E2E',fg='White')
        self.rotulo_produto.grid(row=1,column=0)

        self.entrada_produto = tk.Entry(self.janela_adicionar)
        self.entrada_produto.grid(row=1,column=2, pady=20)

        self.rotulo_quantidade = tk.Label(self.janela_adicionar, text='Quantidade:', font=('Impact',14), bg='#2E2E2E',fg='White')
        self.rotulo_quantidade.grid(row=2,column=0)

        self.entrada_quantidade = tk.Entry(self.janela_adicionar, border=2, justify='center', cursor='Hand2', )
        self.entrada_quantidade.grid(row=2,column=2, pady=10)

        self.botao_confirmar = tk.Button(self.janela_adicionar, text='Confirmar', font=('Impact',18), bg='red', border=10, command=self.adicionar)
        self.botao_confirmar.grid(row=3, column=0, columnspan=3, pady=50)

    def adicionar(self):
        produto = self.entrada_produto.get()
        quantidade = self.entrada_quantidade.get()

        if quantidade.isnumeric():
            quantidade = int(quantidade)
            produto_existe = False
            for produtos in self.estoque:
                if produtos[0] == produto:
                    produtos[1] += quantidade  
                    messagebox.showinfo('Informação', f'{quantidade} de {produto} foram cadastrados.' )

                    produto_existe = True
                    break

            if not produto_existe:
                self.estoque.append([produto, quantidade])
                messagebox.showinfo('Informação', f'{quantidade} de {produto} foram cadastrados.' )
                print('Produto cadastrado com sucesso!')
            self.janela_adicionar.destroy()
        else:
            messagebox.showerror('Erro','Valor de quantidade incorreto!')
        self.janela_adicionar.destroy()

class JanelaListar():
    def __init__(self, estoque):
        def sair():
            self.janela_listar.destroy()

        self.estoque = estoque
        self.janela_listar = tk.Toplevel()
        self.janela_listar.title('Listagem')
        self.janela_listar.geometry('300x700+640+40')
        self.janela_listar.maxsize(300,700)
        self.janela_listar.minsize(300,700)
        self.janela_listar['bg'] = '#2E2E2E'

        if len(self.estoque) == 0:
            self.rotulo_titulo = tk.Label(self.janela_listar, text='Estoque Vázio', font=('Impact', 24), bg='#2e2e2e', fg='#FFD700')
            self.rotulo_titulo.grid(row=0, column=0, columnspan=3, pady=30)

        else:
            self.rotulo_titulo = tk.Label(self.janela_listar, text='Listagem de Produtos', font=('Impact', 24), bg='#2e2e2e', fg='#FFD700')
            self.rotulo_titulo.grid(row=0, column=0, columnspan=3, pady=30)

            self.rotulo_indice = tk.Label(self.janela_listar, text='Indice  ', font=('Impact', 17), bg='#2e2e2e', fg='#FFD700')
            self.rotulo_indice.grid(row=1,column=0)

            self.rotulo_produto = tk.Label(self.janela_listar, text='Produto  ', font=('Impact', 17), bg='#2e2e2e', fg='#FFD700')
            self.rotulo_produto.grid(row=1, column=1)

            self.rotulo_quantidade = tk.Label(self.janela_listar, text='Quantidade', font=('Impact', 17), bg='#2e2e2e', fg='#FFD700')
            self.rotulo_quantidade.grid(row=1,column=2)

            for indice, produto in enumerate(self.estoque, start=1):
                self.valor_indice = tk.Label(self.janela_listar, text=indice, font=('Impact', 15), bg='#2e2e2e', fg='white')
                self.valor_indice.grid(row=indice+2,column=0)
                
                self.valor_produto = tk.Label(self.janela_listar, text=produto[0], font=('Impact', 15), bg='#2e2e2e', fg='white')
                self.valor_produto.grid(row=indice+2,column=1)

                self.valor_quantidade = tk.Label(self.janela_listar, text=produto[1], font=('Impact', 15), bg='#2e2e2e', fg='white')
                self.valor_quantidade.grid(row=indice+2,column=2)

        self.but_sair = tk.Button(self.janela_listar,text='Sair', font=('Impact',18), bg='red', border=10, fg='White', width=7, command=sair)
        self.but_sair.grid(row=144, column=0,columnspan=3)

class JanelaRemover():

    def __init__(self, estoque):

        self.estoque = estoque

        self.janela_remover = tk.Toplevel()
        self.janela_remover.title('Remover')
        self.janela_remover.geometry('360x700+640+40')
        self.janela_remover.maxsize(360,700)
        self.janela_remover.minsize(360,700)
        self.janela_remover['bg'] = '#2e2e2e'

        if len(self.estoque) == 0:
            self.rotulo_titulo = tk.Label(self.janela_remover, text='Estoque Vázio', font=('Impact', 24), bg='#2e2e2e', fg='#FFD700')
            self.rotulo_titulo.grid(row=0, column=0, columnspan=3, pady=30)

        else:
            self.rotulo_titulo = tk.Label(self.janela_remover, text='Listagem de Produtos', font=('Impact', 24), bg='#2e2e2e', fg='#FFD700')
            self.rotulo_titulo.grid(row=0, column=0, columnspan=3, pady=30)

            self.rotulo_indice = tk.Label(self.janela_remover, text='Indice  ', font=('Impact', 17), bg='#2e2e2e', fg='#FFD700')
            self.rotulo_indice.grid(row=1,column=0)

            self.rotulo_produto = tk.Label(self.janela_remover, text='Produto  ', font=('Impact', 17), bg='#2e2e2e', fg='#FFD700')
            self.rotulo_produto.grid(row=1, column=1)

            self.rotulo_quantidade = tk.Label(self.janela_remover, text='Quantidade', font=('Impact', 17), bg='#2e2e2e', fg='#FFD700')
            self.rotulo_quantidade.grid(row=1,column=2)

            for indice, produto in enumerate(self.estoque, start=1):
                self.valor_indice = tk.Label(self.janela_remover, text=indice, font=('Impact', 15), bg='#2e2e2e', fg='white')
                self.valor_indice.grid(row=indice+2,column=0)
                
                self.valor_produto = tk.Label(self.janela_remover, text=produto[0], font=('Impact', 15), bg='#2e2e2e', fg='white')
                self.valor_produto.grid(row=indice+2,column=1)

                self.valor_quantidade = tk.Label(self.janela_remover, text=produto[1], font=('Impact', 15), bg='#2e2e2e', fg='white')
                self.valor_quantidade.grid(row=indice+2,column=2)

            self.rotulo_nome = tk.Label(self.janela_remover, text='Indice', font=('Impact', 18), bg='#2e2e2e', fg='White')
            self.rotulo_nome.grid(row=len(estoque)+3, column=0,pady=30)

            self.entrada_nome = tk.Entry(self.janela_remover)
            self.entrada_nome.grid(row=len(estoque)+3,column=2,pady=30)

            self.rotulo_quantidade = tk.Label(self.janela_remover, text='Quantidade', font=('Impact', 18), bg='#2e2e2e', fg='White')
            self.rotulo_quantidade.grid(row=len(estoque)+4, column=0)

            self.entrada_quantidade = tk.Entry(self.janela_remover)
            self.entrada_quantidade.grid(row=len(estoque)+4,column=2)

            self.but_confirmar = tk.Button(self.janela_remover,text='Confirmar', font=('Impact',18), bg='red', border=10, fg='White', width=7, command=self.confirmar)
            self.but_confirmar.grid(row=len(estoque)+5, column=0,columnspan=3,pady=30)
    def confirmar(self):
            try:
                indice = int(self.entrada_nome.get()) 
                quantidade = int(self.entrada_quantidade.get()) 

                if indice <= 0 or indice > len(self.estoque):
                    messagebox.showerror('Erro', 'Valor de índice inválido!')
                else:
                    if quantidade > self.estoque[indice - 1][1]:
                        messagebox.showerror('Erro', 'Valor de remoção maior que de estoque')
                    elif quantidade == self.estoque[indice - 1][1]:
                        self.estoque.pop(indice - 1)
                        messagebox.showinfo('Aviso', 'Produto Removido!')
                    else:
                        self.estoque[indice - 1][1] -= quantidade
                        messagebox.showinfo('Aviso', f'Foi removido {quantidade} de {self.estoque[indice - 1][0]}, restando {self.estoque[indice - 1][1]}')
            except ValueError:
                messagebox.showerror('Erro', 'Dados inválidos! Verifique os campos e tente novamente.')
            self.janela_remover.destroy()

janela = tk.Tk()
SistemaEstoque(janela)
janela.mainloop()