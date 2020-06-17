import tkinter as tk
from tkinter import ttk
from tkinter import *
from Subrutinas.EvaluacionSubrutinas import Evaluacion
class TeoriaSubrutinas():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana
            self.ventanaTeoria.geometry("675x620")
            self.VT=Temas
            self.notebook=ttk.Notebook(ventana)
            self.Definicion = PhotoImage(file="Subrutinas/Definicion.gif")
            self.SubrutinaDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.SubrutinaDefinicion.image = self.Definicion
            self.SubrutinaDefinicion.place(x=0,y=0)
            self.Declaracion = PhotoImage(file="Subrutinas/Declaracion.gif")
            self.SubrutinaDeclaracion = ttk.Label(ventana,image=self.Declaracion,background="white")
            self.SubrutinaDeclaracion.image = self.Declaracion
            self.SubrutinaDeclaracion.place(x=0,y=0)
            self.Parametros = PhotoImage(file="Subrutinas/Parametros.gif")
            self.SubrutinaParametros = ttk.Label(ventana,image=self.Parametros,background="white")
            self.SubrutinaParametros.image = self.Parametros
            self.SubrutinaParametros.place(x=0,y=0)
            self.Invocacion = PhotoImage(file="Subrutinas/Invocacion.gif")
            self.SubrutinasInvocacion = ttk.Label(ventana,image=self.Invocacion,background="white")
            self.SubrutinasInvocacion.image = self.Invocacion
            self.SubrutinasInvocacion.place(x=0,y=0)
            self.VarLocalGlobal = PhotoImage(file="Subrutinas/FuncionVarLocalGlobal.gif")
            self.SubrutinasVarLocalGlobal = ttk.Label(ventana,image=self.VarLocalGlobal,background="white")
            self.SubrutinasVarLocalGlobal.image = self.VarLocalGlobal
            self.SubrutinasVarLocalGlobal.place(x=0,y=0)
            self.BibliotecaFuncion = PhotoImage(file="Subrutinas/BibliotecasFunciones.gif")
            self.SubrutinasBibliotecas = ttk.Label(ventana,image=self.BibliotecaFuncion,background="white")
            self.SubrutinasBibliotecas.image = self.BibliotecaFuncion
            self.SubrutinasBibliotecas.place(x=0,y=0)
            self.Resumen = PhotoImage(file="Subrutinas/Resumen.gif")
            self.SubrutinasResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.SubrutinasResumen.image = self.Resumen
            self.SubrutinasResumen.place(x=0,y=0)
            self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)
            self.notebook.add(self.SubrutinaDefinicion,text="Pag 1")
            self.notebook.add(self.SubrutinaDeclaracion,text="Pag 2")
            self.notebook.add(self.SubrutinaParametros,text="Pag 3")
            self.notebook.add(self.SubrutinasInvocacion,text="Pag 4")
            self.notebook.add(self.SubrutinasVarLocalGlobal,text="Pag 5")
            self.notebook.add(self.SubrutinasBibliotecas,text="Pag 6")
            self.notebook.add(self.SubrutinasResumen,text="Pag 7")

            self.notebook.pack()
    def Volver(self):
        self.ventanaTeoria.destroy()
        self.VT.deiconify()

    def Evaluacion(self):
        VentanaEva=Evaluacion(self.ventanaTeoria)