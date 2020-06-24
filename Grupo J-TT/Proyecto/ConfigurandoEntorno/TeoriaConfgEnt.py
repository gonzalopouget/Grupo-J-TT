import tkinter as tk
from tkinter import ttk
from tkinter import *
from ConfigurandoEntorno.EvaluacionConfgEnt import Evaluacion
class TeoriaConfgEnt():
    def __init__(self,ventana,temas):
            self.ventanaTeoria=ventana#Aqui se hace una instancia de la ventana teoria que se paso vacia como parametro
            self.VT=temas#Aqui se hace una instancia de la ventana Temas que se paso como parametro
            self.ventanaTeoria.geometry("680x410")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
            self.ventanaTeoria.configure(bg= '#024747')#Se cambia el color del fondo
            self.notebook=ttk.Notebook(ventana)#Dentro de la ventana se crea un notebook para gestionar paneles

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Nano = PhotoImage(file="ConfigurandoEntorno/nano.gif")
            self.ConfgEntNano = ttk.Label(ventana,image=self.Nano,background="white")
            self.ConfgEntNano.image = self.Nano
            self.ConfgEntNano.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.PerfilBash = PhotoImage(file="ConfigurandoEntorno/perfilBash.gif")
            self.ConfgEntPerfilBash = ttk.Label(ventana,image=self.PerfilBash,background="white")
            self.ConfgEntPerfilBash.image = self.PerfilBash
            self.ConfgEntPerfilBash.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Alias1 = PhotoImage(file="ConfigurandoEntorno/alias1.gif")
            self.ConfgEntAlias1 = ttk.Label(ventana,image=self.Alias1,background="white")
            self.ConfgEntAlias1.image = self.Alias1
            self.ConfgEntAlias1.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Alias2 = PhotoImage(file="ConfigurandoEntorno/alias2.gif")
            self.ConfgEntAlias2 = ttk.Label(ventana,image=self.Alias2,background="white")
            self.ConfgEntAlias2.image = self.Alias2
            self.ConfgEntAlias2.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.VariablesEntorno = PhotoImage(file="ConfigurandoEntorno/variablesEntorno.gif")
            self.ConfgEntVarEnt = ttk.Label(ventana,image=self.VariablesEntorno,background="white")
            self.ConfgEntVarEnt.image = self.VariablesEntorno
            self.ConfgEntVarEnt.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Ps1 = PhotoImage(file="ConfigurandoEntorno/ps1.gif")
            self.ConfgEntPs1 = ttk.Label(ventana,image=self.Ps1,background="white")
            self.ConfgEntPs1.image = self.Ps1
            self.ConfgEntPs1.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Home = PhotoImage(file="ConfigurandoEntorno/home.gif")
            self.ConfgEntHome = ttk.Label(ventana,image=self.Home,background="white")
            self.ConfgEntHome.image = self.Home
            self.ConfgEntHome.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Path = PhotoImage(file="ConfigurandoEntorno/path.gif")
            self.ConfgEntPath = ttk.Label(ventana,image=self.Path,background="white")
            self.ConfgEntPath.image = self.Path
            self.ConfgEntPath.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Env = PhotoImage(file="ConfigurandoEntorno/env.gif")
            self.ConfgEntEnv = ttk.Label(ventana,image=self.Env,background="white")
            self.ConfgEntEnv.image = self.Env
            self.ConfgEntEnv.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Resumen = PhotoImage(file="ConfigurandoEntorno/Resumen.gif")
            self.ConfgEntResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.ConfgEntResumen.image = self.Resumen
            self.ConfgEntResumen.place(x=0,y=0)

            #Se crean dos botones, uno para crear la ventana con las preguntas y el otro para volver atras
            self.btnEvaluacion = Button(ventana,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(ventana, text='Volver',command=self.Volver).pack(side=BOTTOM)

            #Se añaden como pestañas en el notebook los labels con las imagenes ya cargadas
            self.notebook.add(self.ConfgEntNano,text="Pag 1")
            self.notebook.add(self.ConfgEntPerfilBash,text="Pag 2")
            self.notebook.add(self.ConfgEntAlias1,text="Pag 3")
            self.notebook.add(self.ConfgEntAlias2,text="Pag 4")
            self.notebook.add(self.ConfgEntVarEnt,text="Pag 5")
            self.notebook.add(self.ConfgEntPs1,text="Pag 6")
            self.notebook.add(self.ConfgEntHome,text="Pag 7")
            self.notebook.add(self.ConfgEntPath,text="Pag 8")
            self.notebook.add(self.ConfgEntEnv,text="Pag 9")
            self.notebook.add(self.ConfgEntResumen,text="Pag 10")
            self.notebook.pack()

    def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaTeoria.destroy()#Y lo que hace es cerrar la ventana Teoria y 
        self.VT.deiconify()# reabrir la ventana anterior, en este caso la ventana temas

    def Evaluacion(self):# Esta funcion es llamada cuando se aprieta el boton Evaluacion de conceptos
        eva=Evaluacion(self.ventanaTeoria)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con las preguntas del tema elegido
