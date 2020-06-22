import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

puntos=0

class Evaluacion():
    def __init__(self,VentanaTeoria):
        global puntos
        puntos=0
        self.k=VentanaTeoria
        self.k.withdraw()
        self.ventanaEvaluacion = tk.Toplevel(VentanaTeoria)
        self.ventanaEvaluacion.title("Evaluacion de Conceptos")
        self.ventanaEvaluacion.geometry("600x280")
        self.ventanaEvaluacion.configure(bg= '#024747')
        self.notebook=ttk.Notebook(self.ventanaEvaluacion)

        self.P1=tk.Frame(self.ventanaEvaluacion)
        self.lblP1=ttk.Label(self.P1,text="Pregunta 1: En Git, el HEAD commit es...\n",font=("bold")).pack()
        self.radioValueP1=tk.IntVar()
        self.rdioOneP1 = tk.Radiobutton(self.P1,text="Código que se ejecuta antes de hacer un commit.",variable=self.radioValueP1,value=1).pack()
        self.rdioTwoP1 = tk.Radiobutton(self.P1,text="El primer commit eliminado de un repositorio.",variable=self.radioValueP1,value=2).pack()
        self.rdioThreeP1 = tk.Radiobutton(self.P1,text="El commit predeterminado hecho durante el comando git init.",variable=self.radioValueP1,value=3).pack()
        self.rdioFourP1 = tk.Radiobutton(self.P1,text="El commit en el que estás actualmente.",variable=self.radioValueP1,value=4).pack()

        self.P2=tk.Frame(self.ventanaEvaluacion)
        self.lblP2=ttk.Label(self.P2,text="Pregunta 2: ¿Qué afirmación es verdadera sobre el siguiente comando?\n",font=("bold")).pack()
        self.lblCommandP2=ttk.Label(self.P2,text="git reset 844d1f7\n").pack()
        self.radioValueP2=tk.IntVar()
        self.rdioOneP2 = tk.Radiobutton(self.P2,text="HEAD se restablecerá al commit cuyo SHA comienza con 844d1f7.",variable=self.radioValueP2,value=5).pack()
        self.rdioTwoP2 = tk.Radiobutton(self.P2,text="El comando no funcionará sin la opción -m.",variable=self.radioValueP2,value=6).pack()
        self.rdioThreeP2 = tk.Radiobutton(self.P2,text="El comando no funcionará a menos que el SHA esté entre comillas.",variable=self.radioValueP2,value=7).pack()
        self.rdioFourP2 = tk.Radiobutton(self.P2,text="Debe escribirse como git 844d1f7 reset.",variable=self.radioValueP2,value=8).pack()
            
        self.P3=tk.Frame(self.ventanaEvaluacion)
        self.lblP3=ttk.Label(self.P3,text="Pregunta 3: ¿Qué comando elimina los cambios de\n\t archivo del área de ensayo?\n",font=("bold")).pack()
        self.radioValueP3=tk.IntVar()
        self.rdioOneP3 = tk.Radiobutton(self.P3,text="git reset HEAD filename",variable=self.radioValueP3,value=9).pack()
        self.rdioTwoP3 = tk.Radiobutton(self.P3,text="git add filename_1 filename_2",variable=self.radioValueP3,value=10).pack()
        self.rdioThreeP3 = tk.Radiobutton(self.P3,text="git checkout HEAD filename",variable=self.radioValueP3,value=11).pack()
        self.rdioFourP3 = tk.Radiobutton(self.P3,text="git reset SHA",variable=self.radioValueP3,value=12).pack()

        self.P4=tk.Frame(self.ventanaEvaluacion)
        self.lblP4=ttk.Label(self.P4,text="Pregunta 4: ¿Qué comando Git te permite ver los SHA\n\t de todos los commits anteriores?\n",font=("bold")).pack()
        self.radioValueP4=tk.IntVar()
        self.rdioOneP4 = tk.Radiobutton(self.P4,text="git reset SHA",variable=self.radioValueP4,value=13).pack()
        self.rdioTwoP4 = tk.Radiobutton(self.P4,text="git status",variable=self.radioValueP4,value=14).pack()
        self.rdioThreeP4 = tk.Radiobutton(self.P4,text="git checkout HEAD filename",variable=self.radioValueP4,value=15).pack()
        self.rdioFourP4 = tk.Radiobutton(self.P4,text="git log",variable=self.radioValueP4,value=16).pack()

        self.P5=tk.Frame(self.ventanaEvaluacion)
        self.lblP5=ttk.Label(self.P5,text="Pregunta 5: ¿Qué comando Git da la salida a continuación?\n",font=("bold")).pack()
        self.lblCommandP5=ttk.Label(self.P5,text="Unstaged changes after reset:\nM       file.txt").pack()
        self.radioValueP5=tk.IntVar()
        self.rdioOneP5 = tk.Radiobutton(self.P5,text="git add file.txt",variable=self.radioValueP5,value=17).pack()
        self.rdioTwoP5 = tk.Radiobutton(self.P5,text="git reset HEAD file.txt",variable=self.radioValueP5,value=18).pack()
        self.rdioThreeP5 = tk.Radiobutton(self.P5,text="git status",variable=self.radioValueP5,value=19).pack()
        self.rdioFourP5 = tk.Radiobutton(self.P5,text="git delete filename",variable=self.radioValueP5,value=20).pack()

        self.P6=tk.Frame(self.ventanaEvaluacion)
        self.lblP6=ttk.Label(self.P6,text="Pregunta 6: Accidentalmente eliminaste líneas de un archivo.\n\t ¿Qué comando puede deshacer tu error?\n",font=("bold")).pack()
        self.radioValueP6=tk.IntVar()
        self.rdioOneP6 = tk.Radiobutton(self.P6,text="git commit -m “message”",variable=self.radioValueP6,value=21).pack()
        self.rdioTwoP6 = tk.Radiobutton(self.P6,text="git add filename",variable=self.radioValueP6,value=22).pack()
        self.rdioThreeP6 = tk.Radiobutton(self.P6,text="git reset HEAD filename",variable=self.radioValueP6,value=23).pack()
        self.rdioFourP6 = tk.Radiobutton(self.P6,text="git checkout HEAD filename",variable=self.radioValueP6,value=24).pack()

        self.P7=tk.Frame(self.ventanaEvaluacion)
        self.lblP7=ttk.Label(self.P7,text="Pregunta 7: ¿Por qué usar los comandos de backtracking de Git?\n",font=("bold")).pack()
        self.radioValueP7=tk.IntVar()
        self.rdioOneP7 = tk.Radiobutton(self.P7,text="Para volver a un commit anterior.",variable=self.radioValueP7,value=25).pack()
        self.rdioTwoP7 = tk.Radiobutton(self.P7,text="Para descartar cambios en el directorio de trabajo.",variable=self.radioValueP7,value=26).pack()
        self.rdioThreeP7 = tk.Radiobutton(self.P7,text="Todos estos.",variable=self.radioValueP7,value=27).pack()
        self.rdioFourP7 = tk.Radiobutton(self.P7,text="Para deshacer un archivo del área de ensayo.",variable=self.radioValueP7,value=28).pack()

        self.P8=tk.Frame(self.ventanaEvaluacion)
        self.lblP8=ttk.Label(self.P8,text="Pregunta 8: ¿Por qué usar el comando a continuación?\n",font=("bold")).pack()
        self.lblCommandP8=ttk.Label(self.P8,text="git checkout HEAD filename\n").pack()
        self.radioValueP8=tk.IntVar()
        self.rdioOneP8 = tk.Radiobutton(self.P8,text="Para eliminar un archivo de un commit anterior.",variable=self.radioValueP8,value=29).pack()
        self.rdioTwoP8 = tk.Radiobutton(self.P8,text="Para restaurar un archivo en el directorio de trabajo para que se vea como lo hizo en el último commit.",variable=self.radioValueP8,value=30).pack()
        self.rdioThreeP8 = tk.Radiobutton(self.P8,text="Para mover el HEAD a un commit previo.",variable=self.radioValueP8,value=31).pack()
        self.rdioFourP8 = tk.Radiobutton(self.P8,text="Para remover el archivo del área de ensayo.",variable=self.radioValueP8,value=32).pack()
            
        self.btnRevisarP1 = Button(self.P1,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP2 = Button(self.P2,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP3 = Button(self.P3,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP4 = Button(self.P4,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP5 = Button(self.P5,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP6 = Button(self.P6,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP7 = Button(self.P7,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnRevisarP8 = Button(self.P8,text="Guardar respuesta",command=self.Revisar).pack(side = BOTTOM)
        self.btnTerminarIntento = Button(self.ventanaEvaluacion,text="Terminar intento",command=self.Terminar).pack(side= BOTTOM)
        self.notebook.add(self.P1,text="Pregunta 1")
        self.notebook.add(self.P2,text="Pregunta 2")
        self.notebook.add(self.P3,text="Pregunta 3")
        self.notebook.add(self.P4,text="Pregunta 4")
        self.notebook.add(self.P5,text="Pregunta 5")
        self.notebook.add(self.P6,text="Pregunta 6")
        self.notebook.add(self.P7,text="Pregunta 7")
        self.notebook.add(self.P8,text="Pregunta 8")
        self.notebook.pack()
            
    def Revisar(self):
        global puntos
        if(self.radioValueP1.get()==4):
            puntos+=2
        elif(self.radioValueP2.get()==5):
            puntos+=2
        elif(self.radioValueP3.get()==9):
            puntos+=2
        elif(self.radioValueP4.get()==16):   
            puntos+=2
        elif(self.radioValueP5.get()==18):
            puntos+=2
        elif(self.radioValueP6.get()==24):
            puntos+=2
        elif(self.radioValueP7.get()==27):
            puntos+=2
        elif(self.radioValueP8.get()==30):
            puntos+=2
    def Terminar(self):
        MsgBox = tk.messagebox.askquestion ('Terminar Intento','¿Esta seguro que desea terminar este intento?',icon = 'warning')
        if MsgBox == 'yes':
            if(puntos==16):
                messagebox.showinfo(message="Excelente, 8/8 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos>=10 and puntos < 16):
                messagebox.showinfo(message="Muy bien, minimo 5/8 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos>=6 and puntos <10):
                messagebox.showinfo(message="Bien, minimo 3/8 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos>=0 and puntos <6):
                messagebox.showinfo(message="Mal, no ha alcanzado el minimo para aprobar, intente nuevamente", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
                
        else:
            tk.messagebox.showinfo('Regreso','Ahora va a volver a la ventana de evaluacion.')
            self.k.deiconify()