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
        self.ventanaEvaluacion.geometry("790x410")
        self.notebook=ttk.Notebook(self.ventanaEvaluacion)
        self.Ej = PhotoImage(file="Expresiones/EJ.gif")
        self.EjEvaluacion = ttk.Label(self.ventanaEvaluacion,image=self.Ej,background="white")
        self.EjEvaluacion.image = self.Ej
        self.EjEvaluacion.place(x=0,y=0)

        self.P1=tk.Frame(self.ventanaEvaluacion)
        self.lblP1=ttk.Label(self.P1,text="Pregunta 1: ¿Cuál es el valor almacenado en total_compra al finalizar la ejecución del programa?").pack()
        self.radioValueP1=tk.IntVar()
        self.rdioOneP1 = tk.Radiobutton(self.P1,text="5636.25",variable=self.radioValueP1,value=1).pack()
        self.rdioTwoP1 = tk.Radiobutton(self.P1,text="6481",variable=self.radioValueP1,value=2).pack()
        self.rdioThreeP1 = tk.Radiobutton(self.P1,text="6481.6875",variable=self.radioValueP1,value=3).pack()
        self.rdioFourP1 = tk.Radiobutton(self.P1,text="7515",variable=self.radioValueP1,value=4).pack()

        self.P2=tk.Frame(self.ventanaEvaluacion)
        self.lblP2=ttk.Label(self.P2,text="Pregunta 2: ¿Cuál operador tiene precedencia (se evalúa primero) en la expresión que calcula\n\tel valor que luego se almacena en la variable precio_con_impuestos").pack()
        self.radioValueP2=tk.IntVar()
        self.rdioOneP2 = tk.Radiobutton(self.P2,text=":= (asignación)",variable=self.radioValueP2,value=5).pack()
        self.rdioTwoP2 = tk.Radiobutton(self.P2,text="* (multiplicación)",variable=self.radioValueP2,value=6).pack()
        self.rdioThreeP2 = tk.Radiobutton(self.P2,text="+ (suma)",variable=self.radioValueP2,value=7).pack()
        self.rdioFourP2 = tk.Radiobutton(self.P2,text="Todos los operadores en esa instrucción tienen el mismo nivel de precedencia.",variable=self.radioValueP2,value=8).pack()
            
        self.P3=tk.Frame(self.ventanaEvaluacion)
        self.lblP3=ttk.Label(self.P3,text="Pregunta 3: Los paréntesis no se pueden eliminar de la expresión que calcula el valor de\n\tprecio_con_descuento porque eso alteraría el orden de evaluación de los operadores.").pack()
        self.radioValueP3=tk.IntVar()
        self.rdioOneP3 = tk.Radiobutton(self.P3,text="Verdadero",variable=self.radioValueP3,value=9).pack()
        self.rdioTwoP3 = tk.Radiobutton(self.P3,text="Falso",variable=self.radioValueP3,value=10).pack()

        self.P4=tk.Frame(self.ventanaEvaluacion)
        self.lblP4=ttk.Label(self.P4,text="Pregunta 4: ¿Cuál de las siguientes expresiones con operadores relacionales es\n\tverdadera (regresa el valor verdadero) cuando se\n\tagrega al programa después de la última línea?").pack()
        self.radioValueP4=tk.IntVar()
        self.rdioOneP4 = tk.Radiobutton(self.P4,text="precio_con_descuento > precio_con_impuestos",variable=self.radioValueP4,value=11).pack()
        self.rdioTwoP4 = tk.Radiobutton(self.P4,text="precio_bruto = precio_con_impuestos",variable=self.radioValueP4,value=12).pack()
        self.rdioThreeP4 = tk.Radiobutton(self.P4,text="porcentaje_impuesto < porcentaje_descuento",variable=self.radioValueP4,value=13).pack()
        self.rdioFourP4 = tk.Radiobutton(self.P4,text="Ninguna de las anteriores.",variable=self.radioValueP4,value=14).pack()
            
        self.btnRevisarP1 = Button(self.P1,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP2 = Button(self.P2,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP3 = Button(self.P3,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP4 = Button(self.P4,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnTerminarIntento = Button(self.ventanaEvaluacion,text="Terminar intento",command=self.Terminar).pack(side= BOTTOM)
        self.notebook.add(self.EjEvaluacion,text="Ejercicio")
        self.notebook.add(self.P1,text="Pregunta 1")
        self.notebook.add(self.P2,text="Pregunta 2")
        self.notebook.add(self.P3,text="Pregunta 3")
        self.notebook.add(self.P4,text="Pregunta 4")
        self.notebook.pack()
            
    def Revisar(self):
        global puntos
        if(self.radioValueP1.get()==3):
            puntos+=2
        elif(self.radioValueP2.get()==6):
            puntos+=2
        elif(self.radioValueP3.get()==9):
            puntos+=2
        elif(self.radioValueP4.get()==13):   
            puntos+=2
    def Terminar(self):
        MsgBox = tk.messagebox.askquestion ('Terminar Intento','¿Esta seguro que desea terminar este intento?',icon = 'warning')
        if MsgBox == 'yes':
            if(puntos==10):
                messagebox.showinfo(message="Excelente, 4/4 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos==8):
                messagebox.showinfo(message="Muy bien, 3/4 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos==6):
                messagebox.showinfo(message="Bien, 2/4 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos>=0 and puntos <6):
                messagebox.showinfo(message="Mal, no ha alcanzado el minimo para aprobar, intente nuevamente", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
                
        else:
            tk.messagebox.showinfo('Regreso','Ahora va a volver a la ventana de evaluacion.')
            self.k.deiconify()
      