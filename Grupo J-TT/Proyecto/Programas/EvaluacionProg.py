import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

puntos=0

class EvaluacionProg():
    def __init__(self,VentanaTeoria):
        self.k=VentanaTeoria
        self.k.withdraw()
        self.ventanaEvaluacion = tk.Toplevel(VentanaTeoria)
        self.ventanaEvaluacion.title("Evaluacion de Conceptos")
        self.ventanaEvaluacion.geometry("950x220")
        self.notebook=ttk.Notebook(self.ventanaEvaluacion)
        self.P1=tk.Frame(self.ventanaEvaluacion)
        self.lblP1=ttk.Label(self.P1,text="Pregunta 1: Los computadores pueden ejecutar directamente los algoritmos.").pack()
        self.radioValueP1=tk.IntVar()
        self.rdioOneP1 = tk.Radiobutton(self.P1,text="Verdadero.",variable=self.radioValueP1,value=1).pack()
        self.rdioTwoP1 = tk.Radiobutton(self.P1,text="Falso.",variable=self.radioValueP1,value=2).pack()

        self.P2=tk.Frame(self.ventanaEvaluacion)
        self.lblP2=ttk.Label(self.P2,text="Pregunta 2: ¿Cuál de las siguientes afirmaciones sobre los programas de computadora es incorrecta?").pack()
        self.radioValueP2=tk.IntVar()
        self.rdioOneP2 = tk.Radiobutton(self.P2,text="Los programas continúan cambiando a lo largo de su ciclo de vida para adaptarse a las necesidades de los usuarios.",variable=self.radioValueP2,value=3).pack()
        self.rdioTwoP2 = tk.Radiobutton(self.P2,text="Las personas que traducen los algoritmos en secuencias de instrucciones que los ordenadores pueden comprender se denominan programadores.",variable=self.radioValueP2,value=4).pack()
        self.rdioThreeP2 = tk.Radiobutton(self.P2,text="El ciclo de vida de un programa consiste en determinar cómo se pueden satisfacer las necesidades de los usuarios.",variable=self.radioValueP2,value=5).pack()
        self.rdioFourP2 = tk.Radiobutton(self.P2,text="Durante la depuración los programas se comprueban cuidadosamente\npara identificar y corregir cualquier error que puede haber sido introducido durante su implementación.",variable=self.radioValueP2,value=6).pack()
            
        self.P3=tk.Frame(self.ventanaEvaluacion)
        self.lblP3=ttk.Label(self.P3,text="Pregunta 3: ¿Cuál de las siguientes opciones hace referencia a la etapa de diseño de un programa?").pack()
        self.radioValueP3=tk.IntVar()
        self.rdioOneP3 = tk.Radiobutton(self.P3,text="Decidir exactamente que debe hacer un programa.",variable=self.radioValueP3,value=7).pack()
        self.rdioTwoP3 = tk.Radiobutton(self.P3,text="Decidir cómo se implementarán las necesidades de los usuarios.",variable=self.radioValueP3,value=8).pack()
        self.rdioThreeP3 = tk.Radiobutton(self.P3,text="Expresar los algoritmos de forma que las computadoras los puedan comprender y ejecutar.",variable=self.radioValueP3,value=9).pack()
        self.rdioFourP3 = tk.Radiobutton(self.P3,text="Identificar e implementar cambios para ajustar los programas a las necesidades cambiantes de los usuarios.",variable=self.radioValueP3,value=10).pack()

        self.P4=tk.Frame(self.ventanaEvaluacion)
        self.lblP4=ttk.Label(self.P4,text="Pregunta 4: Solo existe un programa de computador posible para resolver un problema determinado.").pack()
        self.radioValueP4=tk.IntVar()
        self.rdioOneP4 = tk.Radiobutton(self.P4,text="Verdadero.",variable=self.radioValueP4,value=11).pack()
        self.rdioTwoP4 = tk.Radiobutton(self.P4,text="Falso.",variable=self.radioValueP4,value=12).pack()

        self.P5=tk.Frame(self.ventanaEvaluacion)
        self.radioValueP5=tk.IntVar()
        self.lblP5=ttk.Label(self.P5,text="Pregunta 5: ¿Cuál de las siguientes características de los programas se refiere a la facilidad de implementar cambios\n\tpara ajustarlos a las necesidades de los usuarios?").pack()
        self.rdioOneP5 = tk.Radiobutton(self.P5,text="Eficiencia.",variable=self.radioValueP5,value=13).pack()
        self.rdioTwoP5 = tk.Radiobutton(self.P5,text="Exactitud.",variable=self.radioValueP5,value=14).pack()
        self.rdioThreeP5 = tk.Radiobutton(self.P5,text="Mantenibilidad.",variable=self.radioValueP5,value=15).pack()
        self.rdioFourP5 = tk.Radiobutton(self.P5,text="Usabilidad.",variable=self.radioValueP5,value=16).pack()
            
        self.btnRevisarP1 = Button(self.P1,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP2 = Button(self.P2,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP3 = Button(self.P3,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP4 = Button(self.P4,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP5 = Button(self.P5,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnTerminarIntento = Button(self.ventanaEvaluacion,text="Terminar intento",command=self.Terminar).pack(side= BOTTOM)
        self.notebook.add(self.P1,text="Pregunta 1")
        self.notebook.add(self.P2,text="Pregunta 2")
        self.notebook.add(self.P3,text="Pregunta 3")
        self.notebook.add(self.P4,text="Pregunta 4")
        self.notebook.add(self.P5,text="Pregunta 5")
        self.notebook.pack()
            
    def Revisar(self):
        global puntos
        if(self.radioValueP1.get()==2):
            puntos+=2
        elif(self.radioValueP2.get()==5):
            puntos+=2
        elif(self.radioValueP3.get()==8):
            puntos+=2
        elif(self.radioValueP4.get()==12):   
            puntos+=2
        elif(self.radioValueP5.get()==15):
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
      