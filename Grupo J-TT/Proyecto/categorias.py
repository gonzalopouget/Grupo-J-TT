import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

class Categorias():
     def __init__(self, ventanaPrincipal):
          
        ventanaPrincipal.iconify()

        self.ventanaCategoria = tk.Toplevel(ventanaPrincipal)

        self.ventanaCategoria.title("Categorias")

        self.ventanaCategoria.geometry("640x480")

        self.btnSalir = Button(self.ventanaCategoria, text='Salir',command=self.ventanaCategoria.destroy).pack(side=BOTTOM)

        self.Asignaturas = ttk.Combobox(self.ventanaCategoria, values=["Aritmetica", "Programacion Basica","Geometria","Trigonometria"])

        self.lbl = Label(self.ventanaCategoria,text="Lista de Asignaturas",bg="#483D8B",fg="white",font=("Arial", 20))

        self.btnSelec = Button(self.ventanaCategoria,text="Seleccionar",command=self.funcionPrueba)

        self.lbl.pack(side=TOP)

        self.Asignaturas.pack()

        self.btnSelec.pack()

        self.Asignaturas.current(1)
     
     def funcionPrueba(self):
        messagebox.showinfo(message=self.Asignaturas.get(), title="Asignatura Seleccionada")
            
         
        


     
   

        
