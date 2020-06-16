import tkinter as tk
from tkinter import ttk
from tkinter import *

class TeoriaEntSalDatos():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana
            self.ventanaTeoria.geometry("680x520")
            self.VT=Temas
            self.notebook=ttk.Notebook(ventana)
            self.Definicion = PhotoImage(file="EntradaSalidadeDatos/Definicion.gif")
            self.EntSalDatosDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.EntSalDatosDefinicion.image = self.Definicion
            self.EntSalDatosDefinicion.place(x=0,y=0)
            self.InterfazTexto = PhotoImage(file="EntradaSalidadeDatos/InterfazTexto.gif")
            self.EntSalDatosTexto = ttk.Label(ventana,image=self.InterfazTexto,background="white")
            self.EntSalDatosTexto.image = self.InterfazTexto
            self.EntSalDatosTexto.place(x=0,y=0)
            self.InterfazGrafica = PhotoImage(file="EntradaSalidadeDatos/InterfazGrafica.gif")
            self.EntSalDatosGrafica = ttk.Label(ventana,image=self.InterfazGrafica,background="white")
            self.EntSalDatosGrafica.image = self.InterfazGrafica
            self.EntSalDatosGrafica.place(x=0,y=0)
            self.Archivo = PhotoImage(file="EntradaSalidadeDatos/Archivo.gif")
            self.EntSalDatosArchivo = ttk.Label(ventana,image=self.Archivo,background="white")
            self.EntSalDatosArchivo.image = self.Archivo
            self.EntSalDatosArchivo.place(x=0,y=0)
            self.Resumen = PhotoImage(file="EntradaSalidadeDatos/Resumen.gif")
            self.EntSalDatosResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.EntSalDatosResumen.image = self.Resumen
            self.EntSalDatosResumen.place(x=0,y=0)
            #self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)
            self.notebook.add(self.EntSalDatosDefinicion,text="Pag 1")
            self.notebook.add(self.EntSalDatosTexto,text="Pag 2")
            self.notebook.add(self.EntSalDatosGrafica,text="Pag 3")
            self.notebook.add(self.EntSalDatosArchivo,text="Pag 4")
            self.notebook.add(self.EntSalDatosResumen,text="Pag 5")
            self.notebook.pack()
    def Volver(self):
        self.ventanaTeoria.destroy()
        self.VT.deiconify()