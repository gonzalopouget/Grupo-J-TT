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
        self.ventanaEvaluacion.geometry("490x220")
        self.notebook=ttk.Notebook(self.ventanaEvaluacion)
        self.P1=tk.Frame(self.ventanaEvaluacion)
        self.lblP1=ttk.Label(self.P1,text="Pregunta 1: Seleccione la opción que indica el tipo de subrutina que\n\tpuede regresar un valor al finalizar su ejecución.").pack()
        self.radioValueP1=tk.IntVar()
        self.rdioOneP1 = tk.Radiobutton(self.P1,text="Funciones",variable=self.radioValueP1,value=1).pack()
        self.rdioTwoP1 = tk.Radiobutton(self.P1,text="Procedimientos",variable=self.radioValueP1,value=2).pack()
        self.rdioThreeP1 = tk.Radiobutton(self.P1,text="Funciones y procedimientos",variable=self.radioValueP1,value=3).pack()
        self.rdioFourP1 = tk.Radiobutton(self.P1,text="Ninguna de las anteriores",variable=self.radioValueP1,value=4).pack()

        self.P2=tk.Frame(self.ventanaEvaluacion)
        self.lblP2=ttk.Label(self.P2,text="Pregunta 2: ¿Para qué sirven los parámetros?").pack()
        self.radioValueP2=tk.IntVar()
        self.rdioOneP2 = tk.Radiobutton(self.P2,text="Transferir información.",variable=self.radioValueP2,value=5).pack()
        self.rdioTwoP2 = tk.Radiobutton(self.P2,text="Calcular valores complejos.",variable=self.radioValueP2,value=6).pack()
        self.rdioThreeP2 = tk.Radiobutton(self.P2,text="Ejecutar tareas.",variable=self.radioValueP2,value=7).pack()
        self.rdioFourP2 = tk.Radiobutton(self.P2,text="Todas las anteriores.",variable=self.radioValueP2,value=8).pack()
            
        self.P3=tk.Frame(self.ventanaEvaluacion)
        self.lblP3=ttk.Label(self.P3,text="Pregunta 3:¿Cuál de los siguientes tipos de variables es visible solo son visibles dentro de una subrutina?").pack()
        self.radioValueP3=tk.IntVar()
        self.rdioOneP3 = tk.Radiobutton(self.P3,text="Locales",variable=self.radioValueP3,value=9).pack()
        self.rdioTwoP3 = tk.Radiobutton(self.P3,text="Globales",variable=self.radioValueP3,value=10).pack()
        self.rdioThreeP3 = tk.Radiobutton(self.P3,text="Locales y globales",variable=self.radioValueP3,value=11).pack()
        self.rdioFourP3 = tk.Radiobutton(self.P3,text="Ninguna de las anteriores",variable=self.radioValueP3,value=12).pack()

        self.P4=tk.Frame(self.ventanaEvaluacion)
        self.lblP4=ttk.Label(self.P4,text="Pregunta 4: Modificar el valor de las variables globales dentro del cuerpo de una\n\tsubrutina es considerado una buena práctica de programación.").pack()
        self.radioValueP4=tk.IntVar()
        self.rdioOneP4 = tk.Radiobutton(self.P4,text="Verdadero",variable=self.radioValueP4,value=13).pack()
        self.rdioTwoP4 = tk.Radiobutton(self.P4,text="Falso",variable=self.radioValueP4,value=14).pack()

        self.P5=tk.Frame(self.ventanaEvaluacion)
        self.lblP5=ttk.Label(self.P5,text="Pregunta 5: ¿Cuál de los siguientes tipos de variables es visible tanto\n\tdentro como fuera del cuerpo de una subrutina?").pack()
        self.radioValueP5=tk.IntVar()
        self.rdioOneP5 = tk.Radiobutton(self.P5,text="Locales",variable=self.radioValueP5,value=15).pack()
        self.rdioTwoP5 = tk.Radiobutton(self.P5,text="Globales",variable=self.radioValueP5,value=16).pack()
        self.rdioThreeP5 = tk.Radiobutton(self.P5,text="Locales y globales",variable=self.radioValueP5,value=17).pack()
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
        if(self.radioValueP1.get()==1):
            puntos+=2
        elif(self.radioValueP2.get()==5 ):
            puntos+=2
        elif(self.radioValueP3.get()==9):
            puntos+=2
        elif(self.radioValueP4.get()==14):   
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
            tk.messagebox.showinfo('Regreso','Ahora va a volver a la ventana de evaluacion.')
            self.k.deiconify()
      