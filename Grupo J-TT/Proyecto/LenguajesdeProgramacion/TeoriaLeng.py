import tkinter as tk
from tkinter import ttk
from tkinter import *
from LenguajesdeProgramacion.EvaluacionLeng import Evaluacion
class TeoriaLeng():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana#Aqui se hace una instancia de la ventana teoria que se paso vacia como parametro
            self.ventanaTeoria.geometry("680x570")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
            self.ventanaTeoria.configure(bg= '#024747')#Se cambia el color del fondo
            self.VT=Temas#Aqui se hace una instancia de la ventana Temas que se paso como parametro
            self.notebook=ttk.Notebook(ventana)#Dentro de la ventana se crea un notebook para gestionar paneles

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Definicion = PhotoImage(file="LenguajesdeProgramacion/DefinicionLenguaje.gif")
            self.LengDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.LengDefinicion.image = self.Definicion
            self.LengDefinicion.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Procesadores = PhotoImage(file="LenguajesdeProgramacion/Procesadores.gif")
            self.LengProcesadores = ttk.Label(ventana,image=self.Procesadores,background="white")
            self.LengProcesadores.image = self.Procesadores
            self.LengProcesadores.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Traduccion1 = PhotoImage(file="LenguajesdeProgramacion/TraduccionALenguajeMaquina1.gif")
            self.LengTraduccion1 = ttk.Label(ventana,image=self.Traduccion1,background="white")
            self.LengTraduccion1.image = self.Traduccion1
            self.LengTraduccion1.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Traduccion2 = PhotoImage(file="LenguajesdeProgramacion/TraduccionALenguajeMaquina2.gif")
            self.LengTraduccion2 = ttk.Label(ventana,image=self.Traduccion2,background="white")
            self.LengTraduccion2.image = self.Traduccion2
            self.LengTraduccion2.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Resumen = PhotoImage(file="LenguajesdeProgramacion/Resumen.gif")
            self.LengResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.LengResumen.image = self.Resumen
            self.LengResumen.place(x=0,y=0)
            
            #Se crean dos botones, uno para crear la ventana con las preguntas y el otro para volver atras
            self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)
            
            #Se añaden como pestañas en el notebook los labels con las imagenes ya cargadas
            self.notebook.add(self.LengDefinicion,text="Pag 1")
            self.notebook.add(self.LengProcesadores,text="Pag 2")
            self.notebook.add(self.LengTraduccion1,text="Pag 3")
            self.notebook.add(self.LengTraduccion2,text="Pag 4")
            self.notebook.add(self.LengResumen,text="Pag 5")
            self.notebook.pack()

    def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaTeoria.destroy()#Y lo que hace es cerrar la ventana Teoria y
        self.VT.deiconify()# reabrir la ventana anterior, en este caso la ventana principal.

    def Evaluacion(self):# Esta funcion es llamada cuando se aprieta el boton Evaluacion de conceptos
         VentanaEva=Evaluacion(self.ventanaTeoria)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con las preguntas del tema elegido