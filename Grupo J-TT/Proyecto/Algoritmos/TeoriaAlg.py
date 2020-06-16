import tkinter as tk
from tkinter import ttk
from tkinter import *

class TeoriaAlg():

    def __init__(self,ventana,temas):
            self.ventanaTeoria=ventana
            self.VT=temas
            self.ventanaTeoria.geometry("680x410")
            self.notebook=ttk.Notebook(ventana)
            self.Definicion = PhotoImage(file="Algoritmos/Definicion.gif")
            self.AlgDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.AlgDefinicion.image = self.Definicion
            self.AlgDefinicion.place(x=0,y=0)
            self.Tipos = PhotoImage(file="Algoritmos/Tipos.gif")
            self.AlgTipos = ttk.Label(ventana,image=self.Tipos,background="white")
            self.AlgTipos.image = self.Tipos
            self.AlgTipos.place(x=0,y=0)
            self.Tecnicas1 = PhotoImage(file="Algoritmos/TecnicasDiseño1.gif")
            self.AlgTecnicas1 = ttk.Label(ventana,image=self.Tecnicas1,background="white")
            self.AlgTecnicas1.image = self.Tecnicas1
            self.AlgTecnicas1.place(x=0,y=0)
            self.Tecnicas2 = PhotoImage(file="Algoritmos/TecnicasDiseño2.gif")
            self.AlgTecnicas2 = ttk.Label(ventana,image=self.Tecnicas2,background="white")
            self.AlgTecnicas2.image = self.Tecnicas2
            self.AlgTecnicas2.place(x=0,y=0)
            self.Representacion = PhotoImage(file="Algoritmos/Representacion.gif")
            self.AlgRepresentacion = ttk.Label(ventana,image=self.Representacion,background="white")
            self.AlgRepresentacion.image = self.Representacion
            self.AlgRepresentacion.place(x=0,y=0)
            self.Resumen = PhotoImage(file="Algoritmos/Resumen.gif")
            self.AlgResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.AlgResumen.image = self.Resumen
            self.AlgResumen.place(x=0,y=0)
            #self.btnEvaluacion = Button(ventana,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(ventana, text='Volver',command=self.Volver).pack(side=BOTTOM)
            self.notebook.add(self.AlgDefinicion,text="Pag 1")
            self.notebook.add(self.AlgTipos,text="Pag 2")
            self.notebook.add(self.AlgTecnicas1,text="Pag 3")
            self.notebook.add(self.AlgTecnicas2,text="Pag 4")
            self.notebook.add(self.AlgRepresentacion,text="Pag 5")
            self.notebook.add(self.AlgResumen,text="Pag 6")
            self.notebook.pack()
    def Volver(self):
        self.ventanaTeoria.destroy()
        self.VT.deiconify()