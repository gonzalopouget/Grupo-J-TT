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
        self.ventanaEvaluacion.geometry("670x330")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
        self.ventanaEvaluacion.configure(bg= '#024747')#Se cambia el color del fondo
        self.notebook=ttk.Notebook(self.ventanaEvaluacion)#Dentro de la ventana se crea un notebook para gestionar paneles

        self.P1=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 1
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP1=ttk.Label(self.P1,text="Pregunta 1: El comando git status muestra...\n",font=("bold")).pack()
        self.radioValueP1=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP1 = tk.Radiobutton(self.P1,text="Solo archivos sin seguimiento.",variable=self.radioValueP1,value=1).pack()
        self.rdioTwoP1 = tk.Radiobutton(self.P1,text="Cambios de archivo organizados para commitear.",variable=self.radioValueP1,value=2).pack()
        self.rdioThreeP1 = tk.Radiobutton(self.P1,text="Archivos sin seguimiento y cambios de archivos organizados para commitear.",variable=self.radioValueP1,value=3).pack()
        self.rdioFourP1 = tk.Radiobutton(self.P1,text="El historial de commits de un proyecto Git.",variable=self.radioValueP1,value=4).pack()

        self.P2=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 2
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP2=ttk.Label(self.P2,text="Pregunta 2: ¿Qué tiene de malo el código a continuación?\n",font=("bold")).pack()
        self.lblCommandP2=ttk.Label(self.P2,text="git commit -m Add new scene to screenplay\n").pack()#Algunas preguntas necesitan de un label extra para separar un fragmento de codigo con el que responder la pregunta
        self.radioValueP2=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP2 = tk.Radiobutton(self.P2,text="El mensaje del commit debe estar en mayúsculas.",variable=self.radioValueP2,value=5).pack()
        self.rdioTwoP2 = tk.Radiobutton(self.P2,text="La opción -m no es necesaria aquí.",variable=self.radioValueP2,value=6).pack()
        self.rdioThreeP2 = tk.Radiobutton(self.P2,text="El mensaje del commit carece de comillas.",variable=self.radioValueP2,value=7).pack()
        self.rdioFourP2 = tk.Radiobutton(self.P2,text="La opción -m va antes de la palabra commit.",variable=self.radioValueP2,value=8).pack()
            
        self.P3=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 3
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP3=ttk.Label(self.P3,text="Pregunta 3: ¿En qué lugar de Git creas, editas, eliminas\n\t y organizas archivos de proyecto?\n",font=("bold")).pack()
        self.radioValueP3=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP3 = tk.Radiobutton(self.P3,text="El área de ensayo.",variable=self.radioValueP3,value=9).pack()
        self.rdioTwoP3 = tk.Radiobutton(self.P3,text="El directorio .gitignore.",variable=self.radioValueP3,value=10).pack()
        self.rdioThreeP3 = tk.Radiobutton(self.P3,text="El directorio de trabajo.",variable=self.radioValueP3,value=11).pack()
        self.rdioFourP3 = tk.Radiobutton(self.P3,text="La carpeta de inicialización.",variable=self.radioValueP3,value=12).pack()

        self.P4=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 4
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP4=ttk.Label(self.P4,text="Pregunta 4: ¿Por qué usar Git?\n",font=("bold")).pack()
        self.radioValueP4=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP4 = tk.Radiobutton(self.P4,text="Para asegurar una base de código contra hackers.",variable=self.radioValueP4,value=13).pack()
        self.rdioTwoP4 = tk.Radiobutton(self.P4,text="Para probar la sintaxis adecuada en tu código",variable=self.radioValueP4,value=14).pack()
        self.rdioThreeP4 = tk.Radiobutton(self.P4,text="Para proporcionar ruedas de entrenamiento para conceptos de codificación complejos.",variable=self.radioValueP4,value=15).pack()
        self.rdioFourP4 = tk.Radiobutton(self.P4,text="Para realizar un seguimiento de los cambios realizados en un proyecto a lo largo del tiempo.",variable=self.radioValueP4,value=16).pack()

        self.P5=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 5
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP5=ttk.Label(self.P5,text="Pregunta 5: En el siguiente código, ¿con qué\n\t reemplazarias filename?\n",font=("bold")).pack()
        self.lblCommandP5=ttk.Label(self.P5,text="git add filename\n").pack()#Algunas preguntas necesitan de un label extra para separar un fragmento de codigo con el que responder la pregunta
        self.radioValueP5=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP5 = tk.Radiobutton(self.P5,text="Ninguno de estos.",variable=self.radioValueP5,value=17).pack()
        self.rdioTwoP5 = tk.Radiobutton(self.P5,text="El archivo que deseas eliminar del directorio de trabajo.",variable=self.radioValueP5,value=18).pack()
        self.rdioThreeP5 = tk.Radiobutton(self.P5,text="El nombre del repositorio Git.",variable=self.radioValueP5,value=19).pack()
        self.rdioFourP5 = tk.Radiobutton(self.P5,text="El archivo que deseas agregar al área de ensayo.",variable=self.radioValueP5,value=20).pack()

        self.P6=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 6
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP6=ttk.Label(self.P6,text="Pregunta 6: ¿Qué hace git init?\n",font=("bold")).pack()
        self.radioValueP6=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP6 = tk.Radiobutton(self.P6,text="Agrega todos los archivos al área de ensayo.",variable=self.radioValueP6,value=21).pack()
        self.rdioTwoP6 = tk.Radiobutton(self.P6,text="Commitea tus archivos en el repositorio.",variable=self.radioValueP6,value=22).pack()
        self.rdioThreeP6 = tk.Radiobutton(self.P6,text="Elimina un proyecto Git.",variable=self.radioValueP6,value=23).pack()
        self.rdioFourP6 = tk.Radiobutton(self.P6,text="Inicializa un nuevo proyecto Git.",variable=self.radioValueP6,value=24).pack()

        self.P7=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 7
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP7=ttk.Label(self.P7,text="Pregunta 7: ¿El resultado a continuación es típico de qué comando?\n",font=("bold")).pack()
        self.lblCommandP7=ttk.Label(self.P7,text="commit bda95786432d142bbff996ad32045fa4f32ec619\nAuthor: codecademy <ccuser@codecademy.com>\nDate: on Nov 16 13:13:33 2015 -0500\nFirst commit\n").pack()#Algunas preguntas necesitan de un label extra para separar un fragmento de codigo con el que responder la pregunta
        self.radioValueP7=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP7 = tk.Radiobutton(self.P7,text="git log",variable=self.radioValueP7,value=25).pack()
        self.rdioTwoP7 = tk.Radiobutton(self.P7,text="git diff",variable=self.radioValueP7,value=26).pack()
        self.rdioThreeP7 = tk.Radiobutton(self.P7,text="git add filename",variable=self.radioValueP7,value=27).pack()
        self.rdioFourP7 = tk.Radiobutton(self.P7,text="git status",variable=self.radioValueP7,value=28).pack()

        self.P8=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 8
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP8=ttk.Label(self.P8,text="Pregunta 8: En Git, un commit...\n",font=("bold")).pack()
        self.radioValueP8=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP8 = tk.Radiobutton(self.P8,text="Almacena permanentemente los cambios del área de ensayo en el repositorio.",variable=self.radioValueP6,value=29).pack()
        self.rdioTwoP8 = tk.Radiobutton(self.P8,text="Guarda todos los archivos en tu directorio de trabajo.",variable=self.radioValueP6,value=30).pack()
        self.rdioThreeP8 = tk.Radiobutton(self.P8,text="Registra solo el código con la sintaxis correcta.",variable=self.radioValueP6,value=31).pack()
        self.rdioFourP8 = tk.Radiobutton(self.P8,text="Almacena temporalmente los cambios del área de ensayo en el repositorio.",variable=self.radioValueP6,value=32).pack()

        self.P9=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 9
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP9=ttk.Label(self.P9,text="Pregunta 9: ¿Cuál es el propósito del área de ensayo de Git?\n",font=("bold")).pack()
        self.radioValueP9=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP9 = tk.Radiobutton(self.P9,text="Organizar los cambios de archivo para un commit.",variable=self.radioValueP9,value=33).pack()
        self.rdioTwoP9 = tk.Radiobutton(self.P9,text="Listar notas sobre tu proyecto.",variable=self.radioValueP9,value=34).pack()
        self.rdioThreeP9 = tk.Radiobutton(self.P9,text="Listar archivos que no deseas que Git rastree.",variable=self.radioValueP9,value=35).pack()
        self.rdioFourP9 = tk.Radiobutton(self.P9,text="Para mostrar una lista de los commits de su proyecto.",variable=self.radioValueP9,value=36).pack()
            
        #Todos los frames que contienen las preguntas van a tener un boton para poder "guardar la respuesta" asi se podra calificar con una nota segun las repuestas correctas
        self.btnRevisarP1 = Button(self.P1,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP2 = Button(self.P2,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP3 = Button(self.P3,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP4 = Button(self.P4,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP5 = Button(self.P5,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP6 = Button(self.P6,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP7 = Button(self.P7,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP8 = Button(self.P8,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP9 = Button(self.P9,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)

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
        self.notebook.add(self.P8,text="Pregunta 8")
        self.notebook.add(self.P9,text="Pregunta 9")
        self.notebook.pack()
            
    def Revisar(self):#Esta funcion es llamada cada vez que se "guarda" alguna respuesta de alguna pregunta
        global puntos

        #En estos casos va a aumentar el contador ya que si el valor asignado de la respuesta elegida coincide, quiere decir que es la correcta
        if(self.radioValueP1.get()==3):
            puntos+=2
        elif(self.radioValueP2.get()==6):
            puntos+=2
        elif(self.radioValueP3.get()==11):
            puntos+=2
        elif(self.radioValueP4.get()==16):   
            puntos+=2
        elif(self.radioValueP5.get()==20):
            puntos+=2
        elif(self.radioValueP6.get()==24):
            puntos+=2
        elif(self.radioValueP7.get()==25):
            puntos+=2
        elif(self.radioValueP8.get()==29):
            puntos+=2
        elif(self.radioValueP9.get()==33):
            puntos+=2
    def Terminar(self):#Esta funcion es llamada cuando se aprieta el boton de terminar el intento
        #Va a saltar un mensaje de advertencia con dos respuestas posibles: Si o No
        MsgBox = tk.messagebox.askquestion ('Terminar Intento','¿Esta seguro que desea terminar este intento?',icon = 'warning')
        if MsgBox == 'yes':#Si la respuesta es afirmativa va a proceder a calcular la nota con los puntos que hayan
            if(puntos==18):
                messagebox.showinfo(message="Excelente, 9/9 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos>=12 and puntos < 18):
                messagebox.showinfo(message="Muy bien, minimo 6/9 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos>=6 and puntos <12):
                messagebox.showinfo(message="Bien, minimo 3/9 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos>=0 and puntos <6):
                messagebox.showinfo(message="Mal, no ha alcanzado el minimo para aprobar, intente nuevamente", title="Nota")
                self.ventanaEvaluacion.destroy()
                tk.messagebox.showinfo('Regreso','Ahora va a volver a la ventana de evaluacion.')
                self.k.deiconify()
                
       
            