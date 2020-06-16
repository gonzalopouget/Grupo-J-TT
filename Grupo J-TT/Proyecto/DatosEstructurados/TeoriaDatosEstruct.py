import tkinter as tk
from tkinter import ttk
from tkinter import *

class TeoriaDatosEstruct():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana
            self.ventanaTeoria.geometry("680x575")
            self.VT=Temas
            self.notebook=ttk.Notebook(ventana)
            self.Definicion = PhotoImage(file="DatosEstructurados/Definicion.gif")
            self.DatosEstructDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.DatosEstructDefinicion.image = self.Definicion
            self.DatosEstructDefinicion.place(x=0,y=0)
            self.Matrices1 = PhotoImage(file="DatosEstructurados/Matrices1.gif")
            self.DatosEstructMat1 = ttk.Label(ventana,image=self.Matrices1,background="white")
            self.DatosEstructMat1.image = self.Matrices1
            self.DatosEstructMat1.place(x=0,y=0)
            self.Matrices2 = PhotoImage(file="DatosEstructurados/Matrices2.gif")
            self.DatosEstructMat2 = ttk.Label(ventana,image=self.Matrices2,background="white")
            self.DatosEstructMat2.image = self.Matrices2
            self.DatosEstructMat2.place(x=0,y=0)
            self.Matrices3 = PhotoImage(file="DatosEstructurados/Matrices3.gif")
            self.DatosEstructMat3 = ttk.Label(ventana,image=self.Matrices3,background="white")
            self.DatosEstructMat3.image = self.Matrices3
            self.DatosEstructMat3.place(x=0,y=0)
            self.CadenasCaracteres = PhotoImage(file="DatosEstructurados/CadenasCaracteres.gif")
            self.DatosEstructCadCarac = ttk.Label(ventana,image=self.CadenasCaracteres,background="white")
            self.DatosEstructCadCarac.image = self.CadenasCaracteres
            self.DatosEstructCadCarac.place(x=0,y=0)
            self.Registro1 = PhotoImage(file="DatosEstructurados/Registro1.gif")
            self.DatosEstructReg1 = ttk.Label(ventana,image=self.Registro1,background="white")
            self.DatosEstructReg1.image = self.Registro1
            self.DatosEstructReg1.place(x=0,y=0)
            self.Registro2 = PhotoImage(file="DatosEstructurados/Registro2.gif")
            self.DatosEstructReg2 = ttk.Label(ventana,image=self.Registro2,background="white")
            self.DatosEstructReg2.image = self.Registro2
            self.DatosEstructReg2.place(x=0,y=0)
            self.Otros = PhotoImage(file="DatosEstructurados/OtrosTipos.gif")
            self.DatosEstructOtros = ttk.Label(ventana,image=self.Otros,background="white")
            self.DatosEstructOtros.image = self.Otros
            self.DatosEstructOtros.place(x=0,y=0)
            self.Resumen = PhotoImage(file="DatosEstructurados/Resumen.gif")
            self.DatosEstructResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.DatosEstructResumen.image = self.Resumen
            self.DatosEstructResumen.place(x=0,y=0)
            #self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)
            self.notebook.add(self.DatosEstructDefinicion,text="Pag 1")
            self.notebook.add(self.DatosEstructMat1,text="Pag 2")
            self.notebook.add(self.DatosEstructMat2,text="Pag 3")
            self.notebook.add(self.DatosEstructMat3,text="Pag 4")
            self.notebook.add(self.DatosEstructCadCarac,text="Pag 5")
            self.notebook.add(self.DatosEstructReg1,text="Pag 6")
            self.notebook.add(self.DatosEstructReg2,text="Pag 7")
            self.notebook.add(self.DatosEstructOtros,text="Pag 8")
            self.notebook.add(self.DatosEstructResumen,text="Pag 9")
            self.notebook.pack()
    def Volver(self):
        self.ventanaTeoria.destroy()
        self.VT.deiconify()