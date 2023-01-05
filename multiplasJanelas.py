import tkinter as TK
from tkinter import *
import pyodbc




#Estrutura da Janela
janela = Tk()
janela.title("Multiplas Janelas  ")
janela.geometry("400x300")

def janela1():
    jan1 = TK.Toplevel()
    jan1.title = ("Janela 01")
    jan1.focus_set()  # Coloca o focu na janela aberta.
    jan1.grab_set()  # desabilita a janela anterior

    # Label título
    lblTitulo = Label(
        jan1,
        text="Janela 1 ",
        font="Calibri, 15",
        bd=0,
        relief="solid",
        width=50,
        height=1,
        anchor=NW,
        justify=LEFT  # Alinhamento do texto

    ).place(x=4, y=10)

def janela2():
    jan2 =TK.Toplevel()
    jan2.title=("Janela 02")
    jan2.focus_set() #Coloca o focu na janela aberta.
    jan2.grab_set() #desabilita a janela anterior

    # Label título
    lblTitulo = Label(
        jan2,
        text="Janela 02",
        font="Calibri, 15",
        bd=0,
        relief="solid",
        width=50,
        height=1,
        anchor=NW,
        justify=LEFT  # Alinhamento do texto

    ).place(x=4, y=10)

#botão Janela1
btnjanela1 = Button(janela, text='Janela 1',font=("Calibri, 15"), command=janela1)
btnjanela1.pack(side ='top')
btnjanela1.place(width=120, height=45, x=60, y=40)

#botão Janela2
btnjanela2 = Button(janela, text='Janela 2',font=("Calibri, 15"), command=janela2)
btnjanela2.pack(side ='top')
btnjanela2.place(width=120, height=45, x=60, y=90)




janela.mainloop() #Fim da Janela