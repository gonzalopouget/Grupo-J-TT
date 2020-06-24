import tkinter as tk
from tkinter import ttk
from tkinter import *
from BashScripting.EvaluacionBashScript import Evaluacion
class TeoriaBashScript():
    def __init__(self,ventana,temas):
            self.ventanaTeoria=ventana#Aqui se hace una instancia de la ventana teoria que se paso vacia como parametro
            self.VT=temas#Aqui se hace una instancia de la ventana Temas que se paso como parametro
            self.ventanaTeoria.geometry("680x410")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
            self.ventanaTeoria.configure(bg= '#024747')#Se cambia el color del fondo
            self.notebook=ttk.Notebook(ventana)#Dentro de la ventana se crea un notebook para gestionar paneles

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Definicion = PhotoImage(file="BashScripting/Definicion.gif")
            self.BashScriptDef = ttk.Label(ventana,image=self.Definicion,background="white")
            self.BashScriptDef.image = self.Definicion
            self.BashScriptDef.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Variables = PhotoImage(file="BashScripting/variables.gif")
            self.BashScriptVar = ttk.Label(ventana,image=self.Variables,background="white")
            self.BashScriptVar.image = self.Variables
            self.BashScriptVar.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Condicionales1 = PhotoImage(file="BashScripting/condicionales1.gif")
            self.BashScriptCond1 = ttk.Label(ventana,image=self.Condicionales1,background="white")
            self.BashScriptCond1.image = self.Condicionales1
            self.BashScriptCond1.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Condicionales2 = PhotoImage(file="BashScripting/condicionales2.gif")
            self.BashScriptCond2 = ttk.Label(ventana,image=self.Condicionales2,background="white")
            self.BashScriptCond2.image = self.Condicionales2
            self.BashScriptCond2.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Bucles1 = PhotoImage(file="BashScripting/bucles1.gif")
            self.BashScriptBucles1 = ttk.Label(ventana,image=self.Bucles1,background="white")
            self.BashScriptBucles1.image = self.Bucles1
            self.BashScriptBucles1.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Bucles2 = PhotoImage(file="BashScripting/bucles2.gif")
            self.BashScriptBucles2 = ttk.Label(ventana,image=self.Bucles2,background="white")
            self.BashScriptBucles2.image = self.Bucles2
            self.BashScriptBucles2.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Entradas1 = PhotoImage(file="BashScripting/entradas1.gif")
            self.BashScriptEntradas1 = ttk.Label(ventana,image=self.Entradas1,background="white")
            self.BashScriptEntradas1.image = self.Entradas1
            self.BashScriptEntradas1.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Entradas2 = PhotoImage(file="BashScripting/entradas2.gif")
            self.BashScriptEntradas2 = ttk.Label(ventana,image=self.Entradas2,background="white")
            self.BashScriptEntradas2.image = self.Entradas2
            self.BashScriptEntradas2.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Alias = PhotoImage(file="BashScripting/alias.gif")
            self.BashScriptAlias = ttk.Label(ventana,image=self.Alias,background="white")
            self.BashScriptAlias.image = self.Alias
            self.BashScriptAlias.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Resumen = PhotoImage(file="BashScripting/Resumen.gif")
            self.BashScriptResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.BashScriptResumen.image = self.Resumen
            self.BashScriptResumen.place(x=0,y=0)

            #Se crean dos botones, uno para crear la ventana con las preguntas y el otro para volver atras
            self.btnEvaluacion = Button(ventana,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(ventana, text='Volver',command=self.Volver).pack(side=BOTTOM)

            #Se añaden como pestañas en el notebook los labels con las imagenes ya cargadas
            self.notebook.add(self.BashScriptDef,text="Pag 1")
            self.notebook.add(self.BashScriptVar,text="Pag 2")
            self.notebook.add(self.BashScriptCond1,text="Pag 3")
            self.notebook.add(self.BashScriptCond2,text="Pag 4")
            self.notebook.add(self.BashScriptBucles1,text="Pag 5")
            self.notebook.add(self.BashScriptBucles2,text="Pag 6")
            self.notebook.add(self.BashScriptEntradas1,text="Pag 7")
            self.notebook.add(self.BashScriptEntradas2,text="Pag 8")
            self.notebook.add(self.BashScriptAlias,text="Pag 9")
            self.notebook.add(self.BashScriptResumen,text="Pag 10")
            self.notebook.pack()

    def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaTeoria.destroy()#Y lo que hace es cerrar la ventana Teoria y 
        self.VT.deiconify()# reabrir la ventana anterior, en este caso la ventana temas.

    def Evaluacion(self):# Esta funcion es llamada cuando se aprieta el boton Evaluacion de conceptos
        eva=Evaluacion(self.ventanaTeoria)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con las preguntas del tema elegido
