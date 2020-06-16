import tkinter as tk
from tkinter import ttk
from tkinter import *

class TeoriaDatosPrim():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana
            self.ventanaTeoria.geometry("685x500")
            self.VT=Temas
            self.notebook=ttk.Notebook(ventana)
            self.Definicion1 = PhotoImage(file="DatosPrimitivos/Definicion1.gif")
            self.DatosPrimDefinicion1 = ttk.Label(ventana,image=self.Definicion1,background="white")
            self.DatosPrimDefinicion1.image = self.Definicion1
            self.DatosPrimDefinicion1.place(x=0,y=0)
            self.Definicion2 = PhotoImage(file="DatosPrimitivos/Definicion2.gif")
            self.DatosPrimDefinicion2 = ttk.Label(ventana,image=self.Definicion2,background="white")
            self.DatosPrimDefinicion2.image = self.Definicion2
            self.DatosPrimDefinicion2.place(x=0,y=0)
            self.Enteros = PhotoImage(file="DatosPrimitivos/Enteros.gif")
            self.DatosPrimEnteros = ttk.Label(ventana,image=self.Enteros,background="white")
            self.DatosPrimEnteros.image = self.Enteros
            self.DatosPrimEnteros.place(x=0,y=0)
            self.Reales = PhotoImage(file="DatosPrimitivos/Reales.gif")
            self.DatosPrimReales = ttk.Label(ventana,image=self.Reales,background="white")
            self.DatosPrimReales.image = self.Reales
            self.DatosPrimReales.place(x=0,y=0)
            self.Caracteres = PhotoImage(file="DatosPrimitivos/Caracteres.gif")
            self.DatosPrimCaracteres = ttk.Label(ventana,image=self.Caracteres,background="white")
            self.DatosPrimCaracteres.image = self.Caracteres
            self.DatosPrimCaracteres.place(x=0,y=0)
            self.Logicos = PhotoImage(file="DatosPrimitivos/Logicos.gif")
            self.DatosPrimLogicos = ttk.Label(ventana,image=self.Logicos,background="white")
            self.DatosPrimLogicos.image = self.Logicos
            self.DatosPrimLogicos.place(x=0,y=0)
            self.Apuntadores = PhotoImage(file="DatosPrimitivos/Apuntadores.gif")
            self.DatosPrimApunt = ttk.Label(ventana,image=self.Apuntadores,background="white")
            self.DatosPrimApunt.image = self.Apuntadores
            self.DatosPrimApunt.place(x=0,y=0)
            self.Conversion = PhotoImage(file="DatosPrimitivos/Conversion.gif")
            self.DatosPrimConversion = ttk.Label(ventana,image=self.Conversion,background="white")
            self.DatosPrimConversion.image = self.Conversion
            self.DatosPrimConversion.place(x=0,y=0)
            self.Resumen = PhotoImage(file="DatosPrimitivos/Resumen.gif")
            self.DatosPrimResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.DatosPrimResumen.image = self.Resumen
            self.DatosPrimResumen.place(x=0,y=0)
            #self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)
            self.notebook.add(self.DatosPrimDefinicion1,text="Pag 1")
            self.notebook.add(self.DatosPrimDefinicion2,text="Pag 2")
            self.notebook.add(self.DatosPrimEnteros,text="Pag 3")
            self.notebook.add(self.DatosPrimReales,text="Pag 4")
            self.notebook.add(self.DatosPrimCaracteres,text="Pag 5")
            self.notebook.add(self.DatosPrimLogicos,text="Pag 6")
            self.notebook.add(self.DatosPrimApunt,text="Pag 7")
            self.notebook.add(self.DatosPrimConversion,text="Pag 8")
            self.notebook.add(self.DatosPrimResumen,text="Pag 9")
            self.notebook.pack()
    def Volver(self):
        self.ventanaTeoria.destroy()
        self.VT.deiconify()