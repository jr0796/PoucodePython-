
from motorRelogio import *
import tkinter
from tkinter import messagebox
from datetime import datetime
import customtkinter
import pyglet

pyglet.font.add_file("DS-DIGIB.TTF")
# Esse estilo talvez não reconhça a fonte alterada (DS-DIGIB)

#=================Palheta de cores================
preto = "#3d3d3d"
branca = "#fafcff"
verde = "#21c25c"
vermelha = "#eb463b"
cinza = "#dedcdc"
azul = "#3080f0"
#==========================


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")
app.title("..:: Relógio ::..")
app.configure(bg=branca, fg_color=preto)
app.resizable(width=False, height=False)

def relogio():

    realTime = datetime.now() # Data e hora atual do sistema.
    hora = realTime.strftime("%H:%M:%S")

    lblRelogio.configure(text=hora,text_color="blue")
    lblDiaMesAno.configure(text=f"{diaSemana} - {dia}/{mes}/{ano}")
    lblRelogio.after(200, relogio) #Atraso de 200 mile Segundos

# Label Dia da Semana, Dia Mês e Ano
lblDiaMesAno=customtkinter.CTkLabel(master=app,height=1,width=50,font=("DS-DIGIB", 20),text=" ---",anchor=tkinter.CENTER)
lblDiaMesAno.place(relx=0.01, rely=0.1)


# Label Relógio
lblRelogio=customtkinter.CTkLabel(master=app,height=1,width=50,font=("DS-DIGIB", 90),text="00:00:00 ",anchor=tkinter.CENTER)
lblRelogio.place(relx=0.03, rely=0.2)

relogio()

app.mainloop()