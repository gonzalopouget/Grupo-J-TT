import tkinter as tk
from tkinter import ttk
from tkinter import *
from BacktrackGit.EvaluacionBacktrack import Evaluacion
class TeoriaBacktrack():
    def __init__(self,ventana,temas):
            self.ventanaTeoria=ventana
            self.VT=temas
            self.ventanaTeoria.geometry("700x500")
            self.ventanaTeoria.configure(bg= '#024747')
            self.notebook=ttk.Notebook(ventana)

            self.HeadCommit = PhotoImage(file="BacktrackGit/headcommit.gif")
            self.BacktrackHeadCommit = ttk.Label(ventana,image=self.HeadCommit,background="white")
            self.BacktrackHeadCommit.image = self.HeadCommit
            self.BacktrackHeadCommit.place(x=0,y=0)

            self.Checkout = PhotoImage(file="BacktrackGit/checkout.gif")
            self.BacktrackCheckout = ttk.Label(ventana,image=self.Checkout,background="white")
            self.BacktrackCheckout.image = self.Checkout
            self.BacktrackCheckout.place(x=0,y=0)

            self.Add = PhotoImage(file="BacktrackGit/add.gif")
            self.BacktrackAdd = ttk.Label(ventana,image=self.Add,background="white")
            self.BacktrackAdd.image = self.Add
            self.BacktrackAdd.place(x=0,y=0)

            self.Reset1 = PhotoImage(file="BacktrackGit/reset1.gif")
            self.BacktrackReset1 = ttk.Label(ventana,image=self.Reset1,background="white")
            self.BacktrackReset1.image = self.Reset1
            self.BacktrackReset1.place(x=0,y=0)

            self.Reset2 = PhotoImage(file="BacktrackGit/reset2.gif")
            self.BacktrackReset2 = ttk.Label(ventana,image=self.Reset2,background="white")
            self.BacktrackReset2.image = self.Reset2
            self.BacktrackReset2.place(x=0,y=0)

            self.ResetResumen = PhotoImage(file="BacktrackGit/resetResumen.gif")
            self.BacktrackResetResumen = ttk.Label(ventana,image=self.ResetResumen,background="white")
            self.BacktrackResetResumen.image = self.ResetResumen
            self.BacktrackResetResumen.place(x=0,y=0)

            self.Resumen = PhotoImage(file="BacktrackGit/Resumen.gif")
            self.BacktrackResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.BacktrackResumen.image = self.Resumen
            self.BacktrackResumen.place(x=0,y=0)

            self.btnEvaluacion = Button(ventana,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(ventana, text='Volver',command=self.Volver).pack(side=BOTTOM)

            self.notebook.add(self.BacktrackHeadCommit,text="Pag 1")
            self.notebook.add(self.BacktrackCheckout,text="Pag 2")
            self.notebook.add(self.BacktrackAdd,text="Pag 3")
            self.notebook.add(self.BacktrackReset1,text="Pag 4")
            self.notebook.add(self.BacktrackReset2,text="Pag 5")
            self.notebook.add(self.BacktrackResetResumen,text="Pag 6")
            self.notebook.add(self.BacktrackResumen,text="Pag 7")
            self.notebook.pack()
    def Volver(self):
        self.ventanaTeoria.destroy()
        self.VT.deiconify()
    def Evaluacion(self):
        eva=Evaluacion(self.ventanaTeoria)