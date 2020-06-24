import tkinter as tk
from tkinter import ttk
from tkinter import *
from Algoritmos.EvaluacionAlg import Evaluacion
class TeoriaAlg():

    def __init__(self,ventana,temas):
            self.ventanaTeoria=ventana#Aqui se hace una instancia de la ventana teoria que se paso vacia como parametro
            self.VT=temas#Aqui se hace una instancia de la ventana Temas que se paso como parametro
            self.ventanaTeoria.geometry("800x450")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
            #Se cambia el color del fondo
            self.notebook=ttk.Notebook(ventana)#Dentro de la ventana se crea un notebook para gestionar paneles

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Definicion = PhotoImage(file="Algoritmos/Definicion.gif")
            self.AlgDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.AlgDefinicion.image = self.Definicion
            self.AlgDefinicion.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Tipos = PhotoImage(file="Algoritmos/Tipos.gif")
            self.AlgTipos = ttk.Label(ventana,image=self.Tipos,background="white")
            self.AlgTipos.image = self.Tipos
            self.AlgTipos.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Tecnicas1 = PhotoImage(file="Algoritmos/TecnicasDiseño1.gif")
            self.AlgTecnicas1 = ttk.Label(ventana,image=self.Tecnicas1,background="white")
            self.AlgTecnicas1.image = self.Tecnicas1
            self.AlgTecnicas1.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Tecnicas2 = PhotoImage(file="Algoritmos/TecnicasDiseño2.gif")
            self.AlgTecnicas2 = ttk.Label(ventana,image=self.Tecnicas2,background="white")
            self.AlgTecnicas2.image = self.Tecnicas2
            self.AlgTecnicas2.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Representacion = PhotoImage(file="Algoritmos/Representacion.gif")
            self.AlgRepresentacion = ttk.Label(ventana,image=self.Representacion,background="white")
            self.AlgRepresentacion.image = self.Representacion
            self.AlgRepresentacion.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Resumen = PhotoImage(file="Algoritmos/Resumen.gif")
            self.AlgResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.AlgResumen.image = self.Resumen
            self.AlgResumen.place(x=0,y=0)

            #Se crean dos botones, uno para crear la ventana con las preguntas y el otro para volver atras
            self.btnEvaluacion = Button(ventana,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(ventana, text='Volver',command=self.Volver).pack(side=BOTTOM)

            #Se añaden como pestañas en el notebook los labels con las imagenes ya cargadas
            self.notebook.add(self.AlgDefinicion,text="Pag 1")
            self.notebook.add(self.AlgTipos,text="Pag 2")
            self.notebook.add(self.AlgTecnicas1,text="Pag 3")
            self.notebook.add(self.AlgTecnicas2,text="Pag 4")
            self.notebook.add(self.AlgRepresentacion,text="Pag 5")
            self.notebook.add(self.AlgResumen,text="Pag 6")
            self.notebook.pack()

    def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaTeoria.destroy()#Y lo que hace es cerrar la ventana Teoria y 
        self.VT.deiconify()# reabrir la ventana anterior, en este caso la ventana temas.

    def Evaluacion(self):# Esta funcion es llamada cuando se aprieta el boton Evaluacion de conceptos
        VentanaEva=Evaluacion(self.ventanaTeoria)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con las preguntas del tema elegido