import tkinter as tk
from tkinter import ttk
from tkinter import *
from Algoritmos.TeoriaAlg import TeoriaAlg
from Programas.TeoriaProg import TeoriaProgramas
from Expresiones.TeoriaExpr import TeoriaExpr
from Recursion.TeoriaRec import TeoriaRec
from LenguajesdeProgramacion.TeoriaLeng import TeoriaLeng
from DatosEstructurados.TeoriaDatosEstruct import TeoriaDatosEstruct
from DatosPrimitivos.TeoriaDatosPrim import TeoriaDatosPrim
from ControldeFlujo.TeoriaFlujo import TeoriaFlujo
from EntradaSalidadeDatos.TeoriaEntSalDatos import TeoriaEntSalDatos
from ManejodeErrores.TeoriaManejoErrores import TeoriaManejoErrores
from Subrutinas.TeoriaSubrutinas import TeoriaSubrutinas
from VariablesyAsignaciones.TeoriaVarAsignaciones import TeoriaVarAsignaciones

class TeoriaProg():

    def __init__(self, ventanaTemas,Temas):
        self.VT=ventanaTemas#Aqui se hace una instancia de la ventana Temas que se paso vacia como parametro
        self.VT.withdraw()#Aqui esa ventana pasada como parametro e instanciada anteriormente se minimiza
        self.ventanaTeoria = tk.Toplevel(ventanaTemas)#Aqui se crea la nueva ventana que pasa a ser una ventana hija de la ventana pasada como parametro
        self.ventanaTeoria.title("Teoria")#Se le pone titulo a la ventana
        self.ventanaTeoria.geometry("660x360")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
        self.ventanaTeoria.configure(bg="#024747")#Se cambia el color del fondo

        #Dependiendo el tema que se haya elegido se va a cumplir uno de estos casos, y dependiendo el caso se va a crear una ventana con la teoria correspondiente al tema elegido
        if(Temas.get()=="Algoritmos"):
            alg=TeoriaAlg(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Programas"):
            prog=TeoriaProgramas(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Expresiones"):
            expr=TeoriaExpr(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Recursion"):
            rec=TeoriaRec(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Lenguajes de Programacion"):
            leng=TeoriaLeng(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Tipos de datos estructurados"):
            estruct=TeoriaDatosEstruct(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Tipos de datos primitivos"):
            prim=TeoriaDatosPrim(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Control de flujo"):
            flujo=TeoriaFlujo(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Entrada y salida de datos"):
            entsal=TeoriaEntSalDatos(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Manejo de Errores"):
            manejo=TeoriaManejoErrores(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Subrutinas"):
            subrutinas=TeoriaSubrutinas(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Variables y Asignaciones"):
            variables=TeoriaVarAsignaciones(self.ventanaTeoria,self.VT)
        
    
