import tkinter as tk
from tkinter import messagebox

def root_adicionar():
    def adicionar():
        produto = inp_produto.get()
        quantidade = inp_quantidade.get()

        if (quantidade.isnumeric()) == True:
            quantidade = int(quantidade)
            produto_existe = False
            for produtos in estoque:
                if produtos[0] == produto:
                    produtos[1] += quantidade  
                    produto_existe = True
                    break

            if not produto_existe:
                estoque.append([produto, quantidade])
                messagebox.showwarning('Cadastro Realizado', 'Produto cadastrado com sucesso')
        else:
            messagebox.showerror('Erro', 'A quantidade deve ser um numero valido.')

        janela_adicionar.destroy()

    janela_adicionar = tk.Toplevel()
    janela_adicionar.title('Adicionar Produtos')
    janela_adicionar.geometry('400x500+500+40')
    janela_adicionar.maxsize(300,500)
    janela_adicionar.minsize(300,500)
    janela_adicionar['bg'] = 'Gray'

    msg_produto = tk.Label(janela_adicionar, text='Produto', font=('Impact',28), fg='White', bg='Gray')

    inp_produto = tk.Entry(janela_adicionar, justify='center', highlightcolor="#007acc",highlightbackground="#cccccc",highlightthickness=2, width=40,)

    msg_quantidade = tk.Label(janela_adicionar, text='Quantidade', font=('Impact',28), fg='White', bg='Gray')

    inp_quantidade = tk.Entry(janela_adicionar, justify='center', highlightcolor="#007acc",highlightbackground="#cccccc",highlightthickness=2, width=40)

    bot_confirmar = tk.Button(janela_adicionar, text='Confirmar', font=('Impact', 13), bg='red', fg='white', cursor='hand2', border=5, width=20, command=adicionar)


    msg_produto.grid(row=0, column=0, columnspan=2, pady=10)
    inp_produto.grid(row=1, column=0, columnspan=2, padx=20, pady=10)
    msg_quantidade.grid(row=2, column=0, columnspan=2, pady=10)
    inp_quantidade.grid(row=3, column=0, columnspan=2, padx=20, pady=10)
    bot_confirmar.grid(row=4, column=0, columnspan=2, pady=20)



    janela_adicionar.mainloop()

def listar():
    janela_listar = tk.Toplevel()
    janela_listar.title('Listagem Produtos')
    janela_listar.geometry('400x500+500+40')
    janela_listar.maxsize(400,1000)
    janela_listar.minsize(400,500)
    janela_listar['bg'] = 'Gray'


    if len(estoque) == 0:
        msg_vazio = tk.Label(janela_listar, text='ESTOQUE VÁZIO', font=('Impact', 26), bg='Gray', fg='White')
        msg_vazio.grid(column=0, row=1, columnspan=2, pady=20)
    
    else:
        msg_titulo_lista = tk.Label(janela_listar, text='Listagem de Estoque', font=('Impact', 26), bg='Gray', fg='White')
        msg_titulo_lista.grid(column=0, row=1, columnspan=2, pady=20)
        for indice, produtos in enumerate(estoque):
            produto = tk.Label(janela_listar, text=(f'{indice+1:>5} {produtos[0]:>30} {produtos[1]:>10}'), font=('Impact',14), bg='Gray', fg='White')
            produto.grid(column=0, row=indice+4)

    janela_listar.mainloop()

def remover():
    janela_remover = tk.Toplevel()
    janela_remover.geometry('400x500+500+40')
    janela_remover.maxsize(400,1000)
    janela_remover.minsize(400,500)
    janela_remover.title('Remover Produto')
    janela_remover['bg'] = 'gray'


    if len(estoque) == 0:
        msg_vazio = tk.Label(janela_remover, text='ESTOQUE VÁZIO', font=('Impact', 26), bg='Gray', fg='White')
        msg_vazio.place(x=95, y=20)
    else:
        msg_titulo_lista = tk.Label(janela_remover, text='Listagem de Estoque', font=('Impact', 26), bg='Gray', fg='White')
        msg_titulo_lista.place(x=50, y=20)

        ultimo_y = 0
        for indice, produtos in enumerate(estoque):
            produto = tk.Label(janela_remover, text=(f'{indice+1:>5} {produtos[0]:>40} {produtos[1]:>10}'), font=('Impact',14), bg='Gray', fg='White')
            produto.place(x=45, y=100 + (indice * 30))
            ultimo_y = 100+(indice*30)

        msg_indie_produto = tk.Label(janela_remover, text='Indice do Produto', font=('Impact', 26), bg='Gray', fg='White')
        msg_indie_produto.place(x= 70, y=ultimo_y+100)

        inp_indice_produto = tk.Entry(janela_remover, width=47, cursor='hand2', border=5, justify='center')
        inp_indice_produto.place(x = 47 , y= ultimo_y+150)

        but_confirmar = tk.Button(janela_remover, border= 5, text='Confirmar', bg='Red', fg='White', width=26, font=('Impact', 17), cursor='Hand2')
        but_confirmar.place(x= 47, y= ultimo_y+200)

    janela.mainloop()

def sair():
    janela.destroy()



estoque = []
janela = tk.Tk()
janela.title('Estoque')
janela.geometry('400x400+100+50')
janela.maxsize(400,400)
janela.minsize(400,400)
janela['bg'] = 'gray'

msg_titulo = tk.Label(janela, text='Sistema de Estoque', font=('Impact', 35), bg='Gray', fg='White')
msg_titulo.pack()

but_adicionar = tk.Button(janela, text='Adicionar', border=7, font=('Impact',20), width=100, height=1, bg='Red', cursor='Hand2', command=root_adicionar, fg='White')
but_adicionar.pack(pady=5)

but_listar = tk.Button(janela, text='Listar', border=7, font=('Impact',20), width=100, height=1,bg='Red', cursor='Hand2', command=listar, fg='White')
but_listar.pack(pady=5)

but_remover = tk.Button(janela, text='Remover', border=7, font=('Impact',20), width=100, bg='Red', cursor='Hand2', command=remover,fg='White')
but_remover.pack(pady=5)

but_sair = tk.Button(janela, text='Sair', border=7, font=('Impact',20), width=100, bg='Red', cursor='Hand2', command=sair, fg='White')
but_sair.pack(pady=5)



janela.mainloop()