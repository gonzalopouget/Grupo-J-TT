import tkinter as tk
from tkinter import ttk
from tkinter import *

class Teoria():

    def __init__(self, ventanaTemas,Temas):
        self.ventanaTeoria = tk.Toplevel(ventanaTemas)
        self.ventanaTeoria.title("Teoria")
        self.ventanaTeoria.geometry("640x310")
        self.ventanaTeoria.configure(bg="#024747")
        if(Temas.get()=="Algoritmos"):
            self.NumeroTema = 0
            self.notebook=ttk.Notebook(self.ventanaTeoria)
            self.Definicion = PhotoImage(file="Algoritmos/Definicion.gif")
            self.AlgDefinicion = ttk.Label(self.ventanaTeoria,image=self.Definicion,background="white")
            self.AlgDefinicion.image = self.Definicion
            self.AlgDefinicion.place(x=0,y=0)
            self.Tipos = PhotoImage(file="Algoritmos/Tipos.gif")
            self.AlgTipos = ttk.Label(self.ventanaTeoria,image=self.Tipos,background="white")
            self.AlgTipos.image = self.Tipos
            self.AlgTipos.place(x=0,y=0)
            self.Tecnicas1 = PhotoImage(file="Algoritmos/TecnicasDiseño1.gif")
            self.AlgTecnicas1 = ttk.Label(self.ventanaTeoria,image=self.Tecnicas1,background="white")
            self.AlgTecnicas1.image = self.Tecnicas1
            self.AlgTecnicas1.place(x=0,y=0)
            self.Tecnicas2 = PhotoImage(file="Algoritmos/TecnicasDiseño2.gif")
            self.AlgTecnicas2 = ttk.Label(self.ventanaTeoria,image=self.Tecnicas2,background="white")
            self.AlgTecnicas2.image = self.Tecnicas2
            self.AlgTecnicas2.place(x=0,y=0)
            self.Representacion = PhotoImage(file="Algoritmos/Representacion.gif")
            self.AlgRepresentacion = ttk.Label(self.ventanaTeoria,image=self.Representacion,background="white")
            self.AlgRepresentacion.image = self.Representacion
            self.AlgRepresentacion.place(x=0,y=0)
            self.Resumen = PhotoImage(file="Algoritmos/Resumen.gif")
            self.AlgResumen = ttk.Label(self.ventanaTeoria,image=self.Resumen,background="white")
            self.AlgResumen.image = self.Resumen
            self.AlgResumen.place(x=0,y=0)
            self.notebook.add(self.AlgDefinicion,text="Definicion")
            self.notebook.add(self.AlgTipos,text="Tipos")
            self.notebook.add(self.AlgTecnicas1,text="Tecnicas de diseño(Pagina 1)")
            self.notebook.add(self.AlgTecnicas2,text="Tecnicas de diseño(Pagina 2)")
            self.notebook.add(self.AlgRepresentacion,text="Representacion")
            self.notebook.add(self.AlgResumen,text="Resumen")
            self.notebook.pack()
