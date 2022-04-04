from cProfile import label
from cgitb import text
import random
from string import hexdigits
from telnetlib import ENCRYPT
from tkinter import *
import tkinter as tk
from tkinter import ttk
import binascii
import hashlib
import base64
from turtle import bgcolor, width
from webbrowser import get
from pyDes import *
import pyDes,base64

from setuptools import Command

hexadecimal="0123456789ABCDEF0123456789ABCDEF"
longitud= 16

def cadena1():
    aleatorio1 = random.sample(hexadecimal, longitud)
    aleatorio_hexa1 = "".join(aleatorio1)
    print(f'valor 1 : {aleatorio_hexa1}') 
    return aleatorio_hexa1 
    
def cadena2():
    aleatorio2 = random.sample(hexadecimal, longitud)
    aleatorio_hexa2 = "".join(aleatorio2)
    print(f'valor 2 : {aleatorio_hexa2}')
    return aleatorio_hexa2

def cadena3():
    aleatorio3 = random.sample(hexadecimal, longitud)
    aleatorio_hexa3 = "".join(aleatorio3)
    print(f'valor 3 : {aleatorio_hexa3}')
    return aleatorio_hexa3
    

text1 = cadena1()
text2 = cadena2()
text3 = cadena3()


ws = Tk()
ws.title('Programa_de_Criptografia')
ws.geometry('600x600')
Frame= Frame()
Frame.pack()
titulo = Label(Frame, text="GENERACIÓN DE NUMEROS HEXADECIMAL")
titulo.grid(row=0, column=0)
titulo.config(font=('Arial', 15))
titulo.grid(row=0, column=0)
titulo.config(font=('Arial', 15))


k1 = pyDes.triple_des(text1,padmode=pyDes.PAD_PKCS5)
kcv1 = k1.encrypt(text1)

print('KCV: ' + str(binascii.hexlify(kcv1)[0:6]))


#caja
caja1 = ttk.Entry(justify=tk.LEFT,show="")
caja1.place(x=200, y=80)
caja1.insert(0,text1)

caja2 = ttk.Entry(justify=tk.LEFT,show="")
caja2.place(x=200, y=160)
caja2.insert(0,text2)

caja3 = ttk.Entry(justify=tk.LEFT,show="")
caja3.place(x=200, y=240)
caja3.insert(0,text3)

def clean():
    caja1 = caja1.insert('')


boton1 = ttk.Button(text="GENERAR", command=[cadena1,cadena2,cadena3])
boton1.place(x=200, y =350)


boton = ttk.Button(text="SUMAR")
boton.place(x=300, y =350)

caja1 = ttk.Entry(justify=tk.LEFT,show="")
caja1.place(x=200, y=400)
caja1.insert(0,k1)

ws.mainloop()


