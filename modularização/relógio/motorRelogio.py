from tkinter import *
import tkinter
from datetime import datetime

#=================Palheta de cores================
preto = "#3d3d3d"
branca = "#fafcff"
verde = "#21c25c"
vermelha = "#eb463b"
cinza = "#dedcdc"
azul = "#3080f0"
#==========================

realTime = datetime.now()
hora = realTime.strftime("%H:%M:%S")
diaSemana = realTime.strftime("%A")
dia = realTime.day
mes = realTime.strftime("%B")
ano = realTime.strftime("%Y")

#Teste de prints
""" 
print(realTime)
print(hora)
print(diaSemana)
print(dia)
print(mes)
print(ano)
"""



