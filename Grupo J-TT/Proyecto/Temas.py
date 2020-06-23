import tkinter as tk
from tkinter import ttk
from tkinter import *
from TeoriaProgramacion import TeoriaProg
from TeoriaGit import TeoriaGit
from TeoriaLineaComandos import TeoriaLineaComandos
class Temas():

     def __init__(self, ventanaCategorias,Asignaturas):
        self.VC=ventanaCategorias
        self.VC.withdraw()

        self.ventanaTemas = tk.Toplevel(ventanaCategorias)
        
        self.ventanaTemas.title("Temas")
        
        self.ventanaTemas.geometry("320x160")
        self.ventanaTemas.resizable(0,0)
        
        self.ventanaTemas.configure(bg="#024747")
        
        if(Asignaturas.get()=="Git"):
            self.Temaslbl = Label(self.ventanaTemas,text="Git",bg="#024747",fg="white",font=("Arial", 20))
            self.Temaslbl.pack()
            self.btnSalir = Button(self.ventanaTemas, text='Volver',command=self.Volver).pack(side=BOTTOM)
            self.Temas = ttk.Combobox(self.ventanaTemas, values=["Flujo de Trabajo basico", "Backtrack","Ramificacion","Trabajo en Equipo"])
            self.Temas.pack()
            self.Temas.current(0)
            self.btnSelec = Button(self.ventanaTemas,text="Seleccionar",command=self.VentanaTeoriaGit)
            self.btnSelec.pack()
            
        elif(Asignaturas.get()=="Programacion Basica"):
            self.Temaslbl = Label(self.ventanaTemas,text="Fundamentos de Programacion",bg="#024747",fg="white",font=("Arial", 14))
            self.Temaslbl.pack()
            self.Temas = ttk.Combobox(self.ventanaTemas, values=["Algoritmos", "Programas","Lenguajes de Programacion","Tipos de datos primitivos","Variables y Asignaciones","Expresiones","Control de flujo","Subrutinas","Recursion","Tipos de datos estructurados","Entrada y salida de datos","Manejo de Errores"])
            self.Temas.pack()
            self.btnSalir = Button(self.ventanaTemas, text='Volver',command=self.Volver).pack(side=BOTTOM)
            self.Temas.current(0)
            self.btnSelec = Button(self.ventanaTemas,text="Seleccionar",command=self.VentanaTeoriaProg)
            self.btnSelec.pack()
        elif(Asignaturas.get()=="Linea de Comandos"):
            self.Temaslbl = Label(self.ventanaTemas,text="Linea de Comandos",bg="#024747",fg="white",font=("Arial", 14))
            self.Temaslbl.pack()
            self.Temas = ttk.Combobox(self.ventanaTemas, values=["Navegar Sistema de Archivos", "Ver y Cambiar Sistema de Archivos","Redireccionando Entradas y Salidas","Configuracion de Entorno","Bash Scripting"])
            self.Temas.pack()
            self.btnSalir = Button(self.ventanaTemas, text='Volver',command=self.Volver).pack(side=BOTTOM)
            self.Temas.current(0)
            self.btnSelec = Button(self.ventanaTemas,text="Seleccionar",command=self.VentanaTeoriaLineaComandos)
            self.btnSelec.pack()
        
        

     def VentanaTeoriaProg(self):
         ventanaTeo=Teoria(self.ventanaTemas,self.Temas)
     def VentanaTeoriaGit(self):
         ventanaTeo=TeoriaGit(self.ventanaTemas,self.Temas)
     def VentanaTeoriaLineaComandos(self):
         ventanaTeo=TeoriaLineaComandos(self.ventanaTemas,self.Temas)
     def Volver(self):
         self.ventanaTemas.destroy()
         self.VC.deiconify()
