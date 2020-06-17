import tkinter as tk
from tkinter import ttk
from tkinter import *
from VariablesyAsignaciones.EvaluacionVarAsignaciones import Evaluacion
class TeoriaVarAsignaciones():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana
            self.ventanaTeoria.geometry("680x540")
            self.VT=Temas
            self.notebook=ttk.Notebook(ventana)
            self.Definicion = PhotoImage(file="VariablesyAsignaciones/DefinicionVariable.gif")
            self.VarAsignaDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.VarAsignaDefinicion.image = self.Definicion
            self.VarAsignaDefinicion.place(x=0,y=0)
            self.DeclaracionInicializacion = PhotoImage(file="VariablesyAsignaciones/DeclaracionEInicializacion.gif")
            self.VarAsignaDeclaracionIni = ttk.Label(ventana,image=self.DeclaracionInicializacion,background="white")
            self.VarAsignaDeclaracionIni.image = self.DeclaracionInicializacion
            self.VarAsignaDeclaracionIni.place(x=0,y=0)
            self.Asignacion = PhotoImage(file="VariablesyAsignaciones/Asignacion.gif")
            self.VarAsignaAsignacion = ttk.Label(ventana,image=self.Asignacion,background="white")
            self.VarAsignaAsignacion.image = self.Asignacion
            self.VarAsignaAsignacion.place(x=0,y=0)
            self.Transferencia = PhotoImage(file="VariablesyAsignaciones/Transferencia.gif")
            self.VarAsignaTransferencia = ttk.Label(ventana,image=self.Transferencia,background="white")
            self.VarAsignaTransferencia.image = self.Transferencia
            self.VarAsignaTransferencia.place(x=0,y=0)
            self.EjInicializacion = PhotoImage(file="VariablesyAsignaciones/EjemplosInicializacion.gif")
            self.VarAsignaEjIni = ttk.Label(ventana,image=self.EjInicializacion,background="white")
            self.VarAsignaEjIni.image = self.EjInicializacion
            self.VarAsignaEjIni.place(x=0,y=0)
            self.RecomendacionesNombres = PhotoImage(file="VariablesyAsignaciones/RecomendacionesParaNombres.gif")
            self.VarAsignaRecomendacionNom = ttk.Label(ventana,image=self.RecomendacionesNombres,background="white")
            self.VarAsignaRecomendacionNom.image = self.RecomendacionesNombres
            self.VarAsignaRecomendacionNom.place(x=0,y=0)
            self.Resumen = PhotoImage(file="VariablesyAsignaciones/Resumen.gif")
            self.VarAsignaResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.VarAsignaResumen.image = self.Resumen
            self.VarAsignaResumen.place(x=0,y=0)
            self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)
            self.notebook.add(self.VarAsignaDefinicion,text="Pag 1")
            self.notebook.add(self.VarAsignaDeclaracionIni,text="Pag 2")
            self.notebook.add(self.VarAsignaEjIni,text="Pag 3")
            self.notebook.add(self.VarAsignaAsignacion,text="Pag 4")
            self.notebook.add(self.VarAsignaTransferencia,text="Pag 5")
            self.notebook.add(self.VarAsignaRecomendacionNom,text="Pag 6")
            self.notebook.add(self.VarAsignaResumen,text="Pag 7")

            self.notebook.pack()
    def Volver(self):
        self.ventanaTeoria.destroy()
        self.VT.deiconify()
        
    def Evaluacion(self):
         VentanaEva=Evaluacion(self.ventanaTeoria)