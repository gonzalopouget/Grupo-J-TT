import tkinter as tk
from tkinter import ttk
from tkinter import *
from NavegandoSistemaArchivos.EvaluacionNaveSistArch import Evaluacion
class TeoriaNavSist():
    def __init__(self,ventana,temas):
            self.ventanaTeoria=ventana#Aqui se hace una instancia de la ventana teoria que se paso vacia como parametro
            self.VT=temas#Aqui se hace una instancia de la ventana Temas que se paso como parametro
            self.ventanaTeoria.geometry("680x410")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
            self.ventanaTeoria.configure(bg= '#024747')#Se cambia el color del fondo
            self.notebook=ttk.Notebook(ventana)#Dentro de la ventana se crea un notebook para gestionar paneles

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Definicion = PhotoImage(file="NavegandoSistemaArchivos/Definicion.gif")
            self.NavSistDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.NavSistDefinicion.image = self.Definicion
            self.NavSistDefinicion.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.ls = PhotoImage(file="NavegandoSistemaArchivos/ls.gif")
            self.NavSistls = ttk.Label(ventana,image=self.ls,background="white")
            self.NavSistls.image = self.ls
            self.NavSistls.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.SistemaArchivos = PhotoImage(file="NavegandoSistemaArchivos/sistemaArchivos.gif")
            self.NavSistSistema = ttk.Label(ventana,image=self.SistemaArchivos,background="white")
            self.NavSistSistema.image = self.SistemaArchivos
            self.NavSistSistema.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.pwd = PhotoImage(file="NavegandoSistemaArchivos/pwd.gif")
            self.NavSistpwd = ttk.Label(ventana,image=self.pwd,background="white")
            self.NavSistpwd.image = self.pwd
            self.NavSistpwd.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Cd1 = PhotoImage(file="NavegandoSistemaArchivos/cd1.gif")
            self.NavSistcd1 = ttk.Label(ventana,image=self.Cd1,background="white")
            self.NavSistcd1.image = self.Cd1
            self.NavSistcd1.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Cd2 = PhotoImage(file="NavegandoSistemaArchivos/cd2.gif")
            self.NavSistcd2 = ttk.Label(ventana,image=self.Cd2,background="white")
            self.NavSistcd2.image = self.Cd2
            self.NavSistcd2.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.mkdir = PhotoImage(file="NavegandoSistemaArchivos/mkdir.gif")
            self.NavSistmkdir = ttk.Label(ventana,image=self.mkdir,background="white")
            self.NavSistmkdir.image = self.mkdir
            self.NavSistmkdir.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.touch = PhotoImage(file="NavegandoSistemaArchivos/touch.gif")
            self.NavSisttouch = ttk.Label(ventana,image=self.touch,background="white")
            self.NavSisttouch.image = self.touch
            self.NavSisttouch.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Resumen = PhotoImage(file="NavegandoSistemaArchivos/Resumen.gif")
            self.NavSistResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.NavSistResumen.image = self.Resumen
            self.NavSistResumen.place(x=0,y=0)

            #Se crean dos botones, uno para crear la ventana con las preguntas y el otro para volver atras
            self.btnEvaluacion = Button(ventana,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(ventana, text='Volver',command=self.Volver).pack(side=BOTTOM)

            #Se añaden como pestañas en el notebook los labels con las imagenes ya cargadas
            self.notebook.add(self.NavSistDefinicion,text="Pag 1")
            self.notebook.add(self.NavSistls,text="Pag 2")
            self.notebook.add(self.NavSistSistema,text="Pag 3")
            self.notebook.add(self.NavSistpwd,text="Pag 4")
            self.notebook.add(self.NavSistcd1,text="Pag 5")
            self.notebook.add(self.NavSistcd2,text="Pag 6")
            self.notebook.add(self.NavSistmkdir,text="Pag 7")
            self.notebook.add(self.NavSisttouch,text="Pag 8")
            self.notebook.add(self.NavSistResumen,text="Pag 9")
            self.notebook.pack()

    def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaTeoria.destroy()#Y lo que hace es cerrar la ventana Teoria y
        self.VT.deiconify()# reabrir la ventana anterior, en este caso la ventana principal.

    def Evaluacion(self):# Esta funcion es llamada cuando se aprieta el boton Evaluacion de conceptos
        eva=Evaluacion(self.ventanaTeoria)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con las preguntas del tema elegido
