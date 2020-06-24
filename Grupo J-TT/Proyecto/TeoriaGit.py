import tkinter as tk
from tkinter import ttk
from tkinter import *
from FlujodeTrabajobasicoGit.TeoriaFlujoTrabajoBasico import TeoriaFlujo
from BacktrackGit.TeoriaBacktrack import TeoriaBacktrack
from RamificacionGit.TeoriaRamificacion import TeoriaRam
from TrabajoenEquipoGit.TeoriaTrabajoEquipo import TeoriaTrabajo
class TeoriaGit():

    def __init__(self, ventanaTemas,Temas):
        self.VT=ventanaTemas#Aqui se hace una instancia de la ventana Temas que se paso vacia como parametro
        self.VT.withdraw()#Aqui esa ventana pasada como parametro e instanciada anteriormente se minimiza
        self.ventanaTeoria = tk.Toplevel(ventanaTemas)#Aqui se crea la nueva ventana que pasa a ser una ventana hija de la ventana pasada como parametro
        self.ventanaTeoria.title("Teoria")#Se le pone titulo a la ventana
        self.ventanaTeoria.geometry("660x360")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
        self.ventanaTeoria.configure(bg="#024747")#Se cambia el color del fondo

        #Dependiendo el tema que se haya elegido se va a cumplir uno de estos casos, y dependiendo el caso se va a crear una ventana con la teoria correspondiente al tema elegido
        if(Temas.get()=="Flujo de Trabajo basico"):
            flujo=TeoriaFlujo(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Backtrack"):
            backtrack=TeoriaBacktrack(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Ramificacion"):
            ram=TeoriaRam(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Trabajo en Equipo"):
            trabajo=TeoriaTrabajo(self.ventanaTeoria,self.VT)
        
    
