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
        self.ventanaEvaluacion.geometry("690x340")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
        self.ventanaEvaluacion.configure(bg= '#024747')#Se cambia el color del fondo
        self.notebook=ttk.Notebook(self.ventanaEvaluacion)#Dentro de la ventana se crea un notebook para gestionar paneles

        self.P1=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 1
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP1=ttk.Label(self.P1,text="Pregunta 1: Cuando estás en master y creas una nueva rama...\n",font=("bold")).pack()
        self.radioValueP1=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP1 = tk.Radiobutton(self.P1,text="El comando git branch no listará la nueva rama.",variable=self.radioValueP1,value=1).pack()
        self.rdioTwoP1 = tk.Radiobutton(self.P1,text="La nueva rama y el master comparten exactamente el mismo historial de confirmación.",variable=self.radioValueP1,value=2).pack()
        self.rdioThreeP1 = tk.Radiobutton(self.P1,text="Cada cambio que se realice en la nueva rama también se realizará en master.",variable=self.radioValueP1,value=3).pack()
        self.rdioFourP1 = tk.Radiobutton(self.P1,text="Ninguno de estos.",variable=self.radioValueP1,value=4).pack()

        self.P2=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 2
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP2=ttk.Label(self.P2,text="Pregunta 2: ¿Qué comando lista todas las ramas de un proyecto Git?\n",font=("bold")).pack()
        self.radioValueP2=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP2 = tk.Radiobutton(self.P2,text="git list",variable=self.radioValueP2,value=5).pack()
        self.rdioTwoP2 = tk.Radiobutton(self.P2,text="git show branches",variable=self.radioValueP2,value=6).pack()
        self.rdioThreeP2 = tk.Radiobutton(self.P2,text="git branch",variable=self.radioValueP2,value=7).pack()
        self.rdioFourP2 = tk.Radiobutton(self.P2,text="git checkout branchname",variable=self.radioValueP2,value=8).pack()
            
        self.P3=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 3
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP3=ttk.Label(self.P3,text="Pregunta 3: ¿Por qué el nombre de la\n\t rama my branch no es válido?\n",font=("bold")).pack()
        self.radioValueP3=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP3 = tk.Radiobutton(self.P3,text="La palabra my no se puede usar.",variable=self.radioValueP3,value=9).pack()
        self.rdioTwoP3 = tk.Radiobutton(self.P3,text="Los nombres de rama válidos deben contener un guión.",variable=self.radioValueP3,value=10).pack()
        self.rdioThreeP3 = tk.Radiobutton(self.P3,text="Los nombres de las ramas no pueden contener espacios en blanco.",variable=self.radioValueP3,value=11).pack()
        self.rdioFourP3 = tk.Radiobutton(self.P3,text="Los nombres de las ramas deben estar en mayúscula.",variable=self.radioValueP3,value=12).pack()

        self.P4=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 4
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP4=ttk.Label(self.P4,text="Pregunta 4: Un proyecto Git tiene una\n\t rama bug-fix. ¿Cómo cambias a ella?\n",font=("bold")).pack()
        self.radioValueP4=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP4 = tk.Radiobutton(self.P4,text="git switch master bug-fix",variable=self.radioValueP4,value=13).pack()
        self.rdioTwoP4 = tk.Radiobutton(self.P4,text="git switch bug-switch",variable=self.radioValueP4,value=14).pack()
        self.rdioThreeP4 = tk.Radiobutton(self.P4,text="git branch bug-fix",variable=self.radioValueP4,value=15).pack()
        self.rdioFourP4 = tk.Radiobutton(self.P4,text="git checkout bug-fix",variable=self.radioValueP4,value=16).pack()

        self.P5=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 5
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP5=ttk.Label(self.P5,text="Pregunta 5: Intenta fusionar dos ramas que contienen confirmaciones que\n\t alteran un archivo de manera conflictiva.Esto se llama...\n",font=("bold")).pack()
        self.radioValueP5=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP5 = tk.Radiobutton(self.P5,text="Una fusión de avance rápido.",variable=self.radioValueP5,value=17).pack()
        self.rdioTwoP5 = tk.Radiobutton(self.P5,text="Un conflicto de fusión.",variable=self.radioValueP5,value=18).pack()
        self.rdioThreeP5 = tk.Radiobutton(self.P5,text="Ninguno de estos.",variable=self.radioValueP5,value=19).pack()
        self.rdioFourP5 = tk.Radiobutton(self.P5,text="Un reinicio.",variable=self.radioValueP5,value=20).pack()

        self.P6=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 6
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP6=ttk.Label(self.P6,text="Pregunta 6: Fusionar una rama en master...\n",font=("bold")).pack()
        self.radioValueP6=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP6 = tk.Radiobutton(self.P6,text="Siempre dará como resultado un conflicto de fusión.",variable=self.radioValueP6,value=21).pack()
        self.rdioTwoP6 = tk.Radiobutton(self.P6,text="Integra los cambios realizados en la nueva rama en master.",variable=self.radioValueP6,value=22).pack()
        self.rdioThreeP6 = tk.Radiobutton(self.P6,text="Integra los cambios realizados en master en la nueva sucursal.",variable=self.radioValueP6,value=23).pack()
        self.rdioFourP6 = tk.Radiobutton(self.P6,text="No puede generar un conflicto de fusión.",variable=self.radioValueP6,value=24).pack()

        self.P7=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 7
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP7=ttk.Label(self.P7,text="Pregunta 7: Has fusionado una rama llamada\n\t new-feature en master. ¿Cual es verdad?\n",font=("bold")).pack()
        self.radioValueP7=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP7 = tk.Radiobutton(self.P7,text="master es la rama receptora.",variable=self.radioValueP7,value=25).pack()
        self.rdioTwoP7 = tk.Radiobutton(self.P7,text="new-feature es la rama receptora.",variable=self.radioValueP7,value=26).pack()
        self.rdioThreeP7 = tk.Radiobutton(self.P7,text="master es la rama dadora.",variable=self.radioValueP7,value=27).pack()
        self.rdioFourP7 = tk.Radiobutton(self.P7,text="master es la rama que da y new-feature es la rama receptora.",variable=self.radioValueP7,value=28).pack()

        self.P8=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 8
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP8=ttk.Label(self.P8,text="Pregunta 8: ¿Qué logra el siguiente comando?\n",font=("bold")).pack()
        self.lblCommandP8=ttk.Label(self.P8,text="git branch -d my-branch\n").pack()#Algunas preguntas necesitan de un label extra para separar un fragmento de codigo con el que responder la pregunta
        self.radioValueP8=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP8 = tk.Radiobutton(self.P8,text="Fusionará my-branch en master.",variable=self.radioValueP8,value=29).pack()
        self.rdioTwoP8 = tk.Radiobutton(self.P8,text="Eliminará my-branch.",variable=self.radioValueP8,value=30).pack()
        self.rdioThreeP8 = tk.Radiobutton(self.P8,text="Creará y cambiará al usuario a my-branch.",variable=self.radioValueP8,value=31).pack()
        self.rdioFourP8 = tk.Radiobutton(self.P8,text="Esta es una sintaxis Git no válida.",variable=self.radioValueP8,value=32).pack()

        self.P9=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 9
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP9=ttk.Label(self.P9,text="Pregunta 9: ¿Cuál es una razón común por la que los usuarios\n\t de Git crean una nueva rama?\n",font=("bold")).pack()
        self.radioValueP9=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP9 = tk.Radiobutton(self.P9,text="En caso de que un conflicto de fusión no se pueda resolver.",variable=self.radioValueP6,value=33).pack()
        self.rdioTwoP9 = tk.Radiobutton(self.P9,text="Para ver si la rama tiene el mismo historial de commits que master.",variable=self.radioValueP6,value=34).pack()
        self.rdioThreeP9 = tk.Radiobutton(self.P9,text="Para desarrollar una nueva característica del proyecto.",variable=self.radioValueP6,value=35).pack()
        self.rdioFourP9 = tk.Radiobutton(self.P9,text="Para duplicar master como copia de seguridad.",variable=self.radioValueP6,value=36).pack()

        self.P10=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 10
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP10=ttk.Label(self.P10,text="Pregunta 10: ¿Qué hace el comando a continuación?\n",font=("bold")).pack()
        self.lblCommandP10=ttk.Label(self.P10,text="git branch new_branch\n").pack()#Algunas preguntas necesitan de un label extra para separar un fragmento de codigo con el que responder la pregunta
        self.radioValueP10=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP10 = tk.Radiobutton(self.P10,text="Cambia el nombre de una rama.",variable=self.radioValueP10,value=37).pack()
        self.rdioTwoP10 = tk.Radiobutton(self.P10,text="Crea una nueva rama.",variable=self.radioValueP10,value=38).pack()
        self.rdioThreeP10 = tk.Radiobutton(self.P10,text="Te cambia a una nueva rama.",variable=self.radioValueP10,value=39).pack()
        self.rdioFourP10 = tk.Radiobutton(self.P10,text="Lista el historial de commits de la nueva rama.",variable=self.radioValueP10,value=40).pack()

        self.P11=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 11
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP11=ttk.Label(self.P11,text="Pregunta 11: ¿Qué indica el siguiente código?\n",font=("bold")).pack()
        self.lblCommandP11=ttk.Label(self.P11,text="<<<<<<< HEAD -\n Intuitive and easy to use, providing crucial functionality\n=======\n- Intuitive and fun for use, offering the best in software\n>>>>>>> feature\n").pack()#Algunas preguntas necesitan de un label extra para separar un fragmento de codigo con el que responder la pregunta
        self.radioValueP11=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP11 = tk.Radiobutton(self.P11,text="Comprobador de sintaxis de código de Git.",variable=self.radioValueP11,value=41).pack()
        self.rdioTwoP11 = tk.Radiobutton(self.P11,text="La salida de git status.",variable=self.radioValueP11,value=42).pack()
        self.rdioThreeP11 = tk.Radiobutton(self.P11,text="Una fusión exitosa.",variable=self.radioValueP11,value=43).pack()
        self.rdioFourP11 = tk.Radiobutton(self.P11,text="Un conflicto de fusión.",variable=self.radioValueP11,value=44).pack()

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
        self.btnRevisarP10 = Button(self.P10,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP11 = Button(self.P11,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)

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
        self.notebook.add(self.P10,text="Pregunta 10")
        self.notebook.add(self.P11,text="Pregunta 11")
        self.notebook.pack()
            
    def Revisar(self):#Esta funcion es llamada cada vez que se "guarda" alguna respuesta de alguna pregunta
        global puntos

        #En estos casos va a aumentar el contador ya que si el valor asignado de la respuesta elegida coincide, quiere decir que es la correcta
        if(self.radioValueP1.get()==2):
            puntos+=2
        elif(self.radioValueP2.get()==7):
            puntos+=2
        elif(self.radioValueP3.get()==11):
            puntos+=2
        elif(self.radioValueP4.get()==16):   
            puntos+=2
        elif(self.radioValueP5.get()==18):
            puntos+=2
        elif(self.radioValueP6.get()==22):
            puntos+=2
        elif(self.radioValueP7.get()==25):
            puntos+=2
        elif(self.radioValueP8.get()==30):
            puntos+=2
        elif(self.radioValueP9.get()==35):
            puntos+=2
        elif(self.radioValueP10.get()==38):
            puntos+=2
        elif(self.radioValueP11.get()==44):
            puntos+=2
    def Terminar(self):#Esta funcion es llamada cuando se aprieta el boton de terminar el intento
        #Va a saltar un mensaje de advertencia con dos respuestas posibles: Si o No
        MsgBox = tk.messagebox.askquestion ('Terminar Intento','¿Esta seguro que desea terminar este intento?',icon = 'warning')
        if MsgBox == 'yes':#Si la respuesta es afirmativa va a proceder a calcular la nota con los puntos que hayan
            if(puntos==22):
                messagebox.showinfo(message="Excelente, 11/11 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos>=12 and puntos < 22):
                messagebox.showinfo(message="Muy bien, minimo 6/11 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos>=6 and puntos <12):
                messagebox.showinfo(message="Bien, minimo 3/11 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos>=0 and puntos <6):
                messagebox.showinfo(message="Mal, no ha alcanzado el minimo para aprobar, intente nuevamente", title="Nota")
                self.ventanaEvaluacion.destroy()
                tk.messagebox.showinfo('Regreso','Ahora va a volver a la ventana de evaluacion.')
                self.k.deiconify()
                
    
            