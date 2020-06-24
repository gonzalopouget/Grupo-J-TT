import tkinter as tk
from tkinter import ttk
from tkinter import *
from RedireccionandoEntradaSalida.EvaluacionRedireccEntSal import Evaluacion
class TeoriaRedireccEntSal():
    def __init__(self,ventana,temas):
            self.ventanaTeoria=ventana#Aqui se hace una instancia de la ventana teoria que se paso vacia como parametro
            self.VT=temas#Aqui se hace una instancia de la ventana Temas que se paso como parametro
            self.ventanaTeoria.geometry("680x410")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
            self.ventanaTeoria.configure(bg= '#024747')#Se cambia el color del fondo
            self.notebook=ttk.Notebook(ventana)#Dentro de la ventana se crea un notebook para gestionar paneles

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.StdinStdoutStderr = PhotoImage(file="RedireccionandoEntradaSalida/stdinStdoutStderr.gif")
            self.RedireccEntSalStdInOutDerr = ttk.Label(ventana,image=self.StdinStdoutStderr,background="white")
            self.RedireccEntSalStdInOutDerr.image = self.StdinStdoutStderr
            self.RedireccEntSalStdInOutDerr.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Redireccion = PhotoImage(file="RedireccionandoEntradaSalida/redireccion.gif")
            self.RedireccEntSalRedir = ttk.Label(ventana,image=self.Redireccion,background="white")
            self.RedireccEntSalRedir.image = self.Redireccion
            self.RedireccEntSalRedir.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Mayor = PhotoImage(file="RedireccionandoEntradaSalida/comandoMayor.gif")
            self.RedireccEntSalMayor = ttk.Label(ventana,image=self.Mayor,background="white")
            self.RedireccEntSalMayor.image = self.Mayor
            self.RedireccEntSalMayor.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.DobleMayor = PhotoImage(file="RedireccionandoEntradaSalida/comandoDobleMayor.gif")
            self.RedireccEntSalDobleMayor = ttk.Label(ventana,image=self.DobleMayor,background="white")
            self.RedireccEntSalDobleMayor.image = self.DobleMayor
            self.RedireccEntSalDobleMayor.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Menor = PhotoImage(file="RedireccionandoEntradaSalida/comandoMenor.gif")
            self.RedireccEntSalMenor = ttk.Label(ventana,image=self.Menor,background="white")
            self.RedireccEntSalMenor.image = self.Menor
            self.RedireccEntSalMenor.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Tubo = PhotoImage(file="RedireccionandoEntradaSalida/comandoTubo.gif")
            self.RedireccEntSalTubo = ttk.Label(ventana,image=self.Tubo,background="white")
            self.RedireccEntSalTubo.image = self.Tubo
            self.RedireccEntSalTubo.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Sort = PhotoImage(file="RedireccionandoEntradaSalida/sort.gif")
            self.RedireccEntSalSort = ttk.Label(ventana,image=self.Sort,background="white")
            self.RedireccEntSalSort.image = self.Sort
            self.RedireccEntSalSort.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Uniq = PhotoImage(file="RedireccionandoEntradaSalida/uniq.gif")
            self.RedireccEntSalUniq = ttk.Label(ventana,image=self.Uniq,background="white")
            self.RedireccEntSalUniq.image = self.Uniq
            self.RedireccEntSalUniq.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Grep1 = PhotoImage(file="RedireccionandoEntradaSalida/grep1.gif")
            self.RedireccEntSalGrep1 = ttk.Label(ventana,image=self.Grep1,background="white")
            self.RedireccEntSalGrep1.image = self.Grep1
            self.RedireccEntSalGrep1.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Grep2 = PhotoImage(file="RedireccionandoEntradaSalida/grep2.gif")
            self.RedireccEntSalGrep2 = ttk.Label(ventana,image=self.Grep2,background="white")
            self.RedireccEntSalGrep2.image = self.Grep2
            self.RedireccEntSalGrep2.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Sed = PhotoImage(file="RedireccionandoEntradaSalida/sed.gif")
            self.RedireccEntSalSed = ttk.Label(ventana,image=self.Sed,background="white")
            self.RedireccEntSalSed.image = self.Sed
            self.RedireccEntSalSed.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Resumen = PhotoImage(file="RedireccionandoEntradaSalida/Resumen.gif")
            self.RedireccEntSalResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.RedireccEntSalResumen.image = self.Resumen
            self.RedireccEntSalResumen.place(x=0,y=0)

            #Se crean dos botones, uno para crear la ventana con las preguntas y el otro para volver atras
            self.btnEvaluacion = Button(ventana,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(ventana, text='Volver',command=self.Volver).pack(side=BOTTOM)

            #Se añaden como pestañas en el notebook los labels con las imagenes ya cargadas
            self.notebook.add(self.RedireccEntSalStdInOutDerr,text="Pag 1")
            self.notebook.add(self.RedireccEntSalRedir,text="Pag 2")
            self.notebook.add(self.RedireccEntSalMayor,text="Pag 3")
            self.notebook.add(self.RedireccEntSalDobleMayor,text="Pag 4")
            self.notebook.add(self.RedireccEntSalMenor,text="Pag 5")
            self.notebook.add(self.RedireccEntSalTubo,text="Pag 6")
            self.notebook.add(self.RedireccEntSalSort,text="Pag 7")
            self.notebook.add(self.RedireccEntSalUniq,text="Pag 8")
            self.notebook.add(self.RedireccEntSalGrep1,text="Pag 9")
            self.notebook.add(self.RedireccEntSalGrep2,text="Pag 10")
            self.notebook.add(self.RedireccEntSalSed,text="Pag 11")
            self.notebook.add(self.RedireccEntSalResumen,text="Pag 12")
            self.notebook.pack()

    def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaTeoria.destroy()#Y lo que hace es cerrar la ventana Teoria y
        self.VT.deiconify()# reabrir la ventana anterior, en este caso la ventana principal.

    def Evaluacion(self):# Esta funcion es llamada cuando se aprieta el boton Evaluacion de conceptos
        eva=Evaluacion(self.ventanaTeoria)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con las preguntas del tema elegido
