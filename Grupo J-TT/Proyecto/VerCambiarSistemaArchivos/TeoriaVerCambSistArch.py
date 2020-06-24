import tkinter as tk
from tkinter import ttk
from tkinter import *
from VerCambiarSistemaArchivos.EvaluacionVerCambSistArch import Evaluacion
class TeoriaVerCamb():
    def __init__(self,ventana,temas):
            self.ventanaTeoria=ventana#Aqui se hace una instancia de la ventana teoria que se paso vacia como parametro
            self.VT=temas#Aqui se hace una instancia de la ventana Temas que se paso como parametro
            self.ventanaTeoria.geometry("680x410")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
            self.ventanaTeoria.configure(bg= '#024747')#Se cambia el color del fondo
            self.notebook=ttk.Notebook(ventana)#Dentro de la ventana se crea un notebook para gestionar paneles

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.lsA = PhotoImage(file="VerCambiarSistemaArchivos/ls-a.gif")
            self.VerCamblsA = ttk.Label(ventana,image=self.lsA,background="white")
            self.VerCamblsA.image = self.lsA
            self.VerCamblsA.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.lsL = PhotoImage(file="VerCambiarSistemaArchivos/ls-l.gif")
            self.VerCamblsL = ttk.Label(ventana,image=self.lsL,background="white")
            self.VerCamblsL.image = self.lsL
            self.VerCamblsL.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.lsAlt = PhotoImage(file="VerCambiarSistemaArchivos/ls-alt.gif")
            self.VerCamblsAlt = ttk.Label(ventana,image=self.lsAlt,background="white")
            self.VerCamblsAlt.image = self.lsAlt
            self.VerCamblsAlt.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Cp1 = PhotoImage(file="VerCambiarSistemaArchivos/cp1.gif")
            self.VerCamblsCp1 = ttk.Label(ventana,image=self.Cp1,background="white")
            self.VerCamblsCp1.image = self.Cp1
            self.VerCamblsCp1.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Cp2 = PhotoImage(file="VerCambiarSistemaArchivos/cp2.gif")
            self.VerCamblsCp2 = ttk.Label(ventana,image=self.Cp2,background="white")
            self.VerCamblsCp2.image = self.Cp2
            self.VerCamblsCp2.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Wildcards = PhotoImage(file="VerCambiarSistemaArchivos/wildcards.gif")
            self.VerCamblsWildcards = ttk.Label(ventana,image=self.Wildcards,background="white")
            self.VerCamblsWildcards.image = self.Wildcards
            self.VerCamblsWildcards.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Mv = PhotoImage(file="VerCambiarSistemaArchivos/mv.gif")
            self.VerCamblsMv = ttk.Label(ventana,image=self.Mv,background="white")
            self.VerCamblsMv.image = self.Mv
            self.VerCamblsMv.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Rm = PhotoImage(file="VerCambiarSistemaArchivos/rm.gif")
            self.VerCamblsRm = ttk.Label(ventana,image=self.Rm,background="white")
            self.VerCamblsRm.image = self.Rm
            self.VerCamblsRm.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Resumen = PhotoImage(file="VerCambiarSistemaArchivos/Resumen.gif")
            self.VerCamblsResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.VerCamblsResumen.image = self.Resumen
            self.VerCamblsResumen.place(x=0,y=0)

            #Se crean dos botones, uno para crear la ventana con las preguntas y el otro para volver atras
            self.btnEvaluacion = Button(ventana,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(ventana, text='Volver',command=self.Volver).pack(side=BOTTOM)

            #Se añaden como pestañas en el notebook los labels con las imagenes ya cargadas
            self.notebook.add(self.VerCamblsA,text="Pag 1")
            self.notebook.add(self.VerCamblsL,text="Pag 2")
            self.notebook.add(self.VerCamblsAlt,text="Pag 3")
            self.notebook.add(self.VerCamblsCp1,text="Pag 4")
            self.notebook.add(self.VerCamblsCp2,text="Pag 5")
            self.notebook.add(self.VerCamblsWildcards,text="Pag 6")
            self.notebook.add(self.VerCamblsMv,text="Pag 7")
            self.notebook.add(self.VerCamblsRm,text="Pag 8")
            self.notebook.add(self.VerCamblsResumen,text="Pag 9")
            self.notebook.pack()

    def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaTeoria.destroy()#Y lo que hace es cerrar la ventana Teoria y
        self.VT.deiconify()# reabrir la ventana anterior, en este caso la ventana principal.

    def Evaluacion(self):# Esta funcion es llamada cuando se aprieta el boton Evaluacion de conceptos
        eva=Evaluacion(self.ventanaTeoria)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con las preguntas del tema elegido
