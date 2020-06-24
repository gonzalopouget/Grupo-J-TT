import tkinter as tk
from tkinter import ttk
from tkinter import *
from RamificacionGit.EvaluacionRamificacion import Evaluacion
class TeoriaRam():
    def __init__(self,ventana,temas):
            self.ventanaTeoria=ventana#Aqui se hace una instancia de la ventana teoria que se paso vacia como parametro
            self.VT=temas#Aqui se hace una instancia de la ventana Temas que se paso como parametro
            self.ventanaTeoria.geometry("710x490")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
            self.ventanaTeoria.configure(bg= '#024747')#Se cambia el color del fondo
            self.notebook=ttk.Notebook(ventana)#Dentro de la ventana se crea un notebook para gestionar paneles

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Branch = PhotoImage(file="RamificacionGit/branch.gif")
            self.RamBranch = ttk.Label(ventana,image=self.Branch,background="white")
            self.RamBranch.image = self.Branch
            self.RamBranch.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.BranchResumen = PhotoImage(file="RamificacionGit/resumenRamificacion.gif")
            self.RamBranchResumen = ttk.Label(ventana,image=self.BranchResumen,background="white")
            self.RamBranchResumen.image = self.BranchResumen
            self.RamBranchResumen.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Branch2 = PhotoImage(file="RamificacionGit/branch2.gif")
            self.RamBranch2 = ttk.Label(ventana,image=self.Branch2,background="white")
            self.RamBranch2.image = self.Branch2
            self.RamBranch2.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Checkout = PhotoImage(file="RamificacionGit/checkout.gif")
            self.RamCheckout = ttk.Label(ventana,image=self.Checkout,background="white")
            self.RamCheckout.image = self.Checkout
            self.RamCheckout.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Commit = PhotoImage(file="RamificacionGit/commit.gif")
            self.RamCommit = ttk.Label(ventana,image=self.Commit,background="white")
            self.RamCommit.image = self.Commit
            self.RamCommit.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Merge = PhotoImage(file="RamificacionGit/merge.gif")
            self.RamMerge = ttk.Label(ventana,image=self.Merge,background="white")
            self.RamMerge.image = self.Merge
            self.RamMerge.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.MergeConflict = PhotoImage(file="RamificacionGit/mergeConflict.gif")
            self.RamMergeConf = ttk.Label(ventana,image=self.MergeConflict,background="white")
            self.RamMergeConf.image = self.MergeConflict
            self.RamMergeConf.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Delete = PhotoImage(file="RamificacionGit/borrar.gif")
            self.RamDelete = ttk.Label(ventana,image=self.Delete,background="white")
            self.RamDelete.image = self.Delete
            self.RamDelete.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Resumen = PhotoImage(file="RamificacionGit/Resumen.gif")
            self.RamResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.RamResumen.image = self.Resumen
            self.RamResumen.place(x=0,y=0)

            #Se crean dos botones, uno para crear la ventana con las preguntas y el otro para volver atras
            self.btnEvaluacion = Button(ventana,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(ventana, text='Volver',command=self.Volver).pack(side=BOTTOM)

            #Se añaden como pestañas en el notebook los labels con las imagenes ya cargadas
            self.notebook.add(self.RamBranch,text="Pag 1")
            self.notebook.add(self.RamBranchResumen,text="Pag 2")
            self.notebook.add(self.RamBranch2,text="Pag 3")
            self.notebook.add(self.RamCheckout,text="Pag 4")
            self.notebook.add(self.RamCommit,text="Pag 5")
            self.notebook.add(self.RamMerge,text="Pag 6")
            self.notebook.add(self.RamMergeConf,text="Pag 7")
            self.notebook.add(self.RamDelete,text="Pag 8")
            self.notebook.add(self.RamResumen,text="Pag 9")
            self.notebook.pack()

    def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaTeoria.destroy()#Y lo que hace es cerrar la ventana Teoria y
        self.VT.deiconify()# reabrir la ventana anterior, en este caso la ventana principal.

    def Evaluacion(self):# Esta funcion es llamada cuando se aprieta el boton Evaluacion de conceptos
        eva=Evaluacion(self.ventanaTeoria)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con las preguntas del tema elegido
