import tkinter as tk
from tkinter import ttk
from tkinter import *
from Subrutinas.EvaluacionSubrutinas import Evaluacion
class TeoriaSubrutinas():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana#Aqui se hace una instancia de la ventana teoria que se paso vacia como parametro
            self.ventanaTeoria.geometry("675x620")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
            self.ventanaTeoria.configure(bg= '#024747')#Se cambia el color del fondo
            self.VT=Temas#Aqui se hace una instancia de la ventana Temas que se paso como parametro
            self.notebook=ttk.Notebook(ventana)#Dentro de la ventana se crea un notebook para gestionar paneles

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Definicion = PhotoImage(file="Subrutinas/Definicion.gif")
            self.SubrutinaDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.SubrutinaDefinicion.image = self.Definicion
            self.SubrutinaDefinicion.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Declaracion = PhotoImage(file="Subrutinas/Declaracion.gif")
            self.SubrutinaDeclaracion = ttk.Label(ventana,image=self.Declaracion,background="white")
            self.SubrutinaDeclaracion.image = self.Declaracion
            self.SubrutinaDeclaracion.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Parametros = PhotoImage(file="Subrutinas/Parametros.gif")
            self.SubrutinaParametros = ttk.Label(ventana,image=self.Parametros,background="white")
            self.SubrutinaParametros.image = self.Parametros
            self.SubrutinaParametros.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Invocacion = PhotoImage(file="Subrutinas/Invocacion.gif")
            self.SubrutinasInvocacion = ttk.Label(ventana,image=self.Invocacion,background="white")
            self.SubrutinasInvocacion.image = self.Invocacion
            self.SubrutinasInvocacion.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.VarLocalGlobal = PhotoImage(file="Subrutinas/FuncionVarLocalGlobal.gif")
            self.SubrutinasVarLocalGlobal = ttk.Label(ventana,image=self.VarLocalGlobal,background="white")
            self.SubrutinasVarLocalGlobal.image = self.VarLocalGlobal
            self.SubrutinasVarLocalGlobal.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.BibliotecaFuncion = PhotoImage(file="Subrutinas/BibliotecasFunciones.gif")
            self.SubrutinasBibliotecas = ttk.Label(ventana,image=self.BibliotecaFuncion,background="white")
            self.SubrutinasBibliotecas.image = self.BibliotecaFuncion
            self.SubrutinasBibliotecas.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Resumen = PhotoImage(file="Subrutinas/Resumen.gif")
            self.SubrutinasResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.SubrutinasResumen.image = self.Resumen
            self.SubrutinasResumen.place(x=0,y=0)
            
            #Se crean dos botones, uno para crear la ventana con las preguntas y el otro para volver atras
            self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)
            
            #Se añaden como pestañas en el notebook los labels con las imagenes ya cargadas
            self.notebook.add(self.SubrutinaDefinicion,text="Pag 1")
            self.notebook.add(self.SubrutinaDeclaracion,text="Pag 2")
            self.notebook.add(self.SubrutinaParametros,text="Pag 3")
            self.notebook.add(self.SubrutinasInvocacion,text="Pag 4")
            self.notebook.add(self.SubrutinasVarLocalGlobal,text="Pag 5")
            self.notebook.add(self.SubrutinasBibliotecas,text="Pag 6")
            self.notebook.add(self.SubrutinasResumen,text="Pag 7")
            self.notebook.pack()
            
    def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaTeoria.destroy()#Y lo que hace es cerrar la ventana Teoria y
        self.VT.deiconify()# reabrir la ventana anterior, en este caso la ventana principal.

    def Evaluacion(self):# Esta funcion es llamada cuando se aprieta el boton Evaluacion de conceptos
        VentanaEva=Evaluacion(self.ventanaTeoria)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con las preguntas del tema elegido