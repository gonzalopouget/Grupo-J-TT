import tkinter as tk
from tkinter import ttk
from tkinter import *
from Algoritmos.TeoriaAlg import TeoriaAlg
from Programas.TeoriaProg import TeoriaProg
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

class Teoria():

    def __init__(self, ventanaTemas,Temas):
        self.VT=ventanaTemas
        self.VT.withdraw()
        self.ventanaTeoria = tk.Toplevel(ventanaTemas)
        self.ventanaTeoria.title("Teoria")
        self.ventanaTeoria.geometry("660x360")
        self.ventanaTeoria.resizable(0,0)
        self.ventanaTeoria.configure(bg="#024747")
        if(Temas.get()=="Algoritmos"):
            alg=TeoriaAlg(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Programas"):
            prog=TeoriaProg(self.ventanaTeoria,self.VT)
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
        
    def ventanaEvaluacion(self):
        VentanaEvaluacion=Evaluacion(self.ventanaTeoria,self.NumeroTema)
    
