import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

puntos=0

class Evaluacion():
    def __init__(self,VentanaTeoria):
        global puntos#Esta variable va a servir para almacenar los puntos de las respuestas correctas
        puntos=0#Cada vez que se empiece un intento se va a reiniciar el contador
        self.k=VentanaTeoria#Aqui se hace una instancia de la ventana teoria que se paso como parametro
        self.k.withdraw()#Aqui esa ventana pasada como parametro e instanciada anteriormente se minimiza
        self.ventanaEvaluacion = tk.Toplevel(VentanaTeoria)#Aqui se crea la nueva ventana que pasa a ser una ventana hija de la ventana pasada como parametro
        self.ventanaEvaluacion.title("Evaluacion de Conceptos")#Se le pone titulo a la ventana
        self.ventanaEvaluacion.configure(bg= '#024747')#Se cambia el color del fondo
        self.ventanaEvaluacion.geometry("530x300")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
        self.notebook=ttk.Notebook(self.ventanaEvaluacion)#Dentro de la ventana se crea un notebook para gestionar paneles

        self.P1=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 1
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP1=ttk.Label(self.P1,text="Pregunta 1: ¿Qué comando muestra todos los archivos del directorio actual en formato largo,\n incluidos los archivos ocultos?").pack()
        self.radioValueP1=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP1 = tk.Radiobutton(self.P1,text="ls -a",variable=self.radioValueP1,value=1).pack()
        self.rdioTwoP1 = tk.Radiobutton(self.P1,text="ls -al",variable=self.radioValueP1,value=2).pack()
        self.rdioThreeP1 = tk.Radiobutton(self.P1,text="ls -l",variable=self.radioValueP1,value=3).pack()
        self.rdioFourP1 = tk.Radiobutton(self.P1,text="ls -aa",variable=self.radioValueP1,value=4).pack()

        self.P2=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 2
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP2=ttk.Label(self.P2,text="Pregunta 2: ¿Cuál es el propósito de una opción?").pack()
        self.radioValueP2=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP2 = tk.Radiobutton(self.P2,text="Modificar el comportamiento de un comando.",variable=self.radioValueP2,value=5).pack()
        self.rdioTwoP2 = tk.Radiobutton(self.P2,text="Cambiar el color de la salida del comando.",variable=self.radioValueP2,value=6).pack()
        self.rdioThreeP2 = tk.Radiobutton(self.P2,text="Revertir un comando.",variable=self.radioValueP2,value=7).pack()
        self.rdioFourP2 = tk.Radiobutton(self.P2,text="Hacer un comando opcional.",variable=self.radioValueP2,value=8).pack()
            
        self.P3=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 3
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP3=ttk.Label(self.P3,text="Pregunta 3: ¿Qué comando mueve todos los archivos en el directorio actual a school/?").pack()
        self.radioValueP3=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP3 = tk.Radiobutton(self.P3,text="mv school -a",variable=self.radioValueP3,value=9).pack()
        self.rdioTwoP3 = tk.Radiobutton(self.P3,text="mv school",variable=self.radioValueP3,value=10).pack()
        self.rdioThreeP3 = tk.Radiobutton(self.P3,text="mv * school/",variable=self.radioValueP3,value=11).pack()
        self.rdioFourP3 = tk.Radiobutton(self.P3,text="mv -a school/",variable=self.radioValueP3,value=12).pack()

        self.P4=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 4
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP4=ttk.Label(self.P4,text="Pregunta 4: ¿Qué comando te permite listar los archivos ordenados por la última modificación?").pack()
        self.radioValueP4=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP4 = tk.Radiobutton(self.P4,text="ls",variable=self.radioValueP4,value=13).pack()
        self.rdioTwoP4 = tk.Radiobutton(self.P4,text="ls -t",variable=self.radioValueP4,value=14).pack()
        self.rdioThreeP4 = tk.Radiobutton(self.P4,text="ls -a",variable=self.radioValueP4,value=15).pack()
        self.rdioFourP4 = tk.Radiobutton(self.P4,text="ls -l",variable=self.radioValueP4,value=16).pack()

        self.P5=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 5
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP5=ttk.Label(self.P5,text="Pregunta 5:¿Cómo eliminas todos los archivos en el directorio media/?").pack()
        self.radioValueP5=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP5 = tk.Radiobutton(self.P5,text="rm media/*",variable=self.radioValueP5,value=17).pack()
        self.rdioTwoP5 = tk.Radiobutton(self.P5,text="rm media",variable=self.radioValueP5,value=18).pack()
        self.rdioThreeP5 = tk.Radiobutton(self.P5,text="rm -a media/",variable=self.radioValueP5,value=19).pack()
        self.rdioFourP5 = tk.Radiobutton(self.P5,text="rm -all media/",variable=self.radioValueP5,value=20).pack()

        self.P6=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 6
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP6=ttk.Label(self.P6,text="Pregunta 6: ¿Cómo eliminas el directorio music /?").pack()
        self.radioValueP6=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP6 = tk.Radiobutton(self.P6,text="rm -f music",variable=self.radioValueP6,value=21).pack()
        self.rdioTwoP6 = tk.Radiobutton(self.P6,text="rm -r music",variable=self.radioValueP6,value=22).pack()
        self.rdioThreeP6 = tk.Radiobutton(self.P6,text="rm -a music",variable=self.radioValueP6,value=23).pack()
        self.rdioFourP6 = tk.Radiobutton(self.P6,text="rm music",variable=self.radioValueP6,value=24).pack()

        self.P7=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 7
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP7=ttk.Label(self.P7,text="Pregunta 7: ¿Qué comando podrías usar para copiar el contenido de\n kendrick.txt a un nuevo archivo llamado rappers.txt?").pack()
        self.radioValueP7=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP7 = tk.Radiobutton(self.P7,text="cp kendrick.txt",variable=self.radioValueP7,value=25).pack()
        self.rdioTwoP7 = tk.Radiobutton(self.P7,text="cp kendrick.txt rappers.txt",variable=self.radioValueP7,value=26).pack()
        self.rdioThreeP7 = tk.Radiobutton(self.P7,text="cp rappers.txt kendrick.txt ",variable=self.radioValueP7,value=27).pack()
        self.rdioFourP7 = tk.Radiobutton(self.P7,text="cp rappers.txt",variable=self.radioValueP7,value=28).pack()

        #Todos los frames que contienen las preguntas van a tener un boton para poder "guardar la respuesta" asi se podra calificar con una nota segun las repuestas correctas    
        self.btnRevisarP1 = Button(self.P1,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP2 = Button(self.P2,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP3 = Button(self.P3,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP4 = Button(self.P4,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP5 = Button(self.P5,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP6 = Button(self.P6,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP7 = Button(self.P7,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)

        #Va a haber un boton en todo momento que sirve para terminar de responder y volver hacia atras
        self.btnTerminarIntento = Button(self.ventanaEvaluacion,text="Terminar intento",command=self.Terminar).pack(side= BOTTOM)

        """Se agregan al panel de pestañas o notebook los frames con las preguntas y repuestas
        y posteriormente se ubica al notebook en la ventana para que se vea"""
        self.notebook.add(self.P1,text="Pregunta 1")
        self.notebook.add(self.P2,text="Pregunta 2")
        self.notebook.add(self.P3,text="Pregunta 3")
        self.notebook.add(self.P4,text="Pregunta 4")
        self.notebook.add(self.P5,text="Pregunta 5")
        self.notebook.add(self.P6,text="Pregunta 6")
        self.notebook.add(self.P7,text="Pregunta 7")
        self.notebook.pack()
            
    def Revisar(self):#Esta funcion es llamada cada vez que se "guarda" alguna respuesta de alguna pregunta
        global puntos

        #En estos casos va a aumentar el contador ya que si el valor asignado de la respuesta elegida coincide, quiere decir que es la correcta
        if(self.radioValueP1.get()==2):
            puntos+=2
        elif(self.radioValueP2.get()==5):
            puntos+=2
        elif(self.radioValueP3.get()==11):
            puntos+=2
        elif(self.radioValueP4.get()==14):   
            puntos+=2
        elif(self.radioValueP5.get()==17):
            puntos+=2
        elif(self.radioValueP6.get()==22):
            puntos+=2
        elif(self.radioValueP7.get()==26):
            puntos+=2
    def Terminar(self):#Esta funcion es llamada cuando se aprieta el boton de terminar el intento
        #Va a saltar un mensaje de advertencia con dos respuestas posibles: Si o No
        MsgBox = tk.messagebox.askquestion ('Terminar Intento','¿Esta seguro que desea terminar este intento?',icon = 'warning')
        if MsgBox == 'yes':#Si la respuesta es afirmativa va a proceder a calcular la nota con los puntos que hayan
            if(puntos==14):
                messagebox.showinfo(message="Excelente, 7/7 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos>=8 and puntos < 14):
                messagebox.showinfo(message="Muy bien, minimo 4/7 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos>=4 and puntos <8):
                messagebox.showinfo(message="Bien, minimo 2/7 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos>=0 and puntos <4):
                messagebox.showinfo(message="Mal, no ha alcanzado el minimo para aprobar, intente nuevamente", title="Nota")
                self.ventanaEvaluacion.destroy()
                tk.messagebox.showinfo('Regreso','Ahora va a volver a la ventana de evaluacion.')
                self.k.deiconify()
                
            