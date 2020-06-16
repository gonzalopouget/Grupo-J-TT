import tkinter as tk
from tkinter import ttk
from tkinter import *
from Teoria import Teoria
class Temas():

     def __init__(self, ventanaCategorias,Asignaturas):
        self.VC=ventanaCategorias
        self.VC.withdraw()

        self.ventanaTemas = tk.Toplevel(ventanaCategorias)
        
        self.ventanaTemas.title("Temas")
        
        self.ventanaTemas.geometry("320x160")
        self.ventanaTemas.resizable(0,0)
        
        self.ventanaTemas.configure(bg="#024747")
        
        if(Asignaturas.get()=="-En Proceso-"):
            self.Temaslbl = Label(self.ventanaTemas,text="-En Proceso-",bg="#024747",fg="white",font=("Arial", 20))
            
            self.Temaslbl.pack()
            self.btnSalir = Button(self.ventanaTemas, text='Volver',command=self.Volver).pack(side=BOTTOM)
            
            self.Temas = ttk.Combobox(self.ventanaTemas, values=["-En Proceso-", "-En Proceso-","-En Proceso-","-En Proceso-"])
            
            self.Temas.pack()
            
        elif(Asignaturas.get()=="Programacion Basica"):
            self.Temaslbl = Label(self.ventanaTemas,text="Fundamentos de Programacion",bg="#024747",fg="white",font=("Arial", 14))
            
            self.Temaslbl.pack()
            
            self.Temas = ttk.Combobox(self.ventanaTemas, values=["Algoritmos", "Programas","Lenguajes de Programacion","Tipos de datos primitivos","Variables y Asignaciones","Expresiones","Control de flujo","Subrutinas","Recursion","Tipos de datos estructurados","Entrada y salida de datos","Manejo de Errores"])
            self.Temas.pack()
            self.btnSalir = Button(self.ventanaTemas, text='Volver',command=self.Volver).pack(side=BOTTOM)
            
            self.Temas.current(0)
            
            self.btnSelec = Button(self.ventanaTemas,text="Seleccionar",command=self.VentanaTeoria)
            
            self.btnSelec.pack()
        

     def VentanaTeoria (self):

         ventanaTeo=Teoria(self.ventanaTemas,self.Temas)
     def Volver(self):
         self.ventanaTemas.destroy()
         self.VC.deiconify()
