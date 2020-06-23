import tkinter as tk
from tkinter import ttk
from tkinter import *
from ConfigurandoEntorno.EvaluacionConfgEnt import Evaluacion
class TeoriaConfgEnt():
    def __init__(self,ventana,temas):
            self.ventanaTeoria=ventana
            self.VT=temas
            self.ventanaTeoria.geometry("680x410")
            self.notebook=ttk.Notebook(ventana)

            self.Nano = PhotoImage(file="ConfigurandoEntorno/nano.gif")
            self.ConfgEntNano = ttk.Label(ventana,image=self.Nano,background="white")
            self.ConfgEntNano.image = self.Nano
            self.ConfgEntNano.place(x=0,y=0)

            self.PerfilBash = PhotoImage(file="ConfigurandoEntorno/perfilBash.gif")
            self.ConfgEntPerfilBash = ttk.Label(ventana,image=self.PerfilBash,background="white")
            self.ConfgEntPerfilBash.image = self.PerfilBash
            self.ConfgEntPerfilBash.place(x=0,y=0)

            self.Alias1 = PhotoImage(file="ConfigurandoEntorno/alias1.gif")
            self.ConfgEntAlias1 = ttk.Label(ventana,image=self.Alias1,background="white")
            self.ConfgEntAlias1.image = self.Alias1
            self.ConfgEntAlias1.place(x=0,y=0)

            self.Alias2 = PhotoImage(file="ConfigurandoEntorno/alias2.gif")
            self.ConfgEntAlias2 = ttk.Label(ventana,image=self.Alias2,background="white")
            self.ConfgEntAlias2.image = self.Alias2
            self.ConfgEntAlias2.place(x=0,y=0)

            self.VariablesEntorno = PhotoImage(file="ConfigurandoEntorno/variablesEntorno.gif")
            self.ConfgEntVarEnt = ttk.Label(ventana,image=self.VariablesEntorno,background="white")
            self.ConfgEntVarEnt.image = self.VariablesEntorno
            self.ConfgEntVarEnt.place(x=0,y=0)

            self.Ps1 = PhotoImage(file="ConfigurandoEntorno/ps1.gif")
            self.ConfgEntPs1 = ttk.Label(ventana,image=self.Ps1,background="white")
            self.ConfgEntPs1.image = self.Ps1
            self.ConfgEntPs1.place(x=0,y=0)

            self.Home = PhotoImage(file="ConfigurandoEntorno/home.gif")
            self.ConfgEntHome = ttk.Label(ventana,image=self.Home,background="white")
            self.ConfgEntHome.image = self.Home
            self.ConfgEntHome.place(x=0,y=0)

            self.Path = PhotoImage(file="ConfigurandoEntorno/path.gif")
            self.ConfgEntPath = ttk.Label(ventana,image=self.Path,background="white")
            self.ConfgEntPath.image = self.Path
            self.ConfgEntPath.place(x=0,y=0)

            self.Env = PhotoImage(file="ConfigurandoEntorno/env.gif")
            self.ConfgEntEnv = ttk.Label(ventana,image=self.Env,background="white")
            self.ConfgEntEnv.image = self.Env
            self.ConfgEntEnv.place(x=0,y=0)

            self.Resumen = PhotoImage(file="ConfigurandoEntorno/Resumen.gif")
            self.ConfgEntResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.ConfgEntResumen.image = self.Resumen
            self.ConfgEntResumen.place(x=0,y=0)

            self.btnEvaluacion = Button(ventana,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(ventana, text='Volver',command=self.Volver).pack(side=BOTTOM)

            self.notebook.add(self.ConfgEntNano,text="Pag 1")
            self.notebook.add(self.ConfgEntPerfilBash,text="Pag 2")
            self.notebook.add(self.ConfgEntAlias1,text="Pag 3")
            self.notebook.add(self.ConfgEntAlias2,text="Pag 4")
            self.notebook.add(self.ConfgEntVarEnt,text="Pag 5")
            self.notebook.add(self.ConfgEntPs1,text="Pag 6")
            self.notebook.add(self.ConfgEntHome,text="Pag 7")
            self.notebook.add(self.ConfgEntPath,text="Pag 8")
            self.notebook.add(self.ConfgEntEnv,text="Pag 9")
            self.notebook.add(self.ConfgEntResumen,text="Pag 10")
            self.notebook.pack()
    def Volver(self):
        self.ventanaTeoria.destroy()
        self.VT.deiconify()
    def Evaluacion(self):
        eva=Evaluacion(self.ventanaTeoria)
