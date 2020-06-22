import tkinter as tk
from tkinter import ttk
from tkinter import *
from FlujodeTrabajobasicoGit.TeoriaFlujoTrabajoBasico import TeoriaFlujo
from BacktrackGit.TeoriaBacktrack import TeoriaBacktrack
from RamificacionGit.TeoriaRamificacion import TeoriaRam
from TrabajoenEquipoGit.TeoriaTrabajoEquipo import TeoriaTrabajo
class TeoriaGit():

    def __init__(self, ventanaTemas,Temas):
        self.VT=ventanaTemas
        self.VT.withdraw()
        self.ventanaTeoria = tk.Toplevel(ventanaTemas)
        self.ventanaTeoria.title("Teoria")
        self.ventanaTeoria.geometry("660x360")
        self.ventanaTeoria.resizable(0,0)
        self.ventanaTeoria.configure(bg="#024747")
        if(Temas.get()=="Flujo de Trabajo basico"):
            flujo=TeoriaFlujo(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Backtrack"):
            backtrack=TeoriaBacktrack(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Ramificacion"):
            ram=TeoriaRam(self.ventanaTeoria,self.VT)
        elif(Temas.get()=="Trabajo en Equipo"):
            trabajo=TeoriaTrabajo(self.ventanaTeoria,self.VT)
        
    
