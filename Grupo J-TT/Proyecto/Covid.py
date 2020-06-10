import tkinter as tk
from tkinter import ttk
from tkinter import *

class Covid():

     def __init__(self, ventanaPrincipal):
        self.VP=ventanaPrincipal
        self.VP.withdraw()
        self.ventanaCovid = tk.Toplevel(ventanaPrincipal)
        self.ventanaCovid.title("Informacion sobre el Covid-19")
        self.ventanaCovid.resizable(0,0)
        self.ventanaCovid.geometry("640x400")
        self.ventanaCovid.configure(bg= '#024747')
        self.notebook=ttk.Notebook(self.ventanaCovid)
        self.btnSalir = Button(self.ventanaCovid,text="Volver",command=self.Volver).pack(side = BOTTOM,anchor =S)
        self.sintomas = PhotoImage(file="sintomas-coronavirus.gif")
        self.Covid_Sintomas = ttk.Label(self.ventanaCovid,image=self.sintomas)
        self.Covid_Sintomas.image = self.sintomas
        self.Covid_Sintomas.place(x=0,y=0)
        self.medidas = PhotoImage(file="unnamed.gif")
        self.Covid_Medidas = ttk.Label(self.ventanaCovid,image=self.medidas)
        self.Covid_Medidas.image = self.medidas
        self.Covid_Medidas.place(x=0,y=0)
        self.Covid_Info=tk.Frame(self.ventanaCovid)
        self.lblInfo=Label(self.Covid_Info,text="Mas Info en:")
        self.link = Button(self.Covid_Info,text="https://www.argentina.gob.ar/salud/coronavirus-COVID-19",command=self.clickearLink)
        self.lblInfo.pack()
        self.link.pack()
        self.notebook.add(self.Covid_Sintomas,text="Sintomas")
        self.notebook.add(self.Covid_Medidas,text="Medidas de Precaucion")
        self.notebook.add(self.Covid_Info,text="Mas informacion")
        self.notebook.pack()
     def clickearLink(self):
        import webbrowser
        webbrowser.open("https://www.argentina.gob.ar/salud/coronavirus-COVID-19")

     def Volver(self):
        self.ventanaCovid.destroy()
        self.VP.deiconify()