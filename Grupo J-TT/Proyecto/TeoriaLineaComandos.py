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
        self.VT=ventanaTemas#Aqui se hace una instancia de la ventana Temas que se paso vacia como parametro
        self.VT.withdraw()#Aqui esa ventana pasada como parametro e instanciada anteriormente se minimiza
        self.ventanaTeoria = tk.Toplevel(ventanaTemas)#Aqui se crea la nueva ventana que pasa a ser una ventana hija de la ventana pasada como parametro
        self.ventanaTeoria.title("Teoria")#Se le pone titulo a la ventana
        self.ventanaTeoria.geometry("660x360")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
        self.ventanaTeoria.configure(bg="#024747")#Se cambia el color del fondo

        #Dependiendo el tema que se haya elegido se va a cumplir uno de estos casos, y dependiendo el caso se va a crear una ventana con la teoria correspondiente al tema elegido
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
        
    
