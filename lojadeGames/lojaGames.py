import tkinter as TK
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import pyodbc

janela = Tk()
janela.title("Loja de Games ")
janela.geometry("500x400")


#Conexão com banco SQL
conexao = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-T3K0RN5;PORT=1433;Database=bdLojaGames;Trusted_connection = yes')
print("Conexão bem sucedida!!")

cursor = conexao.cursor()



def janelaConsole():
    janela02 = Toplevel()
    janela02.title = ('Cadastro de COnsole')
    janela02.grab_set()  # desabilita a janela anterior
    janela02.focus_set()  # Coloca o focu na janela aberta.
    janela02.geometry("300x300")

    def cadastroConsole():
        console = txtnomeConsole.get()
        fabricante = txtfabricante.get()

        comando = f"""INSERT INTO tbConsole (nomeConsole, nomeFabricante)
                    VALUES ('{console}','{fabricante}')"""
        cursor.execute(comando)
        cursor.commit()
        limpar()
        print('Dados cadastrados com sucesso!')
        messagebox.showinfo("Cadastro", "Dados cadastrados com Sucesso!")

    def limpar():
        txtnomeConsole .delete(0, "end")
        txtfabricante.delete(0, "end")
        txtnomeConsole.focus_set()

    def cancelarSair():
        resp = messagebox.askyesno("Cancelar e sair", 'Deseja realmente sair?')
        if resp == True:
            janela02.destroy()


    #Label nome do Console
    lblNomeConsole = Label(
        janela02,
        text= "Nome do console:",
        font = "Calibri, 15",
        bd=0,
        relief = "solid",
        width = 50,
        height=1,
        anchor=NW,
        justify=LEFT #Alinhamento do texto
    ).place(x=4, y=10)

    # Criação de caixa de entrada
    txtnomeConsole = Entry(janela02, bd=2, font=("Calibri, 11"), justify=LEFT)
    txtnomeConsole.place(width=260, height=25, x=4, y=40)

    # Label nome do Console
    lblfabricante = Label(
        janela02,
        text="Fabricante:",
        font="Calibri, 15",
        bd=0,
        relief="solid",
        width=50,
        height=1,
        anchor=NW,
        justify=LEFT  # Alinhamento do texto
    ).place(x=4, y=90)

    # Criação de caixa de entrada
    txtfabricante = Entry(janela02, bd=2, font="Calibri, 11", justify=LEFT)
    txtfabricante.place(width=260, height=25, x=4, y=120)


    # botão Confirmar
    btnConfirmar02 = Button(janela02, text='Cadastrar', font="Calibre, 15", command=cadastroConsole)
    btnConfirmar02.pack(side='top')
    btnConfirmar02.place(width=120, height=45, x=140, y=170)

    # botão Cancelar
    btnCancelar02 = Button(janela02, text='Cancelar', font="Calibre, 15", command=cancelarSair)
    btnCancelar02.pack(side='top')
    btnCancelar02.place(width=120, height=45, x=30, y=170)

#Label título
lblTitulo = Label(
    janela,
    text= "Loja de Games  ",
    font = "Calibri, 15",
    bd=0,
    relief = "solid",
    width = 50,
    height=1,
    anchor=NW,
    justify=LEFT #Alinhamento do texto

).place(x=4, y=10)





lblfabricante = Label(
    janela,
    text="Fabricante",
    font="Calibri, 11",
    bd=0,
    relief="solid",
    width=50,
    height=1,
    anchor=NW,
    justify=LEFT
).place(x=4, y=120)

"""

"""



text_box = Text(janela, bd=2, font=("Calibri, 14"))
text_box.place(height=205, width=202, x=4, y=70)

#combo Console
campoSelecionado = TK.StringVar()
combo = ttk.Combobox(janela, width=30, textvariable=(campoSelecionado))
combo.place(x=220, y=120)
combo['values'] = ('Switch')
combo.current()

#combo Jogo
campoSelect = TK.StringVar()
comboGame = ttk.Combobox(janela, width=30, textvariable=campoSelect)
comboGame.place(x=220, y=160)
comboGame['values'] = ('God Of War','Super Mario','Car')
comboGame['state'] = 'readonly'

#Console
btnConsole = Button(janela, text='Console + ',font=("Calibri, 15"), command=janelaConsole) #Função deve ser criada antes
btnConsole.pack(side ='top')
btnConsole.place(width=200, height=35, x=220, y=15)

# Jogos
btnJogo = Button(janela, text='Jogo',font=("Calibri, 15"), command="") #Função deve ser criada antes
btnJogo.pack(side ='top')
btnJogo.place(width=200, height=35, x=220, y=55)


#botão Inserir
btnInserir = Button(janela, text='Inserir',font=("Calibri, 15"), command="")
btnInserir.pack(side ='top')
btnInserir.place(width=120, height=45, x=300, y=190)


#botão Confirmar
btnConfirmar = Button(janela, text='Cadastrar',font=("Calibri, 15"), command="") #Função deve ser criada antes
btnConfirmar.pack(side ='top')
btnConfirmar.place(width=120, height=45, x=220, y=300)

#botão Cancelar
btnCancelar = Button(janela, text='Cancelar',font=("Calibri, 15"), command="")
btnCancelar.pack(side ='top')
btnCancelar.place(width=120, height=45, x=110, y=300)



janela.mainloop()





