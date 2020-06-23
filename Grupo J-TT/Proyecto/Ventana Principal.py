import tkinter as tk
from tkinter import ttk
from tkinter import *
from Covid import Covid#Aqui se importan las funciones.
from categorias import Categorias#Covid y Categorias que estan en otros archivos para ser usadas mas abajo.

class VentanaPrincipal:

    def Ventana(self):

        """En orden de declaracion, primero se crea la que va a ser la ventana raiz de todo, luego se le otorga el titulo que va
        a tener en la parte superior, luego se configura para que no pueda ser ajustable la resolucion, luego se le configura un tamaño,
        posteriormente se cambia el color del fondo, luego se agrega un label con el nombre del proyecto y se configura algunas
        caracteristicas de dicho label como el color, la fuente, etc. 
        Se crea una variable que va a almacenar una imagen que va a ser usada en el boton Covid declarado mas abajo, tambien se declara
        otro boton que va a estar debajo del label"""
        self.principal =  tk.Tk()
        self.principal.title("Educational Python")
        self.principal.resizable(0,0)
        self.principal.geometry("480x320")
        self.principal.configure(bg= '#024747')
        self.frameTitulo=ttk.Label(self.principal, text="Educational Python")
        self.frameTitulo.config(background = "#024747", foreground="white",font=("Verdana",32))
        self.frameTitulo.pack(anchor=CENTER)
        photo = PhotoImage(file = "geisinger-covid19-icon.gif")
        photoimage = photo.subsample(20,20)
        btnCovid = Button(self.principal,text= "Informacion sobre el Covid-19",image=photoimage,background="#3498DB",compound = LEFT,command=self.VentanaCovid).pack(side = BOTTOM)
        btnCategorias = Button(self.principal,text= "Seleccionar una Categoria",command=self.VentanaCategorias).pack()
        self.principal.mainloop()

    def VentanaCovid(self):#Esta funcion es llamada cuando se aprieta el boton Covid.
        ventanaC=Covid(self.principal)#Aqui se llama a una funcion importada de otro archivo y sirve para crear la ventana con info del Covid.

    def VentanaCategorias(self):#Esta funcion es llamada cuando se aprieta el boton para seleccionar categorias.
        ventanaC2=Categorias(self.principal)#Aqui se llama a otra funcio importada de otro archivo y sirve para crear la ventana con las categorias o asignaturas a elegir.


ventana = VentanaPrincipal()
ventana.Ventana()
