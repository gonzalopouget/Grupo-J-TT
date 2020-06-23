import tkinter as tk
from tkinter import ttk
from tkinter import *
from EntradaSalidadeDatos.EvaluacionEntSalDatos import Evaluacion
class TeoriaEntSalDatos():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana#Aqui se hace una instancia de la ventana teoria que se paso vacia como parametro
            self.ventanaTeoria.geometry("680x520")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
            self.ventanaTeoria.configure(bg= '#024747')#Se cambia el color del fondo
            self.VT=Temas#Aqui se hace una instancia de la ventana Temas que se paso como parametro
            self.notebook=ttk.Notebook(ventana)#Dentro de la ventana se crea un notebook para gestionar paneles
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Definicion = PhotoImage(file="EntradaSalidadeDatos/Definicion.gif")
            self.EntSalDatosDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.EntSalDatosDefinicion.image = self.Definicion
            self.EntSalDatosDefinicion.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.InterfazTexto = PhotoImage(file="EntradaSalidadeDatos/InterfazTexto.gif")
            self.EntSalDatosTexto = ttk.Label(ventana,image=self.InterfazTexto,background="white")
            self.EntSalDatosTexto.image = self.InterfazTexto
            self.EntSalDatosTexto.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.InterfazGrafica = PhotoImage(file="EntradaSalidadeDatos/InterfazGrafica.gif")
            self.EntSalDatosGrafica = ttk.Label(ventana,image=self.InterfazGrafica,background="white")
            self.EntSalDatosGrafica.image = self.InterfazGrafica
            self.EntSalDatosGrafica.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Archivo = PhotoImage(file="EntradaSalidadeDatos/Archivo.gif")
            self.EntSalDatosArchivo = ttk.Label(ventana,image=self.Archivo,background="white")
            self.EntSalDatosArchivo.image = self.Archivo
            self.EntSalDatosArchivo.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Resumen = PhotoImage(file="EntradaSalidadeDatos/Resumen.gif")
            self.EntSalDatosResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.EntSalDatosResumen.image = self.Resumen
            self.EntSalDatosResumen.place(x=0,y=0)

            #Se crean dos botones, uno para crear la ventana con las preguntas y el otro para volver atras
            self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)
            
            #Se añaden como pestañas en el notebook los labels con las imagenes ya cargadas
            self.notebook.add(self.EntSalDatosDefinicion,text="Pag 1")
            self.notebook.add(self.EntSalDatosTexto,text="Pag 2")
            self.notebook.add(self.EntSalDatosGrafica,text="Pag 3")
            self.notebook.add(self.EntSalDatosArchivo,text="Pag 4")
            self.notebook.add(self.EntSalDatosResumen,text="Pag 5")
            self.notebook.pack()

    def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaTeoria.destroy()#Y lo que hace es cerrar la ventana Teoria y
        self.VT.deiconify()# reabrir la ventana anterior, en este caso la ventana principal.

    def Evaluacion(self):# Esta funcion es llamada cuando se aprieta el boton Evaluacion de conceptos
         VentanaEva=Evaluacion(self.ventanaTeoria)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con las preguntas del tema elegido