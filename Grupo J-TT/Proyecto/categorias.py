import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from Temas import Temas
class Categorias():
     def __init__(self, ventanaPrincipal):
          
        self.VP=ventanaPrincipal
        self.VP.withdraw()

        self.ventanaCategoria = tk.Toplevel(ventanaPrincipal)

        self.ventanaCategoria.title("Categorias")

        self.ventanaCategoria.geometry("320x160")
        self.ventanaCategoria.resizable(0,0)

        self.ventanaCategoria.configure(bg="#024747")

        self.btnSalir = Button(self.ventanaCategoria, text='Volver',command=self.Volver).pack(side=BOTTOM)

        self.Asignaturas = ttk.Combobox(self.ventanaCategoria, values=["Git", "Programacion Basica","-En Proceso-"])

        self.lbl = Label(self.ventanaCategoria,text="Lista de Asignaturas",bg="#024747",fg="white",font=("Arial", 20))

        self.btnSelec = Button(self.ventanaCategoria,text="Seleccionar",command=self.VentanaTemas)

        self.lbl.pack(side=TOP)

        self.Asignaturas.pack()

        self.btnSelec.pack()

        self.Asignaturas.current(0)
     
     def VentanaTemas(self):
        ventanaTemas=Temas(self.ventanaCategoria,self.Asignaturas)

     def Volver(self):
        self.ventanaCategoria.destroy()
        self.VP.deiconify()
            
         
        


     
   

        
