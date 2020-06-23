import tkinter as tk
from tkinter import ttk
from tkinter import *
from NavegandoSistemaArchivos.EvaluacionNaveSistArch import Evaluacion
class TeoriaNavSist():
    def __init__(self,ventana,temas):
            self.ventanaTeoria=ventana
            self.VT=temas
            self.ventanaTeoria.geometry("680x410")
            self.notebook=ttk.Notebook(ventana)

            self.Definicion = PhotoImage(file="NavegandoSistemaArchivos/Definicion.gif")
            self.NavSistDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.NavSistDefinicion.image = self.Definicion
            self.NavSistDefinicion.place(x=0,y=0)

            self.ls = PhotoImage(file="NavegandoSistemaArchivos/ls.gif")
            self.NavSistls = ttk.Label(ventana,image=self.ls,background="white")
            self.NavSistls.image = self.ls
            self.NavSistls.place(x=0,y=0)

            self.SistemaArchivos = PhotoImage(file="NavegandoSistemaArchivos/sistemaArchivos.gif")
            self.NavSistSistema = ttk.Label(ventana,image=self.SistemaArchivos,background="white")
            self.NavSistSistema.image = self.SistemaArchivos
            self.NavSistSistema.place(x=0,y=0)

            self.pwd = PhotoImage(file="NavegandoSistemaArchivos/pwd.gif")
            self.NavSistpwd = ttk.Label(ventana,image=self.pwd,background="white")
            self.NavSistpwd.image = self.pwd
            self.NavSistpwd.place(x=0,y=0)

            self.Cd1 = PhotoImage(file="NavegandoSistemaArchivos/cd1.gif")
            self.NavSistcd1 = ttk.Label(ventana,image=self.Cd1,background="white")
            self.NavSistcd1.image = self.Cd1
            self.NavSistcd1.place(x=0,y=0)

            self.Cd2 = PhotoImage(file="NavegandoSistemaArchivos/cd2.gif")
            self.NavSistcd2 = ttk.Label(ventana,image=self.Cd2,background="white")
            self.NavSistcd2.image = self.Cd2
            self.NavSistcd2.place(x=0,y=0)

            self.mkdir = PhotoImage(file="NavegandoSistemaArchivos/mkdir.gif")
            self.NavSistmkdir = ttk.Label(ventana,image=self.mkdir,background="white")
            self.NavSistmkdir.image = self.mkdir
            self.NavSistmkdir.place(x=0,y=0)

            self.touch = PhotoImage(file="NavegandoSistemaArchivos/touch.gif")
            self.NavSisttouch = ttk.Label(ventana,image=self.touch,background="white")
            self.NavSisttouch.image = self.touch
            self.NavSisttouch.place(x=0,y=0)

            self.Resumen = PhotoImage(file="NavegandoSistemaArchivos/Resumen.gif")
            self.NavSistResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.NavSistResumen.image = self.Resumen
            self.NavSistResumen.place(x=0,y=0)

            self.btnEvaluacion = Button(ventana,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(ventana, text='Volver',command=self.Volver).pack(side=BOTTOM)

            self.notebook.add(self.NavSistDefinicion,text="Pag 1")
            self.notebook.add(self.NavSistls,text="Pag 2")
            self.notebook.add(self.NavSistSistema,text="Pag 3")
            self.notebook.add(self.NavSistpwd,text="Pag 4")
            self.notebook.add(self.NavSistcd1,text="Pag 5")
            self.notebook.add(self.NavSistcd2,text="Pag 6")
            self.notebook.add(self.NavSistmkdir,text="Pag 7")
            self.notebook.add(self.NavSisttouch,text="Pag 8")
            self.notebook.add(self.NavSistResumen,text="Pag 9")
            self.notebook.pack()

    def Volver(self):
        self.ventanaTeoria.destroy()
        self.VT.deiconify()
    def Evaluacion(self):
        eva=Evaluacion(self.ventanaTeoria)
