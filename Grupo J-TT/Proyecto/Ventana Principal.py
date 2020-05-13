import tkinter as tk
from tkinter import ttk
from tkinter import *
from Covid import Covid
class VentanaPrincipal:
    def Ventana(self):
        self.principal =  tk.Tk()

        self.principal.title("Educational Python")

        self.principal.resizable(0,0)

        self.principal.geometry("800x600")

        self.principal.configure(bg= 'black')

        self.frameTitulo=ttk.Label(self.principal, text="Educational Python")

        self.frameTitulo.config(background = "black", foreground="white",font=("Verdana",32))

        self.frameTitulo.pack(anchor=CENTER)

        photo = PhotoImage(file = r"C:\Users\Gonza\Desktop\Nueva carpeta (4)\geisinger-covid19-icon.gif")

        photoimage = photo.subsample(20,20)

        btnCovid = Button(self.principal,text= "Informacion sobre el Covid-19",image=photoimage,compound = LEFT,background="red",command=self.VentanaCovid).pack(side = BOTTOM)

        self.principal.mainloop()

    def VentanaCovid(self):
        ventanaC=Covid(self.principal)

ventana = VentanaPrincipal()
ventana.Ventana()

