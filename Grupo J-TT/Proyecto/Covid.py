import tkinter as tk
from tkinter import ttk
from tkinter import *
class Covid():
     def __init__(self, ventanaPrincipal):
        self.auxiliar=False

        self.ventanaCovid = tk.Toplevel(ventanaPrincipal)

        self.ventanaCovid.title("Informacion sobre el Covid-19")

        self.ventanaCovid.geometry("400x300")

        self.frameTitulo.pack(anchor=CENTER)

        self.frameTitulo.config(foreground="white",font=("Verdana",24))

        self.ventanaCovid.resizable(0,0)