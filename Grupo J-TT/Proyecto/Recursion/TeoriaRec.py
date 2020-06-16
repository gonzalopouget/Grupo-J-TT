import tkinter as tk
from tkinter import ttk
from tkinter import *

class TeoriaRec():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana
            self.ventanaTeoria.geometry("685x530")
            self.VT=Temas
            self.notebook=ttk.Notebook(ventana)
            self.Definicion = PhotoImage(file="Recursion/Definicion.gif")
            self.RecDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.RecDefinicion.image = self.Definicion
            self.RecDefinicion.place(x=0,y=0)
            self.Ejemplo = PhotoImage(file="Recursion/Ejemplo.gif")
            self.RecEjemplo = ttk.Label(ventana,image=self.Ejemplo,background="white")
            self.RecEjemplo.image = self.Ejemplo
            self.RecEjemplo.place(x=0,y=0)
            self.ErroresComunes = PhotoImage(file="Recursion/ErroresComunes.gif")
            self.RecErroresComunes = ttk.Label(ventana,image=self.ErroresComunes,background="white")
            self.RecErroresComunes.image = self.ErroresComunes
            self.RecErroresComunes.place(x=0,y=0)
            self.RecursionCola = PhotoImage(file="Recursion/RecursionDeCola.gif")
            self.RecRecursionCola = ttk.Label(ventana,image=self.RecursionCola,background="white")
            self.RecRecursionCola.image = self.RecursionCola
            self.RecRecursionCola.place(x=0,y=0)
            self.Resumen = PhotoImage(file="Recursion/Resumen.gif")
            self.RecResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.RecResumen.image = self.Resumen
            self.RecResumen.place(x=0,y=0)
            #self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)
            self.notebook.add(self.RecDefinicion,text="Pag 1")
            self.notebook.add(self.RecEjemplo,text="Pag 2")
            self.notebook.add(self.RecRecursionCola,text="Pag 3")
            self.notebook.add(self.RecErroresComunes,text="Pag 4")
            self.notebook.add(self.RecResumen,text="Pag 5")
            self.notebook.pack()
    def Volver(self):
        self.ventanaTeoria.destroy()
        self.VT.deiconify()