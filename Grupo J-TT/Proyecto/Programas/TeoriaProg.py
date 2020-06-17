import tkinter as tk
from tkinter import ttk
from tkinter import *
from Programas.EvaluacionProg import EvaluacionProg
class TeoriaProg():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana
            self.ventanaTeoria.geometry("685x550")
            self.VT=Temas
            self.notebook=ttk.Notebook(ventana)
            self.Definicion1 = PhotoImage(file="Programas/QueSon1.gif")
            self.ProgDefinicion1 = ttk.Label(ventana,image=self.Definicion1,background="white")
            self.ProgDefinicion1.image = self.Definicion1
            self.ProgDefinicion1.place(x=0,y=0)
            self.Definicion2 = PhotoImage(file="Programas/QueSon2.gif")
            self.ProgDefinicion2 = ttk.Label(ventana,image=self.Definicion2,background="white")
            self.ProgDefinicion2.image = self.Definicion2
            self.ProgDefinicion2.place(x=0,y=0)
            self.FasesCicloVida = PhotoImage(file="Programas/FasesCicloDeVida.gif")
            self.ProgFasesCicloVida = ttk.Label(ventana,image=self.FasesCicloVida,background="white")
            self.ProgFasesCicloVida.image = self.FasesCicloVida
            self.ProgFasesCicloVida.place(x=0,y=0)
            self.DefinicionCicloVida = PhotoImage(file="Programas/DefinicionCicloDeVida.gif")
            self.ProgDefinicionCicloVida = ttk.Label(ventana,image=self.DefinicionCicloVida,background="white")
            self.ProgDefinicionCicloVida.image = self.DefinicionCicloVida
            self.ProgDefinicionCicloVida.place(x=0,y=0)
            self.DefinicionBuenPrograma = PhotoImage(file="Programas/DefinicionBuenPrograma.gif")
            self.ProgDefinicionBuenPrograma = ttk.Label(ventana,image=self.DefinicionBuenPrograma,background="white")
            self.ProgDefinicionBuenPrograma.image = self.DefinicionBuenPrograma
            self.ProgDefinicionBuenPrograma.place(x=0,y=0)
            self.CaractBuenPrograma = PhotoImage(file="Programas/CaracteristicasBuenPrograma.gif")
            self.ProgCaractBuenPrograma = ttk.Label(ventana,image=self.CaractBuenPrograma,background="white")
            self.ProgCaractBuenPrograma.image = self.CaractBuenPrograma
            self.ProgCaractBuenPrograma.place(x=0,y=0)
            self.Documentacion = PhotoImage(file="Programas/DefinicionDocumentacion.gif")
            self.ProgDocumentacion = ttk.Label(ventana,image=self.Documentacion,background="white")
            self.ProgDocumentacion.image = self.Documentacion
            self.ProgDocumentacion.place(x=0,y=0)
            self.ComentarioEj = PhotoImage(file="Programas/EjemploComentario.gif")
            self.ProgComentarioEj = ttk.Label(ventana,image=self.ComentarioEj,background="white")
            self.ProgComentarioEj.image = self.ComentarioEj
            self.ProgComentarioEj.place(x=0,y=0)
            self.Resumen = PhotoImage(file="Programas/Resumen.gif")
            self.ProgResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.ProgResumen.image = self.Resumen
            self.ProgResumen.place(x=0,y=0)
            self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)
            self.notebook.add(self.ProgDefinicion1,text="Pag 1")
            self.notebook.add(self.ProgDefinicion2,text="Pag 2")
            self.notebook.add(self.ProgDefinicionCicloVida,text="Pag 3")
            self.notebook.add(self.ProgFasesCicloVida,text="Pag 4")
            self.notebook.add(self.ProgDefinicionBuenPrograma,text="Pag 5")
            self.notebook.add(self.ProgCaractBuenPrograma,text="Pag 6")
            self.notebook.add(self.ProgDocumentacion,text="Pag 7)")
            self.notebook.add(self.ProgComentarioEj,text="Pag 8")
            self.notebook.add(self.ProgResumen,text="Pag 9")
            self.notebook.pack()
    def Volver(self):
        self.ventanaTeoria.destroy()
        self.VT.deiconify()

    def Evaluacion(self):
        VentanaEva=Evaluacion(self.ventanaTeoria)