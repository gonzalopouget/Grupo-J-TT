import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

puntos=0

class Evaluacion():
    def __init__(self,VentanaTeoria):
        self.k=VentanaTeoria
        self.k.withdraw()
        self.ventanaEvaluacion = tk.Toplevel(VentanaTeoria)
        self.ventanaEvaluacion.title("Evaluacion de Conceptos")
        self.ventanaEvaluacion.geometry("420x220")
        self.notebook=ttk.Notebook(self.ventanaEvaluacion)
        self.P1=tk.Frame(self.ventanaEvaluacion)
        self.lblP1=ttk.Label(self.P1,text="Pregunta 1: Los apuntadores son un tipo de datos primitivo\n\tcon dos valores posibles: verdadero y falso.").pack()
        self.radioValueP1=tk.IntVar()
        self.rdioOneP1 = tk.Radiobutton(self.P1,text="Verdadero.",variable=self.radioValueP1,value=1).pack()
        self.rdioTwoP1 = tk.Radiobutton(self.P1,text="Falso.",variable=self.radioValueP1,value=2).pack()

        self.P2=tk.Frame(self.ventanaEvaluacion)
        self.lblP2=ttk.Label(self.P2,text="Pregunta 2: ¿Cuál de los siguientes valores es un dato\n\tde tipo «número real»?").pack()
        self.radioValueP2=tk.IntVar()
        self.rdioOneP2 = tk.Radiobutton(self.P2,text="123",variable=self.radioValueP2,value=3).pack()
        self.rdioTwoP2 = tk.Radiobutton(self.P2,text="-123",variable=self.radioValueP2,value=4).pack()
        self.rdioThreeP2 = tk.Radiobutton(self.P2,text="123.15",variable=self.radioValueP2,value=5).pack()
        self.rdioFourP2 = tk.Radiobutton(self.P2,text="Todas las anteriores.",variable=self.radioValueP2,value=6).pack()
            
        self.P3=tk.Frame(self.ventanaEvaluacion)
        self.lblP3=ttk.Label(self.P3,text="Pregunta 3: ¿Cuál de los siguientes valores es un dato de tipo «caractér»?").pack()
        self.radioValueP3=tk.IntVar()
        self.rdioOneP3 = tk.Radiobutton(self.P3,text="'8'",variable=self.radioValueP3,value=7).pack()
        self.rdioTwoP3 = tk.Radiobutton(self.P3,text="4E52",variable=self.radioValueP3,value=8).pack()
        self.rdioThreeP3 = tk.Radiobutton(self.P3,text="falso",variable=self.radioValueP2,value=9).pack()
        self.rdioFourP3 = tk.Radiobutton(self.P3,text="Ninguna de las anteriores.",variable=self.radioValueP2,value=10).pack()

        self.P4=tk.Frame(self.ventanaEvaluacion)
        self.lblP4=ttk.Label(self.P4,text="Pregunta 4: Los lenguajes de programación nunca permiten convertir\n\tdatos de un tipo a otro.").pack()
        self.radioValueP4=tk.IntVar()
        self.rdioOneP4 = tk.Radiobutton(self.P4,text="Verdadero.",variable=self.radioValueP4,value=11).pack()
        self.rdioTwoP4 = tk.Radiobutton(self.P4,text="Falso.",variable=self.radioValueP4,value=12).pack()

        self.P5=tk.Frame(self.ventanaEvaluacion)
        self.lblP5=ttk.Label(self.P5,text="Pregunta 5: ¿Cuál de las siguientes categorías de tipos de datos se manipula\n\tmediante operaciones definidas por el programador?").pack()
        self.radioValueP5=tk.IntVar()
        self.rdioOneP5 = tk.Radiobutton(self.P5,text="Primitivos.",variable=self.radioValueP5,value=15).pack()
        self.rdioTwoP5 = tk.Radiobutton(self.P5,text="Estructurados.",variable=self.radioValueP5,value=16).pack()
        self.rdioThreeP5 = tk.Radiobutton(self.P5,text="Definidos por el programador.",variable=self.radioValueP5,value=17).pack()
        self.rdioFourP5 = tk.Radiobutton(self.P5,text="Todas las anteriores.",variable=self.radioValueP5,value=18).pack()
            
        self.btnRevisarP1 = Button(self.P1,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP2 = Button(self.P2,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP3 = Button(self.P3,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP4 = Button(self.P4,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP5 = Button(self.P5,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnTerminarIntento = Button(self.ventanaEvaluacion,text="Terminar intento",command=self.Terminar).pack(side= BOTTOM)
        self.notebook.add(self.P1,text="1")
        self.notebook.add(self.P2,text="2")
        self.notebook.add(self.P3,text="3")
        self.notebook.add(self.P4,text="4")
        self.notebook.add(self.P5,text="5")
        self.notebook.pack()
            
    def Revisar(self):
        global puntos
        if(self.radioValueP1.get()==2):
            puntos+=2
        elif(self.radioValueP2.get()==5):
            puntos+=2
        elif(self.radioValueP3.get()==7):
            puntos+=2
        elif(self.radioValueP4.get()==12):   
            puntos+=2
        elif(self.radioValueP5.get()==17):
            puntos+=2
    def Terminar(self):
        MsgBox = tk.messagebox.askquestion ('Terminar Intento','¿Esta seguro que desea terminar este intento?',icon = 'warning')
        if MsgBox == 'yes':
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
                self.k.deiconify()
                
        else:
            tk.messagebox.showinfo('Regreso','Ahora va a volver a la ventana de evaluacion.')
            self.k.deiconify()
      