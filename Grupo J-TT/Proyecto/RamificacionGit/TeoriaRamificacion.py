import tkinter as tk
from tkinter import ttk
from tkinter import *
from RamificacionGit.EvaluacionRamificacion import Evaluacion
class TeoriaRam():
    def __init__(self,ventana,temas):
            self.ventanaTeoria=ventana
            self.VT=temas
            self.ventanaTeoria.geometry("710x490")
            self.ventanaTeoria.configure(bg= '#024747')
            self.notebook=ttk.Notebook(ventana)

            self.Branch = PhotoImage(file="RamificacionGit/branch.gif")
            self.RamBranch = ttk.Label(ventana,image=self.Branch,background="white")
            self.RamBranch.image = self.Branch
            self.RamBranch.place(x=0,y=0)

            self.BranchResumen = PhotoImage(file="RamificacionGit/resumenRamificacion.gif")
            self.RamBranchResumen = ttk.Label(ventana,image=self.BranchResumen,background="white")
            self.RamBranchResumen.image = self.BranchResumen
            self.RamBranchResumen.place(x=0,y=0)

            self.Branch2 = PhotoImage(file="RamificacionGit/branch2.gif")
            self.RamBranch2 = ttk.Label(ventana,image=self.Branch2,background="white")
            self.RamBranch2.image = self.Branch2
            self.RamBranch2.place(x=0,y=0)

            self.Checkout = PhotoImage(file="RamificacionGit/checkout.gif")
            self.RamCheckout = ttk.Label(ventana,image=self.Checkout,background="white")
            self.RamCheckout.image = self.Checkout
            self.RamCheckout.place(x=0,y=0)

            self.Commit = PhotoImage(file="RamificacionGit/commit.gif")
            self.RamCommit = ttk.Label(ventana,image=self.Commit,background="white")
            self.RamCommit.image = self.Commit
            self.RamCommit.place(x=0,y=0)

            self.Merge = PhotoImage(file="RamificacionGit/merge.gif")
            self.RamMerge = ttk.Label(ventana,image=self.Merge,background="white")
            self.RamMerge.image = self.Merge
            self.RamMerge.place(x=0,y=0)

            self.MergeConflict = PhotoImage(file="RamificacionGit/mergeConflict.gif")
            self.RamMergeConf = ttk.Label(ventana,image=self.MergeConflict,background="white")
            self.RamMergeConf.image = self.MergeConflict
            self.RamMergeConf.place(x=0,y=0)

            self.Delete = PhotoImage(file="RamificacionGit/borrar.gif")
            self.RamDelete = ttk.Label(ventana,image=self.Delete,background="white")
            self.RamDelete.image = self.Delete
            self.RamDelete.place(x=0,y=0)

            self.Resumen = PhotoImage(file="RamificacionGit/Resumen.gif")
            self.RamResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.RamResumen.image = self.Resumen
            self.RamResumen.place(x=0,y=0)

            self.btnEvaluacion = Button(ventana,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(ventana, text='Volver',command=self.Volver).pack(side=BOTTOM)

            self.notebook.add(self.RamBranch,text="Pag 1")
            self.notebook.add(self.RamBranchResumen,text="Pag 2")
            self.notebook.add(self.RamBranch2,text="Pag 3")
            self.notebook.add(self.RamCheckout,text="Pag 4")
            self.notebook.add(self.RamCommit,text="Pag 5")
            self.notebook.add(self.RamMerge,text="Pag 6")
            self.notebook.add(self.RamMergeConf,text="Pag 7")
            self.notebook.add(self.RamDelete,text="Pag 8")
            self.notebook.add(self.RamResumen,text="Pag 9")
            self.notebook.pack()
    def Volver(self):
        self.ventanaTeoria.destroy()
        self.VT.deiconify()
    def Evaluacion(self):
        eva=Evaluacion(self.ventanaTeoria)
