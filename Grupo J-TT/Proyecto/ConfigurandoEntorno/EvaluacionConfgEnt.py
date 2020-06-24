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
        self.lblP1=ttk.Label(self.P1,text="Pregunta 1: ¿Que marca el símbolo ~ ?").pack()
        self.radioValueP1=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP1 = tk.Radiobutton(self.P1,text="El directorio de inicio.",variable=self.radioValueP1,value=1).pack()
        self.rdioTwoP1 = tk.Radiobutton(self.P1,text="El comando nano.",variable=self.radioValueP1,value=2).pack()
        self.rdioThreeP1 = tk.Radiobutton(self.P1,text="El directorio de documentos.",variable=self.radioValueP1,value=3).pack()
        self.rdioFourP1 = tk.Radiobutton(self.P1,text="El comando cat.",variable=self.radioValueP1,value=4).pack()

        self.P2=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 2
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP2=ttk.Label(self.P2,text="Pregunta 2: ¿Qué separa los directorios en tu variable $PATH?").pack()
        self.radioValueP2=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP2 = tk.Radiobutton(self.P2,text=";",variable=self.radioValueP2,value=5).pack()
        self.rdioTwoP2 = tk.Radiobutton(self.P2,text=",",variable=self.radioValueP2,value=6).pack()
        self.rdioThreeP2 = tk.Radiobutton(self.P2,text="“",variable=self.radioValueP2,value=7).pack()
        self.rdioFourP2 = tk.Radiobutton(self.P2,text=":",variable=self.radioValueP2,value=8).pack()
            
        self.P3=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 3
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP3=ttk.Label(self.P3,text="Pregunta 3: ¿Qué pasaría si sacaras el directorio /bin/ de tu $PATH?").pack()
        self.radioValueP3=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP3 = tk.Radiobutton(self.P3,text="Tu computadora falla.",variable=self.radioValueP3,value=9).pack()
        self.rdioTwoP3 = tk.Radiobutton(self.P3,text="Nada.",variable=self.radioValueP3,value=10).pack()
        self.rdioThreeP3 = tk.Radiobutton(self.P3,text="Tu $HOME cambia.",variable=self.radioValueP3,value=11).pack()
        self.rdioFourP3 = tk.Radiobutton(self.P3,text="Ya no podras usar comandos en /bin/.",variable=self.radioValueP3,value=12).pack()

        self.P4=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 4
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP4=ttk.Label(self.P4,text="Pregunta 4: El comando clear ____").pack()
        self.radioValueP4=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP4 = tk.Radiobutton(self.P4,text="Borra el contenido de un archivo.",variable=self.radioValueP4,value=13).pack()
        self.rdioTwoP4 = tk.Radiobutton(self.P4,text="Borra todos los archivos en un directorio.",variable=self.radioValueP4,value=14).pack()
        self.rdioThreeP4 = tk.Radiobutton(self.P4,text="Borra el historial de comandos.",variable=self.radioValueP4,value=15).pack()
        self.rdioFourP4 = tk.Radiobutton(self.P4,text="Borra el terminal de texto.",variable=self.radioValueP4,value=16).pack()

        self.P5=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 5
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP5=ttk.Label(self.P5,text="Pregunta 5: Para ejecutar el comando ls -a cuando escribas la, debes ___").pack()
        self.radioValueP5=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP5 = tk.Radiobutton(self.P5,text="Ninguna de estas.",variable=self.radioValueP5,value=17).pack()
        self.rdioTwoP5 = tk.Radiobutton(self.P5,text="nano la",variable=self.radioValueP5,value=18).pack()
        self.rdioThreeP5 = tk.Radiobutton(self.P5,text="Ingresar alias ls -a = ”la” en tu script bash.",variable=self.radioValueP5,value=19).pack()
        self.rdioFourP5 = tk.Radiobutton(self.P5,text="Ingresar alias la = ”ls -a” en tu script bash.",variable=self.radioValueP5,value=20).pack()

        self.P6=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 6
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP6=ttk.Label(self.P6,text="Pregunta 6: ¿Cómo activarías los cambios que realizaste en tu bash_profile?").pack()
        self.radioValueP6=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP6 = tk.Radiobutton(self.P6,text="Con source ~/.bash_profile.",variable=self.radioValueP6,value=21).pack()
        self.rdioTwoP6 = tk.Radiobutton(self.P6,text="Comenzando una nueva sesión de terminal.",variable=self.radioValueP6,value=22).pack()
        self.rdioThreeP6 = tk.Radiobutton(self.P6,text="Comenzando una nueva sesión de terminal o usando source ~/.bash_profile.",variable=self.radioValueP6,value=23).pack()
        self.rdioFourP6 = tk.Radiobutton(self.P6,text="Con clear.",variable=self.radioValueP6,value=24).pack()

        self.P7=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 7
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP7=ttk.Label(self.P7,text="Pregunta 7: Usando export en tu script bash ____").pack()
        self.radioValueP7=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP7 = tk.Radiobutton(self.P7,text="Agregas otra ventana de terminal.",variable=self.radioValueP7,value=25).pack()
        self.rdioTwoP7 = tk.Radiobutton(self.P7,text="Imprimes el cambio.",variable=self.radioValueP7,value=26).pack()
        self.rdioThreeP7 = tk.Radiobutton(self.P7,text="Envías el cambio a un archivo.",variable=self.radioValueP7,value=27).pack()
        self.rdioFourP7 = tk.Radiobutton(self.P7,text="Haces que la variable esté disponible en todos los subprogramas del shell actual.",variable=self.radioValueP7,value=28).pack()

        self.P8=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 8
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP8=ttk.Label(self.P8,text="Pregunta 8: La variable $HOME contiene _____").pack()
        self.radioValueP8=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP8 = tk.Radiobutton(self.P8,text="Tu nombre de usuario.",variable=self.radioValueP8,value=29).pack()
        self.rdioTwoP8 = tk.Radiobutton(self.P8,text="Ninguna de estas.",variable=self.radioValueP8,value=30).pack()
        self.rdioThreeP8 = tk.Radiobutton(self.P8,text="La ruta a tu directorio de inicio.",variable=self.radioValueP8,value=31).pack()
        self.rdioFourP8 = tk.Radiobutton(self.P8,text="Tu directorio de trabajo actual.",variable=self.radioValueP8,value=32).pack()

        self.P9=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 9
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP9=ttk.Label(self.P9,text="Pregunta 9: El comando nano hello.txt ____").pack()
        self.radioValueP9=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP9 = tk.Radiobutton(self.P9,text="Mueve hello.txt a un directorio llamado nano.",variable=self.radioValueP6,value=33).pack()
        self.rdioTwoP9 = tk.Radiobutton(self.P9,text="Borra el contenido de hello.txt.",variable=self.radioValueP6,value=34).pack()
        self.rdioThreeP9 = tk.Radiobutton(self.P9,text="Abre hello.txt en el editor de texto nano.",variable=self.radioValueP6,value=35).pack()
        self.rdioFourP9 = tk.Radiobutton(self.P9,text="Abre bash_profile en el editor de texto nano.",variable=self.radioValueP6,value=36).pack()

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
        if(self.radioValueP1.get()==1):
            puntos+=2
        elif(self.radioValueP2.get()==8):
            puntos+=2
        elif(self.radioValueP3.get()==12):
            puntos+=2
        elif(self.radioValueP4.get()==16):   
            puntos+=2
        elif(self.radioValueP5.get()==20):
            puntos+=2
        elif(self.radioValueP6.get()==23):
            puntos+=2
        elif(self.radioValueP7.get()==28):
            puntos+=2
        elif(self.radioValueP8.get()==31):
            puntos+=2
        elif(self.radioValueP9.get()==35):
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
                
 
            