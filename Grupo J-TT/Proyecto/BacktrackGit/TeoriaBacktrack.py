import tkinter as tk
from tkinter import ttk
from tkinter import *
from BacktrackGit.EvaluacionBacktrack import Evaluacion
class TeoriaBacktrack():
    def __init__(self,ventana,temas):
            self.ventanaTeoria=ventana#Aqui se hace una instancia de la ventana teoria que se paso vacia como parametro
            self.VT=temas#Aqui se hace una instancia de la ventana Temas que se paso como parametro
            self.ventanaTeoria.geometry("700x500")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
            self.ventanaTeoria.configure(bg= '#024747')#Se cambia el color del fondo
            self.notebook=ttk.Notebook(ventana)#Dentro de la ventana se crea un notebook para gestionar paneles

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.HeadCommit = PhotoImage(file="BacktrackGit/headcommit.gif")
            self.BacktrackHeadCommit = ttk.Label(ventana,image=self.HeadCommit,background="white")
            self.BacktrackHeadCommit.image = self.HeadCommit
            self.BacktrackHeadCommit.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Checkout = PhotoImage(file="BacktrackGit/checkout.gif")
            self.BacktrackCheckout = ttk.Label(ventana,image=self.Checkout,background="white")
            self.BacktrackCheckout.image = self.Checkout
            self.BacktrackCheckout.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Add = PhotoImage(file="BacktrackGit/add.gif")
            self.BacktrackAdd = ttk.Label(ventana,image=self.Add,background="white")
            self.BacktrackAdd.image = self.Add
            self.BacktrackAdd.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Reset1 = PhotoImage(file="BacktrackGit/reset1.gif")
            self.BacktrackReset1 = ttk.Label(ventana,image=self.Reset1,background="white")
            self.BacktrackReset1.image = self.Reset1
            self.BacktrackReset1.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Reset2 = PhotoImage(file="BacktrackGit/reset2.gif")
            self.BacktrackReset2 = ttk.Label(ventana,image=self.Reset2,background="white")
            self.BacktrackReset2.image = self.Reset2
            self.BacktrackReset2.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.ResetResumen = PhotoImage(file="BacktrackGit/resetResumen.gif")
            self.BacktrackResetResumen = ttk.Label(ventana,image=self.ResetResumen,background="white")
            self.BacktrackResetResumen.image = self.ResetResumen
            self.BacktrackResetResumen.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Resumen = PhotoImage(file="BacktrackGit/Resumen.gif")
            self.BacktrackResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.BacktrackResumen.image = self.Resumen
            self.BacktrackResumen.place(x=0,y=0)

            #Se crean dos botones, uno para crear la ventana con las preguntas y el otro para volver atras
            self.btnEvaluacion = Button(ventana,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(ventana, text='Volver',command=self.Volver).pack(side=BOTTOM)

            #Se añaden como pestañas en el notebook los labels con las imagenes ya cargadas
            self.notebook.add(self.BacktrackHeadCommit,text="Pag 1")
            self.notebook.add(self.BacktrackCheckout,text="Pag 2")
            self.notebook.add(self.BacktrackAdd,text="Pag 3")
            self.notebook.add(self.BacktrackReset1,text="Pag 4")
            self.notebook.add(self.BacktrackReset2,text="Pag 5")
            self.notebook.add(self.BacktrackResetResumen,text="Pag 6")
            self.notebook.add(self.BacktrackResumen,text="Pag 7")
            self.notebook.pack()

    def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaTeoria.destroy()#Y lo que hace es cerrar la ventana Teoria y 
        self.VT.deiconify()# reabrir la ventana anterior, en este caso la ventana principal.

    def Evaluacion(self):# Esta funcion es llamada cuando se aprieta el boton Evaluacion de conceptos
        eva=Evaluacion(self.ventanaTeoria)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con las preguntas del tema elegido