import tkinter as tk
from tkinter import ttk
from tkinter import *
from TeoriaProgramacion import TeoriaProg
from TeoriaGit import TeoriaGit
from TeoriaLineaComandos import TeoriaLineaComandos
class Temas():

     def __init__(self, ventanaCategorias,Asignaturas):
        self.VC=ventanaCategorias#Aqui se hace una instancia de la ventana categorias que se paso como parametro
        self.VC.withdraw()#Aqui esa ventana pasada como parametro e instanciada anteriormente se minimiza
        self.ventanaTemas = tk.Toplevel(ventanaCategorias)#Aqui se crea la nueva ventana que pasa a ser una ventana hija de la ventana pasada como parametro
        self.ventanaTemas.title("Temas")#Se le pone titulo a la ventana
        self.ventanaTemas.geometry("320x160")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
        self.ventanaTemas.resizable(0,0)#Se vuelve inmodificable el tamaño de la ventana
        self.ventanaTemas.configure(bg="#024747")#Se cambia el color del fondo

        #Aqui se plantea el primer caso que puede existir cuando se haya elegido una asignatura,es decir,el caso donde
        #se haya elegido Git, y en consecuencia se va a proceder a crearse una ventana solo con los temas que le corresponden a Git
        
        if(Asignaturas.get()=="Git"):

            #Se crea y se "empaqueta" en la ventana un label para mostrarle al usuario la asignatura o categoria elegida
            self.Temaslbl = Label(self.ventanaTemas,text="Git",bg="#024747",fg="white",font=("Arial", 20))
            self.Temaslbl.pack()

            #Se crea un boton para salir de la ventana actual y volver a la anterior
            self.btnSalir = Button(self.ventanaTemas, text='Volver',command=self.Volver).pack(side=BOTTOM)

            #Se crea y se "empaqueta" en la ventana una lista para elegir con los temas que correspondad a Git
            self.Temas = ttk.Combobox(self.ventanaTemas, values=["Flujo de Trabajo basico", "Backtrack","Ramificacion","Trabajo en Equipo"])
            self.Temas.pack()
            self.Temas.current(0)#Tambien se configura para que por defecto muestre como la lista al primer Tema

            #Se crea un boton para seleccionar el tema deseado
            self.btnSelec = Button(self.ventanaTemas,text="Seleccionar",command=self.VentanaTeoriaGit)
            self.btnSelec.pack()

        #Aqui se plantea el segundo caso que puede existir cuando se haya elegido una asignatura,es decir,el caso donde
        #se haya elegido Programacion Basica, y en consecuencia se va a proceder a crearse una ventana solo con los temas que le corresponden a Programacion Basica

        elif(Asignaturas.get()=="Programacion Basica"):

            #Se crea y se "empaqueta" en la ventana un label para mostrarle al usuario la asignatura o categoria elegida
            self.Temaslbl = Label(self.ventanaTemas,text="Fundamentos de Programacion",bg="#024747",fg="white",font=("Arial", 14))
            self.Temaslbl.pack()

            #Se crea y se "empaqueta" en la ventana una lista para elegir con los temas que correspondad a Git
            self.Temas = ttk.Combobox(self.ventanaTemas, values=["Algoritmos", "Programas","Lenguajes de Programacion","Tipos de datos primitivos","Variables y Asignaciones","Expresiones","Control de flujo","Subrutinas","Recursion","Tipos de datos estructurados","Entrada y salida de datos","Manejo de Errores"])
            self.Temas.pack()

            #Se crea un boton para salir de la ventana actual y volver a la anterior
            self.btnSalir = Button(self.ventanaTemas, text='Volver',command=self.Volver).pack(side=BOTTOM)
            self.Temas.current(0)#Tambien se configura para que por defecto muestre como la lista al primer Tema

            #Se crea un boton para seleccionar el tema deseado
            self.btnSelec = Button(self.ventanaTemas,text="Seleccionar",command=self.VentanaTeoriaProg)
            self.btnSelec.pack()

        #Aqui se plantea el tercer caso que puede existir cuando se haya elegido una asignatura,es decir,el caso donde
        #se haya elegido Linea de Comandos, y en consecuencia se va a proceder a crearse una ventana solo con los temas que le corresponden a Linea de Comandos
        
        elif(Asignaturas.get()=="Linea de Comandos"):

            #Se crea y se "empaqueta" en la ventana un label para mostrarle al usuario la asignatura o categoria elegida
            self.Temaslbl = Label(self.ventanaTemas,text="Linea de Comandos",bg="#024747",fg="white",font=("Arial", 14))
            self.Temaslbl.pack()

            #Se crea y se "empaqueta" en la ventana una lista para elegir con los temas que correspondad a Git
            self.Temas = ttk.Combobox(self.ventanaTemas, values=["Navegar Sistema de Archivos", "Ver y Cambiar Sistema de Archivos","Redireccionando Entradas y Salidas","Configuracion de Entorno","Bash Scripting"])
            self.Temas.pack()

            #Se crea un boton para salir de la ventana actual y volver a la anterior
            self.btnSalir = Button(self.ventanaTemas, text='Volver',command=self.Volver).pack(side=BOTTOM)
            self.Temas.current(0)#Tambien se configura para que por defecto muestre como la lista al primer Tema

            #Se crea un boton para seleccionar el tema deseado
            self.btnSelec = Button(self.ventanaTemas,text="Seleccionar",command=self.VentanaTeoriaLineaComandos)
            self.btnSelec.pack()
        
     def VentanaTeoriaProg(self):#Esta funcion es llamada cuando se aprieta el boton seleccionar pero en el caso que se haya elegido Programacion Basica.
         ventanaTeo=TeoriaProg(self.ventanaTemas,self.Temas)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con la teoria del tema elegido.
     
     def VentanaTeoriaGit(self):#Esta funcion es llamada cuando se aprieta el boton seleccionar pero en el caso que se haya elegido Programacion Basica.
         ventanaTeo=TeoriaGit(self.ventanaTemas,self.Temas)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con la teoria del tema elegido.
     
     def VentanaTeoriaLineaComandos(self):#Esta funcion es llamada cuando se aprieta el boton seleccionar pero en el caso que se haya elegido Programacion Basica.
         ventanaTeo=TeoriaLineaComandos(self.ventanaTemas,self.Temas)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con la teoria del tema elegido.

     def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
         self.ventanaTemas.destroy()#Y lo que hace es cerrar la ventana Temas y 
         self.VC.deiconify()# reabrir la ventana anterior, en este caso la ventana principal.
