import tkinter as tk
from tkinter import ttk
from tkinter import *
from TrabajoenEquipoGit.EvaluacionTrabajoEquipo import Evaluacion
class TeoriaTrabajo():
    def __init__(self,ventana,temas):
            self.ventanaTeoria=ventana
            self.VT=temas
            self.ventanaTeoria.geometry("680x510")
            self.ventanaTeoria.configure(bg= '#024747')
            self.notebook=ttk.Notebook(ventana)

            self.Clone = PhotoImage(file="TrabajoenEquipoGit/clone.gif")
            self.TrabajoClone = ttk.Label(ventana,image=self.Clone,background="white")
            self.TrabajoClone.image = self.Clone
            self.TrabajoClone.place(x=0,y=0)

            self.Remote = PhotoImage(file="TrabajoenEquipoGit/remote.gif")
            self.TrabajoRemote = ttk.Label(ventana,image=self.Remote,background="white")
            self.TrabajoRemote.image = self.Remote
            self.TrabajoRemote.place(x=0,y=0)

            self.Fetch = PhotoImage(file="TrabajoenEquipoGit/fetch.gif")
            self.TrabajoFetch = ttk.Label(ventana,image=self.Fetch,background="white")
            self.TrabajoFetch.image = self.Fetch
            self.TrabajoFetch.place(x=0,y=0)
            
            self.Merge = PhotoImage(file="TrabajoenEquipoGit/merge.gif")
            self.TrabajoMerge = ttk.Label(ventana,image=self.Merge,background="white")
            self.TrabajoMerge.image = self.Merge
            self.TrabajoMerge.place(x=0,y=0)

            self.Flujo = PhotoImage(file="TrabajoenEquipoGit/flujoTrabajo.gif")
            self.TrabajoFlujo = ttk.Label(ventana,image=self.Flujo,background="white")
            self.TrabajoFlujo.image = self.Flujo
            self.TrabajoFlujo.place(x=0,y=0)

            self.Push = PhotoImage(file="TrabajoenEquipoGit/push.gif")
            self.TrabajoPush = ttk.Label(ventana,image=self.Push,background="white")
            self.TrabajoPush.image = self.Push
            self.TrabajoPush.place(x=0,y=0)

            self.Resumen = PhotoImage(file="TrabajoenEquipoGit/Resumen.gif")
            self.TrabajoResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.TrabajoResumen.image = self.Resumen
            self.TrabajoResumen.place(x=0,y=0)

            self.btnEvaluacion = Button(ventana,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(ventana, text='Volver',command=self.Volver).pack(side=BOTTOM)

            self.notebook.add(self.TrabajoClone,text="Pag 1")
            self.notebook.add(self.TrabajoRemote,text="Pag 2")
            self.notebook.add(self.TrabajoFetch,text="Pag 3")
            self.notebook.add(self.TrabajoMerge,text="Pag 4")
            self.notebook.add(self.TrabajoFlujo,text="Pag 5")
            self.notebook.add(self.TrabajoPush,text="Pag 6")
            self.notebook.add(self.TrabajoResumen,text="Pag 7")
            self.notebook.pack()
    def Volver(self):
        self.ventanaTeoria.destroy()
        self.VT.deiconify()
    def Evaluacion(self):
        eva=Evaluacion(self.ventanaTeoria)