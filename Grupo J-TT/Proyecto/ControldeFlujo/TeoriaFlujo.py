import tkinter as tk
from tkinter import ttk
from tkinter import *
from ControldeFlujo.EvaluacionTeoriaFlujo import Evaluacion
class TeoriaFlujo():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana#Aqui se hace una instancia de la ventana teoria que se paso vacia como parametro
            self.ventanaTeoria.geometry("690x610")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
            self.ventanaTeoria.configure(bg= '#024747')#Se cambia el color del fondo
            self.VT=Temas#Aqui se hace una instancia de la ventana Temas que se paso como parametro
            self.notebook=ttk.Notebook(ventana)#Dentro de la ventana se crea un notebook para gestionar paneles

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Definicion = PhotoImage(file="ControldeFlujo/Definicion.gif")
            self.FlujoDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.FlujoDefinicion.image = self.Definicion
            self.FlujoDefinicion.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.EstSelecc = PhotoImage(file="ControldeFlujo/EstructurasSeleccion.gif")
            self.FlujoEstSelecc = ttk.Label(ventana,image=self.EstSelecc,background="white")
            self.FlujoEstSelecc.image = self.EstSelecc
            self.FlujoEstSelecc.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.SeleccDoble = PhotoImage(file="ControldeFlujo/SeleccionDoble.gif")
            self.FlujoSeleccDoble = ttk.Label(ventana,image=self.SeleccDoble,background="white")
            self.FlujoSeleccDoble.image = self.SeleccDoble
            self.FlujoSeleccDoble.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.SeleccMult = PhotoImage(file="ControldeFlujo/SeleccionMultiple.gif")
            self.FlujoSeleccMult = ttk.Label(ventana,image=self.SeleccMult,background="white")
            self.FlujoSeleccMult.image = self.SeleccMult
            self.FlujoSeleccMult.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.EstRepe = PhotoImage(file="ControldeFlujo/EstructurasRepeticion.gif")
            self.FlujoEstRepe = ttk.Label(ventana,image=self.EstRepe,background="white")
            self.FlujoEstRepe.image = self.EstRepe
            self.FlujoEstRepe.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.CicloCond = PhotoImage(file="ControldeFlujo/CicloPorCondicion.gif")
            self.FlujoCicloCond = ttk.Label(ventana,image=self.CicloCond,background="white")
            self.FlujoCicloCond.image = self.CicloCond
            self.FlujoCicloCond.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.CicloCont = PhotoImage(file="ControldeFlujo/CicloPorContador.gif")
            self.FlujoCicloCont = ttk.Label(ventana,image=self.CicloCont,background="white")
            self.FlujoCicloCont.image = self.CicloCont
            self.FlujoCicloCont.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.BloquesCod = PhotoImage(file="ControldeFlujo/BloquesCodigo.gif")
            self.FlujoBloquesCod = ttk.Label(ventana,image=self.BloquesCod,background="white")
            self.FlujoBloquesCod.image = self.BloquesCod
            self.FlujoBloquesCod.place(x=0,y=0)

            self.EstrucAni = PhotoImage(file="ControldeFlujo/EstructuraAnidada.gif")
            self.FlujoEstructAni = ttk.Label(ventana,image=self.EstrucAni,background="white")
            self.FlujoEstructAni.image = self.EstrucAni
            self.FlujoEstructAni.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Resumen = PhotoImage(file="ControldeFlujo/Resumen.gif")
            self.FlujoResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.FlujoResumen.image = self.Resumen
            self.FlujoResumen.place(x=0,y=0)

            #Se crean dos botones, uno para crear la ventana con las preguntas y el otro para volver atras
            self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)

            #Se añaden como pestañas en el notebook los labels con las imagenes ya cargadas
            self.notebook.add(self.FlujoDefinicion,text="Pag 1")
            self.notebook.add(self.FlujoEstSelecc,text="Pag 2")
            self.notebook.add(self.FlujoSeleccDoble,text="Pag 3")
            self.notebook.add(self.FlujoSeleccMult,text="Pag 4")
            self.notebook.add(self.FlujoEstRepe,text="Pag 5")
            self.notebook.add(self.FlujoCicloCond,text="Pag 6")
            self.notebook.add(self.FlujoCicloCont,text="Pag 7")
            self.notebook.add(self.FlujoBloquesCod,text="Pag 8")
            self.notebook.add(self.FlujoEstructAni,text="Pag 9")
            self.notebook.add(self.FlujoResumen,text="Pag 10")
            self.notebook.pack()

    def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaTeoria.destroy()#Y lo que hace es cerrar la ventana Teoria y 
        self.VT.deiconify()# reabrir la ventana anterior, en este caso la ventana principal.

    def Evaluacion(self):# Esta funcion es llamada cuando se aprieta el boton Evaluacion de conceptos
         VentanaEva=Evaluacion(self.ventanaTeoria)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con las preguntas del tema elegido