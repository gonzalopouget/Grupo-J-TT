import tkinter as tk
from tkinter import ttk
from tkinter import *

class Covid():

     def __init__(self, ventanaPrincipal):
        self.VP=ventanaPrincipal#Aqui se hace una instancia de la ventana principal que se paso como parametro
        self.VP.withdraw()#Aqui esa ventana pasada como parametro e instanciada anteriormente se minimiza
        self.ventanaCovid = tk.Toplevel(ventanaPrincipal)#Aqui se crea la nueva ventana que pasa a ser una ventana hija de la ventana pasada como parametro
        self.ventanaCovid.title("Informacion sobre el Covid-19")#Se le pone titulo a la ventana
        self.ventanaCovid.resizable(0,0)#Se vuelve inmodificable el tamaño de la ventana
        self.ventanaCovid.geometry("640x400")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
        self.ventanaCovid.configure(bg= '#024747')#Se cambia el color del fondo
        self.notebook=ttk.Notebook(self.ventanaCovid)#Dentro de la ventana se crea un notebook para gestionar paneles
        self.btnSalir = Button(self.ventanaCovid,text="Volver",command=self.Volver).pack(side = BOTTOM,anchor =S)#Se crea un boton para salir de la ventana
        self.sintomas = PhotoImage(file="sintomas-coronavirus.gif")#Se carga una imagen en una variable
        self.Covid_Sintomas = ttk.Label(self.ventanaCovid,image=self.sintomas)#Se crea un label que va a tener dentro la imagen anterior
        self.Covid_Sintomas.image = self.sintomas#Aqui se configura la imagen dentro del label
        self.Covid_Sintomas.place(x=0,y=0)#Se ubica al label en la ventana
        self.medidas = PhotoImage(file="unnamed.gif")#Se carga otra imagen en otra variable
        self.Covid_Medidas = ttk.Label(self.ventanaCovid,image=self.medidas)#Se procede a crear otro label igual que antes
        self.Covid_Medidas.image = self.medidas#Se configura la nueva imagen en el nuevo label
        self.Covid_Medidas.place(x=0,y=0)#Se ubica el nuevo label en la ventana
        self.Covid_Info=tk.Frame(self.ventanaCovid)#Se crea un frame para meterle cosas
        self.lblInfo=Label(self.Covid_Info,text="Mas Info en:")#Se configura un label dentro del frame
        #Se crea un boton que va a albergar un link
        self.link = Button(self.Covid_Info,text="https://www.argentina.gob.ar/salud/coronavirus-COVID-19",command=self.clickearLink)
        self.lblInfo.pack()#Se ubica al lbl en el frame
        self.link.pack()#Se ubica al boton del link en el frame
        
        """Se agregan al panel de pestañas o notebook los label con las imagenes y el frame con el link
        y posteriormente se ubica al notebook en la ventana para que se vea"""
        self.notebook.add(self.Covid_Sintomas,text="Sintomas")
        self.notebook.add(self.Covid_Medidas,text="Medidas de Precaucion")
        self.notebook.add(self.Covid_Info,text="Mas informacion")
        self.notebook.pack()

     def clickearLink(self):#Esta funcion es llamada cuando se aprieta el boton que esta ubicado en la tercer pestaña del notebook.
        import webbrowser
        webbrowser.open("https://www.argentina.gob.ar/salud/coronavirus-COVID-19")#Y basicamente te redirige a esta pagina del gobierno que tiene informacion mas detallada sobre el Covid.

     def Volver(self):# Esta funcion es llamada cuando se aprieta el boton Volver
        self.ventanaCovid.destroy()#Y lo que hace es cerrar la ventana Covid y 
        self.VP.deiconify()# reabrir la ventana anterior, en este caso la ventana principal.