import tkinter as tk
from tkinter import ttk
from tkinter import *

class TeoriaExpr():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana
            self.ventanaTeoria.geometry("700x590")
            self.VT=Temas
            self.notebook=ttk.Notebook(ventana)
            self.Definicion = PhotoImage(file="Expresiones/Definicion.gif")
            self.ExprDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.ExprDefinicion.image = self.Definicion
            self.ExprDefinicion.place(x=0,y=0)
            self.OpAritmeticos = PhotoImage(file="Expresiones/OperadoresAritmeticos.gif")
            self.ExprOpAritmeticos = ttk.Label(ventana,image=self.OpAritmeticos,background="white")
            self.ExprOpAritmeticos.image = self.OpAritmeticos
            self.ExprOpAritmeticos.place(x=0,y=0)
            self.OpAritmeticosEj = PhotoImage(file="Expresiones/OperadoresAritmeticosEjemplos.gif")
            self.ExprOpAritmeticosEj = ttk.Label(ventana,image=self.OpAritmeticosEj,background="white")
            self.ExprOpAritmeticosEj.image = self.OpAritmeticosEj
            self.ExprOpAritmeticosEj.place(x=0,y=0)
            self.OpLogicos = PhotoImage(file="Expresiones/OperadoresLogicos.gif")
            self.ExprOpLogicos = ttk.Label(ventana,image=self.OpLogicos,background="white")
            self.ExprOpLogicos.image = self.OpLogicos
            self.ExprOpLogicos.place(x=0,y=0)
            self.OpRelacionales = PhotoImage(file="Expresiones/OperadoresRelacionales.gif")
            self.ExprOpRelacionales = ttk.Label(ventana,image=self.OpRelacionales,background="white")
            self.ExprOpRelacionales.image = self.OpRelacionales
            self.ExprOpRelacionales.place(x=0,y=0)
            self.ExpresionesComplejas = PhotoImage(file="Expresiones/ExpresionesComplejasProcedencia.gif")
            self.ExprComp = ttk.Label(ventana,image=self.ExpresionesComplejas,background="white")
            self.ExprComp.image = self.ExpresionesComplejas
            self.ExprComp.place(x=0,y=0)
            self.Asignacion = PhotoImage(file="Expresiones/AsignacionResultados.gif")
            self.ExprAsigRes = ttk.Label(ventana,image=self.Asignacion,background="white")
            self.ExprAsigRes.image = self.Asignacion
            self.ExprAsigRes.place(x=0,y=0)
            self.Uso = PhotoImage(file="Expresiones/UsoVariables.gif")
            self.ExprUsoVar = ttk.Label(ventana,image=self.Uso,background="white")
            self.ExprUsoVar.image = self.Uso
            self.ExprUsoVar.place(x=0,y=0)
            self.Resumen = PhotoImage(file="Expresiones/Resumen.gif")
            self.ExprResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.ExprResumen.image = self.Resumen
            self.ExprResumen.place(x=0,y=0)
            #self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)
            self.notebook.add(self.ExprDefinicion,text="Pag 1")
            self.notebook.add(self.ExprOpAritmeticos,text="Pag 2")
            self.notebook.add(self.ExprOpAritmeticosEj,text="Pag 3")
            self.notebook.add(self.ExprOpRelacionales,text="Pag 4")
            self.notebook.add(self.ExprOpLogicos,text="Pag 5")
            self.notebook.add(self.ExprAsigRes,text="Pag 6")
            self.notebook.add(self.ExprUsoVar,text="Pag 7")
            self.notebook.add(self.ExprComp,text="Pag 8")
            self.notebook.add(self.ExprResumen,text="Pag 9")
            self.notebook.pack()
    def Volver(self):
        self.ventanaTeoria.destroy()
        self.VT.deiconify()