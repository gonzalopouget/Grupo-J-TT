import tkinter as tk
from tkinter import ttk
from tkinter import *
from Expresiones.EvaluacionExpr import Evaluacion
class TeoriaExpr():

    def __init__(self,ventana,Temas):
            self.ventanaTeoria=ventana#Aqui se hace una instancia de la ventana teoria que se paso vacia como parametro
            self.ventanaTeoria.geometry("700x590")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
            self.ventanaTeoria.configure(bg= '#024747')#Se cambia el color del fondo
            self.VT=Temas#Aqui se hace una instancia de la ventana Temas que se paso como parametro
            self.notebook=ttk.Notebook(ventana)#Dentro de la ventana se crea un notebook para gestionar paneles
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Definicion = PhotoImage(file="Expresiones/Definicion.gif")
            self.ExprDefinicion = ttk.Label(ventana,image=self.Definicion,background="white")
            self.ExprDefinicion.image = self.Definicion
            self.ExprDefinicion.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.OpAritmeticos = PhotoImage(file="Expresiones/OperadoresAritmeticos.gif")
            self.ExprOpAritmeticos = ttk.Label(ventana,image=self.OpAritmeticos,background="white")
            self.ExprOpAritmeticos.image = self.OpAritmeticos
            self.ExprOpAritmeticos.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.OpAritmeticosEj = PhotoImage(file="Expresiones/OperadoresAritmeticosEjemplos.gif")
            self.ExprOpAritmeticosEj = ttk.Label(ventana,image=self.OpAritmeticosEj,background="white")
            self.ExprOpAritmeticosEj.image = self.OpAritmeticosEj
            self.ExprOpAritmeticosEj.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.OpLogicos = PhotoImage(file="Expresiones/OperadoresLogicos.gif")
            self.ExprOpLogicos = ttk.Label(ventana,image=self.OpLogicos,background="white")
            self.ExprOpLogicos.image = self.OpLogicos
            self.ExprOpLogicos.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.OpRelacionales = PhotoImage(file="Expresiones/OperadoresRelacionales.gif")
            self.ExprOpRelacionales = ttk.Label(ventana,image=self.OpRelacionales,background="white")
            self.ExprOpRelacionales.image = self.OpRelacionales
            self.ExprOpRelacionales.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.ExpresionesComplejas = PhotoImage(file="Expresiones/ExpresionesComplejasProcedencia.gif")
            self.ExprComp = ttk.Label(ventana,image=self.ExpresionesComplejas,background="white")
            self.ExprComp.image = self.ExpresionesComplejas
            self.ExprComp.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Asignacion = PhotoImage(file="Expresiones/AsignacionResultados.gif")
            self.ExprAsigRes = ttk.Label(ventana,image=self.Asignacion,background="white")
            self.ExprAsigRes.image = self.Asignacion
            self.ExprAsigRes.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Uso = PhotoImage(file="Expresiones/UsoVariables.gif")
            self.ExprUsoVar = ttk.Label(ventana,image=self.Uso,background="white")
            self.ExprUsoVar.image = self.Uso
            self.ExprUsoVar.place(x=0,y=0)
            
            #Se configura un lbl con una captura de pantalla, que contiene la informacion requerida
            self.Resumen = PhotoImage(file="Expresiones/Resumen.gif")
            self.ExprResumen = ttk.Label(ventana,image=self.Resumen,background="white")
            self.ExprResumen.image = self.Resumen
            self.ExprResumen.place(x=0,y=0)
            
            #Se crean dos botones, uno para crear la ventana con las preguntas y el otro para volver atras
            self.btnEvaluacion = Button(self.ventanaTeoria,text="Evaluacion de conceptos",command=self.Evaluacion).pack(side = BOTTOM)
            self.btnSalir = Button(self.ventanaTeoria, text='Volver',command=self.Volver).pack(side=BOTTOM)
            
            #Se añaden como pestañas en el notebook los labels con las imagenes ya cargadas
            self.notebook.add(self.ExprDefinicion,text="Pag 1")
            self.notebook.add(self.ExprOpAritmeticos,text="Pag 2")
            self.notebook.add(self.ExprOpAritmeticosEj,text="Pag 3")
            self.notebook.add(self.ExprOpRelacionales,text="Pag 4")
            self.notebook.add(self.ExprOpLogicos,text="Pag 5")
            self.notebook.add(self.ExprAsigRes,text="Pag 6")
            self.notebook.add(self.ExprUsoVar,text="Pag 7")
            self.notebook.add(self.ExprComp,text="Pag 8")
            self.notebook.add(self.ExprResumen,text="Pag 9")
            self.notebook.pack()

    def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaTeoria.destroy()#Y lo que hace es cerrar la ventana Teoria y
        self.VT.deiconify()# reabrir la ventana anterior, en este caso la ventana principal.

    def Evaluacion(self):# Esta funcion es llamada cuando se aprieta el boton Evaluacion de conceptos
         VentanaEva=Evaluacion(self.ventanaTeoria)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con las preguntas del tema elegido