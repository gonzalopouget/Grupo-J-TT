import tkinter as tk
from tkinter import ttk
from tkinter import *
from TrabajoenEquipoGit.EvaluacionTrabajoEquipo import Evaluacion
class TeoriaTrabajo():
    def __init__(self,ventana,temas):
            self.ventanaTeoria=ventana#Aqui se hace una instancia de la ventana teoria que se paso vacia como parametro
            self.VT=temas#Aqui se hace una instancia de la ventana Temas que se paso como parametro
            self.ventanaTeoria.geometry("680x510")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
            self.ventanaTeoria.configure(bg= '#024747')#Se cambia el color del fondo
            self.notebook=ttk.Notebook(ventana)#Dentro de la ventana se crea un notebook para gestionar paneles

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Clone = PhotoImage(file="TrabajoenEquipoGit/clone.gif")
            self.TrabajoClone = ttk.Label(ventana,image=self.Clone,background="white")
            self.TrabajoClone.image = self.Clone
            self.TrabajoClone.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Remote = PhotoImage(file="TrabajoenEquipoGit/remote.gif")
            self.TrabajoRemote = ttk.Label(ventana,image=self.Remote,background="white")
            self.TrabajoRemote.image = self.Remote
            self.TrabajoRemote.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Fetch = PhotoImage(file="TrabajoenEquipoGit/fetch.gif")
            self.TrabajoFetch = ttk.Label(ventana,image=self.Fetch,background="white")
            self.TrabajoFetch.image = self.Fetch
            self.TrabajoFetch.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Merge = PhotoImage(file="TrabajoenEquipoGit/merge.gif")
            self.TrabajoMerge = ttk.Label(ventana,image=self.Merge,background="white")
            self.TrabajoMerge.image = self.Merge
            self.TrabajoMerge.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Flujo = PhotoImage(file="TrabajoenEquipoGit/flujoTrabajo.gif")
            self.TrabajoFlujo = ttk.Label(ventana,image=self.Flujo,background="white")
            self.TrabajoFlujo.image = self.Flujo
            self.TrabajoFlujo.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Push = PhotoImage(file="TrabajoenEquipoGit/push.gif")
            self.TrabajoPush = ttk.Label(ventana,image=self.Push,background="white")
            self.TrabajoPush.image = self.Push
            self.TrabajoPush.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Resumen = PhotoImage(file="TrabajoenEquipoGit/Resumen.gif")
            self.TrabajoResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.TrabajoResumen.image = self.Resumen
            self.TrabajoResumen.place(x=0,y=0)

            #Se crean dos botones, uno para crear la ventana con las preguntas y el otro para volver atras
            self.btnEvaluacion = Button(ventana,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(ventana, text='Volver',command=self.Volver).pack(side=BOTTOM)

            #Se añaden como pestañas en el notebook los labels con las imagenes ya cargadas
            self.notebook.add(self.TrabajoClone,text="Pag 1")
            self.notebook.add(self.TrabajoRemote,text="Pag 2")
            self.notebook.add(self.TrabajoFetch,text="Pag 3")
            self.notebook.add(self.TrabajoMerge,text="Pag 4")
            self.notebook.add(self.TrabajoFlujo,text="Pag 5")
            self.notebook.add(self.TrabajoPush,text="Pag 6")
            self.notebook.add(self.TrabajoResumen,text="Pag 7")
            self.notebook.pack()

    def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaTeoria.destroy()#Y lo que hace es cerrar la ventana Teoria y
        self.VT.deiconify()# reabrir la ventana anterior, en este caso la ventana principal.

    def Evaluacion(self):# Esta funcion es llamada cuando se aprieta el boton Evaluacion de conceptos
        eva=Evaluacion(self.ventanaTeoria)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con las preguntas del tema elegido