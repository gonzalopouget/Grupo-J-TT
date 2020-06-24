import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from Temas import Temas
class Categorias():
     def __init__(self, ventanaPrincipal):
          
        self.VP=ventanaPrincipal#Aqui se hace una instancia de la ventana principal que se paso vacia como parametro
        self.VP.withdraw()#Aqui esa ventana pasada como parametro e instanciada anteriormente se minimiza
        self.ventanaCategoria = tk.Toplevel(ventanaPrincipal)
        self.ventanaCategoria.title("Categorias")#Se le pone titulo#Aqui se crea la nueva ventana que pasa a ser una ventana hija de la ventana pasada como parametro a la ventana
        self.ventanaCategoria.geometry("320x160")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
        self.ventanaCategoria.resizable(0,0)#Se vuelve inmodificable el tamaño de la ventana
        self.ventanaCategoria.configure(bg="#024747")#Se cambia el color del fondo
        self.btnSalir = Button(self.ventanaCategoria, text='Volver',command=self.Volver).pack(side=BOTTOM)
        
        #Se crea  en la ventana una lista para elegir con las asignaturas o categorias
        self.Asignaturas = ttk.Combobox(self.ventanaCategoria, values=["Git", "Programacion Basica","Linea de Comandos"])
        #Se crea y se "empaqueta" en la ventana un label para mostrarle al usuario la lista de asignaturas
        self.lbl = Label(self.ventanaCategoria,text="Lista de Asignaturas",bg="#024747",fg="white",font=("Arial", 20))
        self.btnSelec = Button(self.ventanaCategoria,text="Seleccionar",command=self.VentanaTemas)#Se crea un boton para seleccionar el tema deseado
        self.lbl.pack(side=TOP)#Se "empaqueta el label"
        self.Asignaturas.pack()#Se "empaqueta" la lista con las asignaturas
        self.btnSelec.pack()#Se empaqueta el boton para seleccionar
        self.Asignaturas.current(0)#Tambien se configura para que por defecto muestre como a la primer asignatura
     
     def VentanaTemas(self):#Esta funcion es llamada cuando se aprieta el boton seleccionar.
        ventanaTemas=Temas(self.ventanaCategoria,self.Asignaturas)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con los temas correspondientes a la asignatura elegida.

     def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaCategoria.destroy()#Y lo que hace es cerrar la ventana Temas y 
        self.VP.deiconify()# reabrir la ventana anterior, en este caso la ventana principal.
            
         
        


     
   

        
