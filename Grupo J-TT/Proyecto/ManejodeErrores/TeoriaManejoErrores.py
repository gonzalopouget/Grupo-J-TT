import tkinter as tk
from tkinter import ttk
from tkinter import *
from ManejodeErrores.EvaluacionManejoErrores import Evaluacion
class TeoriaManejoErrores():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana
            self.ventanaTeoria.geometry("680x530")
            self.VT=Temas
            self.notebook=ttk.Notebook(ventana)
            self.Definicion = PhotoImage(file="ManejodeErrores/Definicion.gif")
            self.ManejoDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.ManejoDefinicion.image = self.Definicion
            self.ManejoDefinicion.place(x=0,y=0)
            self.ValoresRetorEsp = PhotoImage(file="ManejodeErrores/ValoresRetornoEspeciales.gif")
            self.ManejoValoresRetorEsp = ttk.Label(ventana,image=self.ValoresRetorEsp,background="white")
            self.ManejoValoresRetorEsp.image = self.ValoresRetorEsp
            self.ManejoValoresRetorEsp.place(x=0,y=0)
            self.IndicadoresExplic = PhotoImage(file="ManejodeErrores/IndicadoresExplicitos.gif")
            self.ManejoIndicadoresExplic = ttk.Label(ventana,image=self.IndicadoresExplic,background="white")
            self.ManejoIndicadoresExplic.image = self.IndicadoresExplic
            self.ManejoIndicadoresExplic.place(x=0,y=0)
            self.ManejadorErrores = PhotoImage(file="ManejodeErrores/ManejadorErrores.gif")
            self.ManejoManejadorErrores = ttk.Label(ventana,image=self.ManejadorErrores,background="white")
            self.ManejoManejadorErrores.image = self.ManejadorErrores
            self.ManejoManejadorErrores.place(x=0,y=0)
            self.Excepciones1 = PhotoImage(file="ManejodeErrores/Excepciones1.gif")
            self.ManejoExcepciones1 = ttk.Label(ventana,image=self.Excepciones1,background="white")
            self.ManejoExcepciones1.image = self.Excepciones1
            self.ManejoExcepciones1.place(x=0,y=0)
            self.Excepciones2 = PhotoImage(file="ManejodeErrores/Excepciones2.gif")
            self.ManejoExcepciones2 = ttk.Label(ventana,image=self.Excepciones2,background="white")
            self.ManejoExcepciones2.image = self.Excepciones2
            self.ManejoExcepciones2.place(x=0,y=0)
            self.ProgSegura = PhotoImage(file="ManejodeErrores/ProgramacionSeguraContraFallos.gif")
            self.ManejoProgSegura = ttk.Label(ventana,image=self.ProgSegura,background="white")
            self.ManejoProgSegura.image = self.ProgSegura
            self.ManejoProgSegura.place(x=0,y=0)
            self.Resumen = PhotoImage(file="ManejodeErrores/Resumen.gif")
            self.ManejoResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.ManejoResumen.image = self.Resumen
            self.ManejoResumen.place(x=0,y=0)
            self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)
            self.notebook.add(self.ManejoDefinicion,text="Pag 1")
            self.notebook.add(self.ManejoValoresRetorEsp,text="Pag 2")
            self.notebook.add(self.ManejoIndicadoresExplic,text="Pag 3")
            self.notebook.add(self.ManejoManejadorErrores,text="Pag 4")
            self.notebook.add(self.ManejoExcepciones1,text="Pag 5")
            self.notebook.add(self.ManejoExcepciones2,text="Pag 6")
            self.notebook.add(self.ManejoProgSegura,text="Pag 7")
            self.notebook.add(self.ManejoResumen,text="Pag 8")
            self.notebook.pack()
    def Volver(self):
        self.ventanaTeoria.destroy()
        self.VT.deiconify()

    def Evaluacion(self):
         VentanaEva=Evaluacion(self.ventanaTeoria)