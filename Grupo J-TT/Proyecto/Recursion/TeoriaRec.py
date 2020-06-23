import tkinter as tk
from tkinter import ttk
from tkinter import *
from Recursion.EvaluacionRec import Evaluacion
class TeoriaRec():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana#Aqui se hace una instancia de la ventana teoria que se paso vacia como parametro
            self.ventanaTeoria.geometry("685x530")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
            self.ventanaTeoria.configure(bg= '#024747')#Se cambia el color del fondo
            self.VT=Temas#Aqui se hace una instancia de la ventana Temas que se paso como parametro
            self.notebook=ttk.Notebook(ventana)#Dentro de la ventana se crea un notebook para gestionar paneles
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Definicion = PhotoImage(file="Recursion/Definicion.gif")
            self.RecDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.RecDefinicion.image = self.Definicion
            self.RecDefinicion.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Ejemplo = PhotoImage(file="Recursion/Ejemplo.gif")
            self.RecEjemplo = ttk.Label(ventana,image=self.Ejemplo,background="white")
            self.RecEjemplo.image = self.Ejemplo
            self.RecEjemplo.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.ErroresComunes = PhotoImage(file="Recursion/ErroresComunes.gif")
            self.RecErroresComunes = ttk.Label(ventana,image=self.ErroresComunes,background="white")
            self.RecErroresComunes.image = self.ErroresComunes
            self.RecErroresComunes.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.RecursionCola = PhotoImage(file="Recursion/RecursionDeCola.gif")
            self.RecRecursionCola = ttk.Label(ventana,image=self.RecursionCola,background="white")
            self.RecRecursionCola.image = self.RecursionCola
            self.RecRecursionCola.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Resumen = PhotoImage(file="Recursion/Resumen.gif")
            self.RecResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.RecResumen.image = self.Resumen
            self.RecResumen.place(x=0,y=0)
            
            #Se crean dos botones, uno para crear la ventana con las preguntas y el otro para volver atras
            self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)
            
            #Se añaden como pestañas en el notebook los labels con las imagenes ya cargadas
            self.notebook.add(self.RecDefinicion,text="Pag 1")
            self.notebook.add(self.RecEjemplo,text="Pag 2")
            self.notebook.add(self.RecRecursionCola,text="Pag 3")
            self.notebook.add(self.RecErroresComunes,text="Pag 4")
            self.notebook.add(self.RecResumen,text="Pag 5")
            self.notebook.pack()

    def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaTeoria.destroy()#Y lo que hace es cerrar la ventana Teoria y
        self.VT.deiconify()# reabrir la ventana anterior, en este caso la ventana principal.

    def Evaluacion(self):# Esta funcion es llamada cuando se aprieta el boton Evaluacion de conceptos
        VentanaEva=Evaluacion(self.ventanaTeoria)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con las preguntas del tema elegido