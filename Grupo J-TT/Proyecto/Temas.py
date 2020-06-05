import tkinter as tk
from tkinter import ttk
from tkinter import *
from Teoria import Teoria
class Temas():

     def __init__(self, ventanaCategorias,Asignaturas):
        self.ventanaTemas = tk.Toplevel(ventanaCategorias)
        
        self.ventanaTemas.title("Temas")
        
        self.ventanaTemas.geometry("320x160")
        
        self.ventanaTemas.configure(bg="#024747")
        
        if(Asignaturas.get()=="-En Proceso-"):
            self.Temaslbl = Label(self.ventanaTemas,text="-En Proceso-",bg="#024747",fg="white",font=("Arial", 20))
            
            self.Temaslbl.pack()
            
            self.Temas = ttk.Combobox(self.ventanaTemas, values=["-En Proceso-", "-En Proceso-","-En Proceso-","-En Proceso-"])
            
            self.Temas.pack()
            
        elif(Asignaturas.get()=="Programacion Basica"):
            self.Temaslbl = Label(self.ventanaTemas,text="Fundamentos de Programacion",bg="#024747",fg="white",font=("Arial", 14))
            
            self.Temaslbl.pack()
            
            self.Temas = ttk.Combobox(self.ventanaTemas, values=["Algoritmos", "Programas","Lenguajes de Programacion","Tipos de datos primitivos","Variables y asignaciones","Expresiones","Control de flujo","Funciones y procedimientos","Recursion","Tipos de datos primitivos","Entrada y salida de datos"])

            self.Temas.pack()
            
            self.Temas.current(0)
            
            self.btnSelec = Button(self.ventanaTemas,text="Seleccionar",command=self.VentanaTeoria)
            
            self.btnSelec.pack()
        

     def VentanaTeoria (self):

         ventanaTeo=Teoria(self.ventanaTemas,self.Temas)
