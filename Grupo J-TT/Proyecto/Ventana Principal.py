import tkinter as tk
from tkinter import ttk
from tkinter import *
from Covid import Covid
from categorias import Categorias

class VentanaPrincipal:

    def Ventana(self):
        self.principal =  tk.Tk()
        self.principal.title("Educational Python")
        self.principal.resizable(0,0)
        self.principal.geometry("480x320")
        self.principal.configure(bg= '#024747')
        self.frameTitulo=ttk.Label(self.principal, text="Educational Python")
        self.frameTitulo.config(background = "#024747", foreground="white",font=("Verdana",32))
        self.frameTitulo.pack(anchor=CENTER)
        photo = PhotoImage(file = "geisinger-covid19-icon.gif")
        photoimage = photo.subsample(20,20)
        btnCovid = Button(self.principal,text= "Informacion sobre el Covid-19",image=photoimage,compound = LEFT,background="#3498DB",command=self.VentanaCovid).pack(side = BOTTOM)
        btnCategorias = Button(self.principal,text= "Seleccionar una Categoria",background="#3498DB",command=self.VentanaCategorias).pack()
        self.principal.mainloop()

    def VentanaCovid(self):
        ventanaC=Covid(self.principal)

    def VentanaCategorias(self):
        ventanaC2=Categorias(self.principal)


ventana = VentanaPrincipal()
ventana.Ventana()
