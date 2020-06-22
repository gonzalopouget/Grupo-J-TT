import tkinter as tk
from tkinter import ttk
from tkinter import *
from FlujodeTrabajobasicoGit.EvaluacionFlujoTrabajoBasico import Evaluacion
class TeoriaFlujo():
    def __init__(self,ventana,temas):
            self.ventanaTeoria=ventana
            self.VT=temas
            self.ventanaTeoria.geometry("840x530")
            self.ventanaTeoria.configure(bg= '#024747')
            self.notebook=ttk.Notebook(ventana)

            self.Init = PhotoImage(file="FlujodeTrabajobasicoGit/Init.gif")
            self.FlujoTBInit = ttk.Label(ventana,image=self.Init,background="white")
            self.FlujoTBInit.image = self.Init
            self.FlujoTBInit.place(x=0,y=0)

            self.Flujo = PhotoImage(file="FlujodeTrabajobasicoGit/flujotrabajo.gif")
            self.FlujoTBFlujo = ttk.Label(ventana,image=self.Flujo,background="white")
            self.FlujoTBFlujo.image = self.Flujo
            self.FlujoTBFlujo.place(x=0,y=0)

            self.FlujoImg = PhotoImage(file="FlujodeTrabajobasicoGit/fa.gif")
            self.FlujoTBFlujoImg = ttk.Label(ventana,image=self.FlujoImg,background="white")
            self.FlujoTBFlujoImg.image = self.FlujoImg
            self.FlujoTBFlujoImg.place(x=0,y=0)

            self.Status = PhotoImage(file="FlujodeTrabajobasicoGit/status.gif")
            self.FlujoTBStatus = ttk.Label(ventana,image=self.Status,background="white")
            self.FlujoTBStatus.image = self.Status
            self.FlujoTBStatus.place(x=0,y=0)

            self.Add = PhotoImage(file="FlujodeTrabajobasicoGit/add.gif")
            self.FlujoTBAdd = ttk.Label(ventana,image=self.Add,background="white")
            self.FlujoTBAdd.image = self.Add
            self.FlujoTBAdd.place(x=0,y=0)
            
            self.Diff = PhotoImage(file="FlujodeTrabajobasicoGit/diff.gif")
            self.FlujoTBDiff = ttk.Label(ventana,image=self.Diff,background="white")
            self.FlujoTBDiff.image = self.Diff
            self.FlujoTBDiff.place(x=0,y=0)

            self.Commit = PhotoImage(file="FlujodeTrabajobasicoGit/commit.gif")
            self.FlujoTBCommit = ttk.Label(ventana,image=self.Commit,background="white")
            self.FlujoTBCommit.image = self.Commit
            self.FlujoTBCommit.place(x=0,y=0)

            self.Log = PhotoImage(file="FlujodeTrabajobasicoGit/log.gif")
            self.FlujoTBLog = ttk.Label(ventana,image=self.Log,background="white")
            self.FlujoTBLog.image = self.Log
            self.FlujoTBLog.place(x=0,y=0)

            self.Resumen = PhotoImage(file="FlujodeTrabajobasicoGit/Resumen.gif")
            self.FlujoTBResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.FlujoTBResumen.image = self.Resumen
            self.FlujoTBResumen.place(x=0,y=0)

            self.btnEvaluacion = Button(ventana,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(ventana, text='Volver',command=self.Volver).pack(side=BOTTOM)
            
            self.notebook.add(self.FlujoTBInit,text="Pag 1")
            self.notebook.add(self.FlujoTBFlujo,text="Pag 2")
            self.notebook.add(self.FlujoTBFlujoImg,text="Pag 3")
            self.notebook.add(self.FlujoTBStatus,text="Pag 4")
            self.notebook.add(self.FlujoTBAdd,text="Pag 5")
            self.notebook.add(self.FlujoTBDiff,text="Pag 6")
            self.notebook.add(self.FlujoTBCommit,text="Pag 7")
            self.notebook.add(self.FlujoTBLog,text="Pag 8")
            self.notebook.add(self.FlujoTBResumen,text="Pag 9")
            self.notebook.pack()
    def Volver(self):
        self.ventanaTeoria.destroy()
        self.VT.deiconify()
    def Evaluacion(self):
        eva=Evaluacion(self.ventanaTeoria)