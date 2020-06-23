import tkinter as tk
from tkinter import ttk
from tkinter import *
from NavegandoSistemaArchivos.TeoriaNaveSistArch import TeoriaNavSist
from VerCambiarSistemaArchivos.TeoriaVerCambSistArch import TeoriaVerCamb
from RedireccionandoEntradaSalida.TeoriaRedireccEntSal import TeoriaRedireccEntSal
from ConfigurandoEntorno.TeoriaConfgEnt import TeoriaConfgEnt
from BashScripting.TeoriaBashScript import TeoriaBashScript
class TeoriaLineaComandos():

    def __init__(self, ventanaTemas,Temas):
        self.VT=ventanaTemas
        self.VT.withdraw()
        self.ventanaTeoria = tk.Toplevel(ventanaTemas)
        self.ventanaTeoria.title("Teoria")
        self.ventanaTeoria.geometry("660x360")
        self.ventanaTeoria.resizable(0,0)
        self.ventanaTeoria.configure(bg="#024747")
        if(Temas.get()=="Navegar Sistema de Archivos"):
            navegar=TeoriaNavSist(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Ver y Cambiar Sistema de Archivos"):
            verCambiar=TeoriaVerCamb(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Redireccionando Entradas y Salidas"):
            redireccEntSal=TeoriaRedireccEntSal(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Configuracion de Entorno"):
            confgEnt=TeoriaConfgEnt(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Bash Scripting"):
            bashScript=TeoriaBashScript(self.ventanaTeoria,self.VT)
        
    
