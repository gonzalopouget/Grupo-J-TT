import tkinter as tk
from tkinter import ttk
from tkinter import *
from DatosPrimitivos.EvaluacionDatosPrim import Evaluacion
class TeoriaDatosPrim():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana#Aqui se hace una instancia de la ventana teoria que se paso vacia como parametro
            self.ventanaTeoria.geometry("685x500")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
            self.ventanaTeoria.configure(bg= '#024747')#Se cambia el color del fondo
            self.VT=Temas#Aqui se hace una instancia de la ventana Temas que se paso como parametro
            self.notebook=ttk.Notebook(ventana)#Dentro de la ventana se crea un notebook para gestionar paneles
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Definicion1 = PhotoImage(file="DatosPrimitivos/Definicion1.gif")
            self.DatosPrimDefinicion1 = ttk.Label(ventana,image=self.Definicion1,background="white")
            self.DatosPrimDefinicion1.image = self.Definicion1
            self.DatosPrimDefinicion1.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Definicion2 = PhotoImage(file="DatosPrimitivos/Definicion2.gif")
            self.DatosPrimDefinicion2 = ttk.Label(ventana,image=self.Definicion2,background="white")
            self.DatosPrimDefinicion2.image = self.Definicion2
            self.DatosPrimDefinicion2.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Enteros = PhotoImage(file="DatosPrimitivos/Enteros.gif")
            self.DatosPrimEnteros = ttk.Label(ventana,image=self.Enteros,background="white")
            self.DatosPrimEnteros.image = self.Enteros
            self.DatosPrimEnteros.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Reales = PhotoImage(file="DatosPrimitivos/Reales.gif")
            self.DatosPrimReales = ttk.Label(ventana,image=self.Reales,background="white")
            self.DatosPrimReales.image = self.Reales
            self.DatosPrimReales.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Caracteres = PhotoImage(file="DatosPrimitivos/Caracteres.gif")
            self.DatosPrimCaracteres = ttk.Label(ventana,image=self.Caracteres,background="white")
            self.DatosPrimCaracteres.image = self.Caracteres
            self.DatosPrimCaracteres.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Logicos = PhotoImage(file="DatosPrimitivos/Logicos.gif")
            self.DatosPrimLogicos = ttk.Label(ventana,image=self.Logicos,background="white")
            self.DatosPrimLogicos.image = self.Logicos
            self.DatosPrimLogicos.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Apuntadores = PhotoImage(file="DatosPrimitivos/Apuntadores.gif")
            self.DatosPrimApunt = ttk.Label(ventana,image=self.Apuntadores,background="white")
            self.DatosPrimApunt.image = self.Apuntadores
            self.DatosPrimApunt.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Conversion = PhotoImage(file="DatosPrimitivos/Conversion.gif")
            self.DatosPrimConversion = ttk.Label(ventana,image=self.Conversion,background="white")
            self.DatosPrimConversion.image = self.Conversion
            self.DatosPrimConversion.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Resumen = PhotoImage(file="DatosPrimitivos/Resumen.gif")
            self.DatosPrimResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.DatosPrimResumen.image = self.Resumen
            self.DatosPrimResumen.place(x=0,y=0)
            
            #Se crean dos botones, uno para crear la ventana con las preguntas y el otro para volver atras
            self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)
            
            #Se añaden como pestañas en el notebook los labels con las imagenes ya cargadas
            self.notebook.add(self.DatosPrimDefinicion1,text="Pag 1")
            self.notebook.add(self.DatosPrimDefinicion2,text="Pag 2")
            self.notebook.add(self.DatosPrimEnteros,text="Pag 3")
            self.notebook.add(self.DatosPrimReales,text="Pag 4")
            self.notebook.add(self.DatosPrimCaracteres,text="Pag 5")
            self.notebook.add(self.DatosPrimLogicos,text="Pag 6")
            self.notebook.add(self.DatosPrimApunt,text="Pag 7")
            self.notebook.add(self.DatosPrimConversion,text="Pag 8")
            self.notebook.add(self.DatosPrimResumen,text="Pag 9")
            self.notebook.pack()

    def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaTeoria.destroy()#Y lo que hace es cerrar la ventana Teoria y
        self.VT.deiconify()# reabrir la ventana anterior, en este caso la ventana principal.

    def Evaluacion(self):# Esta funcion es llamada cuando se aprieta el boton Evaluacion de conceptos
        VentanaEva=Evaluacion(self.ventanaTeoria)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con las preguntas del tema elegido