import tkinter.messagebox
from tkinter import messagebox
import moduloMain
import customtkinter


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

moduloMain.msgBoasVindas()
nome = input('Digite o seu nome aqui ')
moduloMain.msgPersonalizada(nome)


def menssagem():
    tkinter.messagebox.showinfo("Olá Querido Usuário","Deseja realmente sair?0")


    # Criação de caixa de entrada
    txtnome =customtkinter.CTkEntry(app, bd=2, font=("Calibri, 11"))
    txtnome.place(relx=0.5, rely=0.5, anchor = tkinter.CENTER)


    # Label nome do Console
    lblfabricante = customtkinter.CTkLabel(
        app,
        text="Fabricante:",
        font="Calibri, 15",
        bd=0,
        relief="solid",
        width=50,
        height=1,

        justify=LEFT  # Alinhamento do texto
    ).place(relx=0.5, rely=0.5,anchor=CENTER)



app.mainloop()