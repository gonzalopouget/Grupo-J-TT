import tkinter as tk
from tkinter import ttk
from tkinter import *
from DatosEstructurados.EvaluacionDatosEstruct import Evaluacion
class TeoriaDatosEstruct():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana#Aqui se hace una instancia de la ventana teoria que se paso vacia como parametro
            self.ventanaTeoria.geometry("680x575")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
            self.ventanaTeoria.configure(bg= '#024747')#Se cambia el color del fondo
            self.VT=Temas#Aqui se hace una instancia de la ventana Temas que se paso como parametro
            self.notebook=ttk.Notebook(ventana)#Dentro de la ventana se crea un notebook para gestionar paneles
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Definicion = PhotoImage(file="DatosEstructurados/Definicion.gif")
            self.DatosEstructDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.DatosEstructDefinicion.image = self.Definicion
            self.DatosEstructDefinicion.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Matrices1 = PhotoImage(file="DatosEstructurados/Matrices1.gif")
            self.DatosEstructMat1 = ttk.Label(ventana,image=self.Matrices1,background="white")
            self.DatosEstructMat1.image = self.Matrices1
            self.DatosEstructMat1.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Matrices2 = PhotoImage(file="DatosEstructurados/Matrices2.gif")
            self.DatosEstructMat2 = ttk.Label(ventana,image=self.Matrices2,background="white")
            self.DatosEstructMat2.image = self.Matrices2
            self.DatosEstructMat2.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Matrices3 = PhotoImage(file="DatosEstructurados/Matrices3.gif")
            self.DatosEstructMat3 = ttk.Label(ventana,image=self.Matrices3,background="white")
            self.DatosEstructMat3.image = self.Matrices3
            self.DatosEstructMat3.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.CadenasCaracteres = PhotoImage(file="DatosEstructurados/CadenasCaracteres.gif")
            self.DatosEstructCadCarac = ttk.Label(ventana,image=self.CadenasCaracteres,background="white")
            self.DatosEstructCadCarac.image = self.CadenasCaracteres
            self.DatosEstructCadCarac.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Registro1 = PhotoImage(file="DatosEstructurados/Registro1.gif")
            self.DatosEstructReg1 = ttk.Label(ventana,image=self.Registro1,background="white")
            self.DatosEstructReg1.image = self.Registro1
            self.DatosEstructReg1.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Registro2 = PhotoImage(file="DatosEstructurados/Registro2.gif")
            self.DatosEstructReg2 = ttk.Label(ventana,image=self.Registro2,background="white")
            self.DatosEstructReg2.image = self.Registro2
            self.DatosEstructReg2.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Otros = PhotoImage(file="DatosEstructurados/OtrosTipos.gif")
            self.DatosEstructOtros = ttk.Label(ventana,image=self.Otros,background="white")
            self.DatosEstructOtros.image = self.Otros
            self.DatosEstructOtros.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Resumen = PhotoImage(file="DatosEstructurados/Resumen.gif")
            self.DatosEstructResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.DatosEstructResumen.image = self.Resumen
            self.DatosEstructResumen.place(x=0,y=0)
            
            #Se crean dos botones, uno para crear la ventana con las preguntas y el otro para volver atras
            self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)
            
            #Se añaden como pestañas en el notebook los labels con las imagenes ya cargadas
            self.notebook.add(self.DatosEstructDefinicion,text="Pag 1")
            self.notebook.add(self.DatosEstructMat1,text="Pag 2")
            self.notebook.add(self.DatosEstructMat2,text="Pag 3")
            self.notebook.add(self.DatosEstructMat3,text="Pag 4")
            self.notebook.add(self.DatosEstructCadCarac,text="Pag 5")
            self.notebook.add(self.DatosEstructReg1,text="Pag 6")
            self.notebook.add(self.DatosEstructReg2,text="Pag 7")
            self.notebook.add(self.DatosEstructOtros,text="Pag 8")
            self.notebook.add(self.DatosEstructResumen,text="Pag 9")
            self.notebook.pack()

    def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaTeoria.destroy()#Y lo que hace es cerrar la ventana Teoria y
        self.VT.deiconify()# reabrir la ventana anterior, en este caso la ventana principal.

    def Evaluacion(self):# Esta funcion es llamada cuando se aprieta el boton Evaluacion de conceptos
        VentanaEva=Evaluacion(self.ventanaTeoria)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con las preguntas del tema elegido