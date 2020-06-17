import tkinter as tk
from tkinter import ttk
from tkinter import *
from LenguajesdeProgramacion.EvaluacionLeng import Evaluacion
class TeoriaLeng():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana
            self.ventanaTeoria.geometry("680x570")
            self.VT=Temas
            self.notebook=ttk.Notebook(ventana)
            self.Definicion = PhotoImage(file="LenguajesdeProgramacion/DefinicionLenguaje.gif")
            self.LengDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.LengDefinicion.image = self.Definicion
            self.LengDefinicion.place(x=0,y=0)
            self.Procesadores = PhotoImage(file="LenguajesdeProgramacion/Procesadores.gif")
            self.LengProcesadores = ttk.Label(ventana,image=self.Procesadores,background="white")
            self.LengProcesadores.image = self.Procesadores
            self.LengProcesadores.place(x=0,y=0)
            self.Traduccion1 = PhotoImage(file="LenguajesdeProgramacion/TraduccionALenguajeMaquina1.gif")
            self.LengTraduccion1 = ttk.Label(ventana,image=self.Traduccion1,background="white")
            self.LengTraduccion1.image = self.Traduccion1
            self.LengTraduccion1.place(x=0,y=0)
            self.Traduccion2 = PhotoImage(file="LenguajesdeProgramacion/TraduccionALenguajeMaquina2.gif")
            self.LengTraduccion2 = ttk.Label(ventana,image=self.Traduccion2,background="white")
            self.LengTraduccion2.image = self.Traduccion2
            self.LengTraduccion2.place(x=0,y=0)
            self.Resumen = PhotoImage(file="LenguajesdeProgramacion/Resumen.gif")
            self.LengResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.LengResumen.image = self.Resumen
            self.LengResumen.place(x=0,y=0)
            self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)
            self.notebook.add(self.LengDefinicion,text="Pag 1")
            self.notebook.add(self.LengProcesadores,text="Pag 2")
            self.notebook.add(self.LengTraduccion1,text="Pag 3")
            self.notebook.add(self.LengTraduccion2,text="Pag 4")
            self.notebook.add(self.LengResumen,text="Pag 5")
            self.notebook.pack()
    def Volver(self):
        self.ventanaTeoria.destroy()
        self.VT.deiconify()

    def Evaluacion(self):
         VentanaEva=Evaluacion(self.ventanaTeoria)