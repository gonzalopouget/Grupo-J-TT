import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

puntos=0

class Evaluacion():
    def __init__(self,VentanaTeoria,NumeroTema):
        self.k=VentanaTeoria
        self.k.withdraw()
        self.ventanaEvaluacion = tk.Toplevel(VentanaTeoria)
        self.ventanaEvaluacion.title("Evaluacion de Conceptos")
        self.ventanaEvaluacion.geometry("410x230")
        self.ventanaEvaluacion.resizable(0,0)
        self.ventanaEvaluacion.configure(bg= '#024747')
        if(NumeroTema==0):
            self.notebook=ttk.Notebook(self.ventanaEvaluacion)
            self.P1=tk.Frame(self.ventanaEvaluacion)
            self.lblP1=ttk.Label(self.P1,text="Pregunta 1: ¿Cuál de las siguientes definiciones\n\tdescribe un algoritmo? (2p)").pack()
            self.radioValueP1=tk.IntVar()
            self.rdioOneP1 = tk.Radiobutton(self.P1,text="Un dispositivo de entrada.",variable=self.radioValueP1,value=1).pack()
            self.rdioTwoP1 = tk.Radiobutton(self.P1,text="Un mecanismo para la generación de nuevas ideas.",variable=self.radioValueP1,value=2).pack()
            self.rdioThreeP1 = tk.Radiobutton(self.P1,text="Un proceso infinito y variable.",variable=self.radioValueP1,value=3).pack()
            self.rdioFourP1 = tk.Radiobutton(self.P1,text="Una secuencia exacta de pasos para resolver un problema.",variable=self.radioValueP1,value=4).pack()

            self.P2=tk.Frame(self.ventanaEvaluacion)
            self.lblP2=ttk.Label(self.P2,text="Pregunta 2: ¿Cuál de las siguientes opciones se refiere a un método\n\tde desarrollo de algoritmos? (2p)").pack()
            self.radioValueP2=tk.IntVar()
            self.rdioOneP2 = tk.Radiobutton(self.P2,text="Divide y conquista.",variable=self.radioValueP2,value=5).pack()
            self.rdioTwoP2 = tk.Radiobutton(self.P2,text="Programación dinámica.",variable=self.radioValueP2,value=6).pack()
            self.rdioThreeP2 = tk.Radiobutton(self.P2,text="Voracidad.",variable=self.radioValueP2,value=7).pack()
            self.rdioFourP2 = tk.Radiobutton(self.P2,text="Todas las anteriores.",variable=self.radioValueP2,value=8).pack()
            
            self.P3=tk.Frame(self.ventanaEvaluacion)
            self.lblP3=ttk.Label(self.P3,text="Pregunta 3: Los algoritmos debe terminar después de\n\tun número determinado de pasos. (2p)").pack()
            self.radioValueP3=tk.IntVar()
            self.rdioOneP3 = tk.Radiobutton(self.P3,text="Verdadero",variable=self.radioValueP3,value=9).pack()
            self.rdioTwoP3 = tk.Radiobutton(self.P3,text="Falso",variable=self.radioValueP3,value=10).pack()

            self.P4=tk.Frame(self.ventanaEvaluacion)
            self.lblP4=ttk.Label(self.P4,text="Pregunta 4: ¿Cuál de los siguientes tipos de algoritmos da una solución\n\tinexacta pero dentro de un margen de error preestablecido? (2p)").pack()
            self.radioValueP4=tk.IntVar()
            self.rdioOneP4 = tk.Radiobutton(self.P4,text="Algoritmos aproximados.",variable=self.radioValueP4,value=11).pack()
            self.rdioTwoP4 = tk.Radiobutton(self.P4,text="Algoritmos de recorridos sobre grafos.",variable=self.radioValueP4,value=12).pack()
            self.rdioThreeP4 = tk.Radiobutton(self.P4,text="Algoritmos heurísticos.",variable=self.radioValueP4,value=13).pack()
            self.rdioFourP4 = tk.Radiobutton(self.P4,text="Algoritmos probabilistas.",variable=self.radioValueP4,value=14).pack()

            self.P5=tk.Frame(self.ventanaEvaluacion)
            self.lblP5=ttk.Label(self.P5,text="Pregunta 5: ¿Cuál de las siguientes opciones menciona técnicas usadas\n\tpara representar algoritmos sin ambigüedades? (2p)").pack()
            self.radioValueP5=tk.IntVar()
            self.rdioOneP5 = tk.Radiobutton(self.P5,text="Lenguaje natural y diagramas de flujo..",variable=self.radioValueP5,value=15).pack()
            self.rdioTwoP5 = tk.Radiobutton(self.P5,text="Seudocódigo y diagramas de flujo.",variable=self.radioValueP5,value=16).pack()
            self.rdioThreeP5 = tk.Radiobutton(self.P5,text="Seudocódigo y lenguaje natural.",variable=self.radioValueP5,value=17).pack()
            self.rdioFourP5 = tk.Radiobutton(self.P5,text="Ninguna de las anteriores.",variable=self.radioValueP5,value=18).pack()
            
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
        if(self.radioValueP1.get()==4):
            puntos+=2
        elif(self.radioValueP2.get()==8):
            puntos+=2
        elif(self.radioValueP3.get()==9):
            puntos+=2
        elif(self.radioValueP4.get()==11):   
            puntos+=2
        elif(self.radioValueP5.get()==16):
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
            tk.messagebox.showinfo('Regreso','Ahora va a volver a la ventana de teoria.')
            self.ventanaEvaluacion.destroy()
            self.k.deiconify()
      