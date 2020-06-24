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
        self.ventanaEvaluacion.geometry("700x220")#Se le otorga una resolucion que muestre correctamente todos los elementos que van a ir en la pantalla
        self.notebook=ttk.Notebook(self.ventanaEvaluacion)#Dentro de la ventana se crea un notebook para gestionar paneles

        self.P1=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 1
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP1=ttk.Label(self.P1,text="Pregunta 1: Todos los algoritmos se pueden representar como programas usando simplemente instrucciones que\n\tse ejecutan de forma consecutiva sin alteraciones en el flujo de control.").pack()
        self.radioValueP1=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP1 = tk.Radiobutton(self.P1,text="Verdadero.",variable=self.radioValueP1,value=1).pack()
        self.rdioTwoP1 = tk.Radiobutton(self.P1,text="Falso.",variable=self.radioValueP1,value=2).pack()

        self.P2=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 2
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP2=ttk.Label(self.P2,text="Pregunta 2: ¿Cuál es el tipo de la estructura de control: si ... entonces ... sino ... fin_si?").pack()
        self.radioValueP2=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP2 = tk.Radiobutton(self.P2,text="Ejecución secuencial",variable=self.radioValueP2,value=3).pack()
        self.rdioTwoP2 = tk.Radiobutton(self.P2,text="Invocación",variable=self.radioValueP2,value=4).pack()
        self.rdioThreeP2 = tk.Radiobutton(self.P2,text="Repetición",variable=self.radioValueP2,value=5).pack()
        self.rdioFourP2 = tk.Radiobutton(self.P2,text="Selección doble",variable=self.radioValueP2,value=6).pack()
            
        self.P3=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 3
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP3=ttk.Label(self.P3,text="Pregunta 3: En que condición es preferible usar una estructura de repetición controlada por un contador.").pack()
        self.radioValueP3=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP3 = tk.Radiobutton(self.P3,text="Cuando la cantidad de iteraciones se conoce por anticipado.",variable=self.radioValueP3,value=7).pack()
        self.rdioTwoP3 = tk.Radiobutton(self.P3,text="Cuando es necesario limitar el alcance de las variables.",variable=self.radioValueP3,value=8).pack()
        self.rdioThreeP3 = tk.Radiobutton(self.P3,text="Cuando se deben ejecutar múltiples instrucciones simultáneamente.",variable=self.radioValueP3,value=9).pack()
        self.rdioFourP3 = tk.Radiobutton(self.P3,text="Todas las anteriores.",variable=self.radioValueP3,value=10).pack()

        self.P4=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 4
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP4=ttk.Label(self.P4,text="Pregunta 4: ¿Cuál de las siguientes estructuras de control permite usar bloques de\n\tcódigo en las secciones donde permite usar instrucciones individuales?").pack()
        self.radioValueP4=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP4 = tk.Radiobutton(self.P4,text="si ... entonces ... sino ... fin_si",variable=self.radioValueP4,value=11).pack()
        self.rdioTwoP4 = tk.Radiobutton(self.P4,text="mientras ... hacer ... fin_mientras",variable=self.radioValueP4,value=12).pack()
        self.rdioThreeP4 = tk.Radiobutton(self.P4,text="según_sea ... hacer ... fin_según_sea",variable=self.radioValueP4,value=13).pack()
        self.rdioFourP4 = tk.Radiobutton(self.P4,text="Todas las anteriores.",variable=self.radioValueP4,value=14).pack()

        self.P5=tk.Frame(self.ventanaEvaluacion)#Se crea un frame para meterle cosas relacionadas con la pregunta 5
        #Dentro de ese frame se agregan la pregunta a responder y las opciones de respuesta
        self.lblP5=ttk.Label(self.P5,text="Pregunta 5: No está permitido colocar estructuras de repetición dentro de estructuras de selección.").pack()
        self.radioValueP5=tk.IntVar()#Cada boton de las preguntas va a tener asignado un valor para poder distinguir uno de otro
        self.rdioOneP5 = tk.Radiobutton(self.P5,text="Verdadero.",variable=self.radioValueP5,value=15).pack()
        self.rdioTwoP5 = tk.Radiobutton(self.P5,text="Falso.",variable=self.radioValueP5,value=16).pack()
            
        #Todos los frames que contienen las preguntas van a tener un boton para poder "guardar la respuesta" asi se podra calificar con una nota segun las repuestas correctas
        self.btnRevisarP1 = Button(self.P1,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP2 = Button(self.P2,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP3 = Button(self.P3,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP4 = Button(self.P4,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP5 = Button(self.P5,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)

        #Va a haber un boton en todo momento que sirve para terminar de responder y volver hacia atras
        self.btnTerminarIntento = Button(self.ventanaEvaluacion,text="Terminar intento",command=self.Terminar).pack(side= BOTTOM)

        """Se agregan al panel de pestañas o notebook los frames con las preguntas y repuestas
        y posteriormente se ubica al notebook en la ventana para que se vea"""
        self.notebook.add(self.P1,text="Pregunta 1")
        self.notebook.add(self.P2,text="Pregunta 2")
        self.notebook.add(self.P3,text="Pregunta 3")
        self.notebook.add(self.P4,text="Pregunta 4")
        self.notebook.add(self.P5,text="Pregunta 5")
        self.notebook.pack()
            
    def Revisar(self):#Esta funcion es llamada cada vez que se "guarda" alguna respuesta de alguna pregunta
        global puntos

        #En estos casos va a aumentar el contador ya que si el valor asignado de la respuesta elegida coincide, quiere decir que es la correcta
        if(self.radioValueP1.get()==2):
            puntos+=2
        elif(self.radioValueP2.get()==6):
            puntos+=2
        elif(self.radioValueP3.get()==7):
            puntos+=2
        elif(self.radioValueP4.get()==14):   
            puntos+=2
        elif(self.radioValueP5.get()==16):
            puntos+=2
    def Terminar(self):#Esta funcion es llamada cuando se aprieta el boton de terminar el intento
        #Va a saltar un mensaje de advertencia con dos respuestas posibles: Si o No
        MsgBox = tk.messagebox.askquestion ('Terminar Intento','¿Esta seguro que desea terminar este intento?',icon = 'warning')
        if MsgBox == 'yes':#Si la respuesta es afirmativa va a proceder a calcular la nota con los puntos que hayan
            if(puntos==10):
                messagebox.showinfo(message="Excelente, 5/5 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos==8):
                messagebox.showinfo(message="Muy bien, 4/5 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos==6):
                messagebox.showinfo(message="Bien, 3/5 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos>=0 and puntos <6):
                messagebox.showinfo(message="Mal, no ha alcanzado el minimo para aprobar, intente nuevamente", title="Nota")
                self.ventanaEvaluacion.destroy()
                tk.messagebox.showinfo('Regreso','Ahora va a volver a la ventana de evaluacion.')
                self.k.deiconify()
                
           
      