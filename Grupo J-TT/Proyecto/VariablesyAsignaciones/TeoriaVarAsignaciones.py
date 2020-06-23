import tkinter as tk
from tkinter import ttk
from tkinter import *
from VariablesyAsignaciones.EvaluacionVarAsignaciones import Evaluacion
class TeoriaVarAsignaciones():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana#Aqui se hace una instancia de la ventana teoria que se paso vacia como parametro
            self.ventanaTeoria.geometry("680x540")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
            self.ventanaTeoria.configure(bg= '#024747')#Se cambia el color del fondo
            self.VT=Temas#Aqui se hace una instancia de la ventana Temas que se paso como parametro
            self.notebook=ttk.Notebook(ventana)#Dentro de la ventana se crea un notebook para gestionar paneles

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Definicion = PhotoImage(file="VariablesyAsignaciones/DefinicionVariable.gif")
            self.VarAsignaDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.VarAsignaDefinicion.image = self.Definicion
            self.VarAsignaDefinicion.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.DeclaracionInicializacion = PhotoImage(file="VariablesyAsignaciones/DeclaracionEInicializacion.gif")
            self.VarAsignaDeclaracionIni = ttk.Label(ventana,image=self.DeclaracionInicializacion,background="white")
            self.VarAsignaDeclaracionIni.image = self.DeclaracionInicializacion
            self.VarAsignaDeclaracionIni.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Asignacion = PhotoImage(file="VariablesyAsignaciones/Asignacion.gif")
            self.VarAsignaAsignacion = ttk.Label(ventana,image=self.Asignacion,background="white")
            self.VarAsignaAsignacion.image = self.Asignacion
            self.VarAsignaAsignacion.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Transferencia = PhotoImage(file="VariablesyAsignaciones/Transferencia.gif")
            self.VarAsignaTransferencia = ttk.Label(ventana,image=self.Transferencia,background="white")
            self.VarAsignaTransferencia.image = self.Transferencia
            self.VarAsignaTransferencia.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.EjInicializacion = PhotoImage(file="VariablesyAsignaciones/EjemplosInicializacion.gif")
            self.VarAsignaEjIni = ttk.Label(ventana,image=self.EjInicializacion,background="white")
            self.VarAsignaEjIni.image = self.EjInicializacion
            self.VarAsignaEjIni.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.RecomendacionesNombres = PhotoImage(file="VariablesyAsignaciones/RecomendacionesParaNombres.gif")
            self.VarAsignaRecomendacionNom = ttk.Label(ventana,image=self.RecomendacionesNombres,background="white")
            self.VarAsignaRecomendacionNom.image = self.RecomendacionesNombres
            self.VarAsignaRecomendacionNom.place(x=0,y=0)

            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Resumen = PhotoImage(file="VariablesyAsignaciones/Resumen.gif")
            self.VarAsignaResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.VarAsignaResumen.image = self.Resumen
            self.VarAsignaResumen.place(x=0,y=0)

            #Se crean dos botones, uno para crear la ventana con las preguntas y el otro para volver atras
            self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)

            #Se añaden como pestañas en el notebook los labels con las imagenes ya cargadas
            self.notebook.add(self.VarAsignaDefinicion,text="Pag 1")
            self.notebook.add(self.VarAsignaDeclaracionIni,text="Pag 2")
            self.notebook.add(self.VarAsignaEjIni,text="Pag 3")
            self.notebook.add(self.VarAsignaAsignacion,text="Pag 4")
            self.notebook.add(self.VarAsignaTransferencia,text="Pag 5")
            self.notebook.add(self.VarAsignaRecomendacionNom,text="Pag 6")
            self.notebook.add(self.VarAsignaResumen,text="Pag 7")
            self.notebook.pack()

    def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaTeoria.destroy()#Y lo que hace es cerrar la ventana Teoria y 
        self.VT.deiconify()# reabrir la ventana anterior, en este caso la ventana principal.
        
    def Evaluacion(self):# Esta funcion es llamada cuando se aprieta el boton Evaluacion de conceptos
         VentanaEva=Evaluacion(self.ventanaTeoria)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con las preguntas del tema elegido