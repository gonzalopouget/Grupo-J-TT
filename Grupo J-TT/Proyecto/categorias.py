import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from Temas import Temas
class Categorias():
     def __init__(self, ventanaPrincipal):
          
        ventanaPrincipal.iconify()

        self.ventanaCategoria = tk.Toplevel(ventanaPrincipal)

        self.ventanaCategoria.title("Categorias")

        self.ventanaCategoria.geometry("640x480")

        self.ventanaCategoria.configure(bg="#024747")

        self.btnSalir = Button(self.ventanaCategoria, text='Salir',command=self.ventanaCategoria.destroy).pack(side=BOTTOM)

        self.Asignaturas = ttk.Combobox(self.ventanaCategoria, values=["-En Proceso-", "Programacion Basica","-En Proceso-","-En Proceso-"])

        self.lbl = Label(self.ventanaCategoria,text="Lista de Asignaturas",bg="#024747",fg="white",font=("Arial", 20))

        self.btnSelec = Button(self.ventanaCategoria,text="Seleccionar",command=self.VentanaTemas)

        self.lbl.pack(side=TOP)

        self.Asignaturas.pack()

        self.btnSelec.pack()

        self.Asignaturas.current(1)
     
     def VentanaTemas(self):
        ventanaTemas=Temas(self.ventanaCategoria,self.Asignaturas)
            
         
        


     
   

        
