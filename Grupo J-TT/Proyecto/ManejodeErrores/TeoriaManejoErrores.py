import tkinter as tk
from tkinter import ttk
from tkinter import *
from ManejodeErrores.EvaluacionManejoErrores import Evaluacion
class TeoriaManejoErrores():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana#Aqui se hace una instancia de la ventana teoria que se paso vacia como parametro
            self.ventanaTeoria.geometry("680x530")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
            self.ventanaTeoria.configure(bg= '#024747')#Se cambia el color del fondo
            self.VT=Temas#Aqui se hace una instancia de la ventana Temas que se paso como parametro
            self.notebook=ttk.Notebook(ventana)#Dentro de la ventana se crea un notebook para gestionar paneles

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Definicion = PhotoImage(file="ManejodeErrores/Definicion.gif")
            self.ManejoDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.ManejoDefinicion.image = self.Definicion
            self.ManejoDefinicion.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Definicion = PhotoImage(file="ManejodeErrores/Definicion.gif")
            self.ValoresRetorEsp = PhotoImage(file="ManejodeErrores/ValoresRetornoEspeciales.gif")
            self.ManejoValoresRetorEsp = ttk.Label(ventana,image=self.ValoresRetorEsp,background="white")
            self.ManejoValoresRetorEsp.image = self.ValoresRetorEsp
            self.ManejoValoresRetorEsp.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Definicion = PhotoImage(file="ManejodeErrores/Definicion.gif")
            self.IndicadoresExplic = PhotoImage(file="ManejodeErrores/IndicadoresExplicitos.gif")
            self.ManejoIndicadoresExplic = ttk.Label(ventana,image=self.IndicadoresExplic,background="white")
            self.ManejoIndicadoresExplic.image = self.IndicadoresExplic
            self.ManejoIndicadoresExplic.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.ManejadorErrores = PhotoImage(file="ManejodeErrores/ManejadorErrores.gif")
            self.ManejoManejadorErrores = ttk.Label(ventana,image=self.ManejadorErrores,background="white")
            self.ManejoManejadorErrores.image = self.ManejadorErrores
            self.ManejoManejadorErrores.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Excepciones1 = PhotoImage(file="ManejodeErrores/Excepciones1.gif")
            self.ManejoExcepciones1 = ttk.Label(ventana,image=self.Excepciones1,background="white")
            self.ManejoExcepciones1.image = self.Excepciones1
            self.ManejoExcepciones1.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Excepciones2 = PhotoImage(file="ManejodeErrores/Excepciones2.gif")
            self.ManejoExcepciones2 = ttk.Label(ventana,image=self.Excepciones2,background="white")
            self.ManejoExcepciones2.image = self.Excepciones2
            self.ManejoExcepciones2.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.ProgSegura = PhotoImage(file="ManejodeErrores/ProgramacionSeguraContraFallos.gif")
            self.ManejoProgSegura = ttk.Label(ventana,image=self.ProgSegura,background="white")
            self.ManejoProgSegura.image = self.ProgSegura
            self.ManejoProgSegura.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Resumen = PhotoImage(file="ManejodeErrores/Resumen.gif")
            self.ManejoResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.ManejoResumen.image = self.Resumen
            self.ManejoResumen.place(x=0,y=0)

            #Se crean dos botones, uno para crear la ventana con las preguntas y el otro para volver atras
            self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)

            #Se añaden como pestañas en el notebook los labels con las imagenes ya cargadas
            self.notebook.add(self.ManejoDefinicion,text="Pag 1")
            self.notebook.add(self.ManejoValoresRetorEsp,text="Pag 2")
            self.notebook.add(self.ManejoIndicadoresExplic,text="Pag 3")
            self.notebook.add(self.ManejoManejadorErrores,text="Pag 4")
            self.notebook.add(self.ManejoExcepciones1,text="Pag 5")
            self.notebook.add(self.ManejoExcepciones2,text="Pag 6")
            self.notebook.add(self.ManejoProgSegura,text="Pag 7")
            self.notebook.add(self.ManejoResumen,text="Pag 8")
            self.notebook.pack()

    def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaTeoria.destroy()#Y lo que hace es cerrar la ventana Teoria y 
        self.VT.deiconify()# reabrir la ventana anterior, en este caso la ventana principal.

    def Evaluacion(self):# Esta funcion es llamada cuando se aprieta el boton Evaluacion de conceptos
         VentanaEva=Evaluacion(self.ventanaTeoria)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con las preguntas del tema elegido.