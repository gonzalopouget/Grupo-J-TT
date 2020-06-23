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
        self.ventanaEvaluacion.geometry("530x300")
        self.notebook=ttk.Notebook(self.ventanaEvaluacion)

        self.P1=tk.Frame(self.ventanaEvaluacion)
        self.lblP1=ttk.Label(self.P1,text="Pregunta 1: ¿Qué comando busca “Gambino” recursivamente en todos los archivos?").pack()
        self.radioValueP1=tk.IntVar()
        self.rdioOneP1 = tk.Radiobutton(self.P1,text="grep -R “Gambino” .",variable=self.radioValueP1,value=1).pack()
        self.rdioTwoP1 = tk.Radiobutton(self.P1,text="grep Gambino | *",variable=self.radioValueP1,value=2).pack()
        self.rdioThreeP1 = tk.Radiobutton(self.P1,text="grep “Gambino”",variable=self.radioValueP1,value=3).pack()
        self.rdioFourP1 = tk.Radiobutton(self.P1,text="grep -a “Gambino”",variable=self.radioValueP1,value=4).pack()

        self.P2=tk.Frame(self.ventanaEvaluacion)
        self.lblP2=ttk.Label(self.P2,text="Pregunta 2: ¿Que comando busca “Earl” en el archivo greatest.txt\n y luego envía los resultados al archivo oddfuture.txt.?").pack()
        self.radioValueP2=tk.IntVar()
        self.rdioOneP2 = tk.Radiobutton(self.P2,text="grep “Earl” greatest.txt | oddfuture.txt",variable=self.radioValueP2,value=5).pack()
        self.rdioTwoP2 = tk.Radiobutton(self.P2,text="grep “Earl” greatest.txt cat oddfuture.txt",variable=self.radioValueP2,value=6).pack()
        self.rdioThreeP2 = tk.Radiobutton(self.P2,text="grep “Earl” oddfuture.txt",variable=self.radioValueP2,value=7).pack()
        self.rdioFourP2 = tk.Radiobutton(self.P2,text="grep “Earl” greatest.txt >> oddfuture.txt",variable=self.radioValueP2,value=8).pack()
            
        self.P3=tk.Frame(self.ventanaEvaluacion)
        self.lblP3=ttk.Label(self.P3,text="Pregunta 3: ¿Que comando agrega la cadena “Aesop Rock” al archivo greatest.txt?").pack()
        self.radioValueP3=tk.IntVar()
        self.rdioOneP3 = tk.Radiobutton(self.P3,text="cat “Aesop Rock” > greatest.txt",variable=self.radioValueP3,value=9).pack()
        self.rdioTwoP3 = tk.Radiobutton(self.P3,text="echo “Aesop Rock” >> greatest.txt",variable=self.radioValueP3,value=10).pack()
        self.rdioThreeP3 = tk.Radiobutton(self.P3,text="Ninguno de estas.",variable=self.radioValueP3,value=11).pack()
        self.rdioFourP3 = tk.Radiobutton(self.P3,text="cat “Aesop Rock” >> greatest.txt",variable=self.radioValueP3,value=12).pack()

        self.P4=tk.Frame(self.ventanaEvaluacion)
        self.lblP4=ttk.Label(self.P4,text="Pregunta 4: ¿Qué comando imprime la cadena “Lamar” en el archivo greatest.txt?").pack()
        self.radioValueP4=tk.IntVar()
        self.rdioOneP4 = tk.Radiobutton(self.P4,text="echo “Lamar” < greatest.txt",variable=self.radioValueP4,value=13).pack()
        self.rdioTwoP4 = tk.Radiobutton(self.P4,text="cat “Lamar” greatest.txt",variable=self.radioValueP4,value=14).pack()
        self.rdioThreeP4 = tk.Radiobutton(self.P4,text="echo “Lamar” > greatest.txt",variable=self.radioValueP4,value=15).pack()
        self.rdioFourP4 = tk.Radiobutton(self.P4,text="mv “Lamar” greatest.txt",variable=self.radioValueP4,value=16).pack()

        self.P5=tk.Frame(self.ventanaEvaluacion)
        self.lblP5=ttk.Label(self.P5,text="Pregunta 5: El comando echo toma una cadena como ____ e imprime esa cadena como ____.").pack()
        self.radioValueP5=tk.IntVar()
        self.rdioOneP5 = tk.Radiobutton(self.P5,text="Salida estandar, Entrada estandar",variable=self.radioValueP5,value=17).pack()
        self.rdioTwoP5 = tk.Radiobutton(self.P5,text="Error estandar, Salida estandar.",variable=self.radioValueP5,value=18).pack()
        self.rdioThreeP5 = tk.Radiobutton(self.P5,text="Entrada estandar, Salida estandar.",variable=self.radioValueP5,value=19).pack()
        self.rdioFourP5 = tk.Radiobutton(self.P5,text="Entrada estandar, Error estandar.",variable=self.radioValueP5,value=20).pack()

        self.P6=tk.Frame(self.ventanaEvaluacion)
        self.lblP6=ttk.Label(self.P6,text="Pregunta 6: El comando uniq elimina duplicados ____.").pack()
        self.radioValueP6=tk.IntVar()
        self.rdioOneP6 = tk.Radiobutton(self.P6,text="Solo si son adyacentes.",variable=self.radioValueP6,value=21).pack()
        self.rdioTwoP6 = tk.Radiobutton(self.P6,text="Ninguno de estas.",variable=self.radioValueP6,value=22).pack()
        self.rdioThreeP6 = tk.Radiobutton(self.P6,text="De toda la entrada.",variable=self.radioValueP6,value=23).pack()
        self.rdioFourP6 = tk.Radiobutton(self.P6,text="Si estan separados.",variable=self.radioValueP6,value=24).pack()

        self.P7=tk.Frame(self.ventanaEvaluacion)
        self.lblP7=ttk.Label(self.P7,text="Pregunta 7: ¿Qué comandos ordenarían el contenido del archivo greatest.txt y los imprimirían?").pack()
        self.radioValueP7=tk.IntVar()
        self.rdioOneP7 = tk.Radiobutton(self.P7,text="Ninguno de estas",variable=self.radioValueP7,value=25).pack()
        self.rdioTwoP7 = tk.Radiobutton(self.P7,text="echo greatest.txt > sort",variable=self.radioValueP7,value=26).pack()
        self.rdioThreeP7 = tk.Radiobutton(self.P7,text="cat greatest.txt >> sort",variable=self.radioValueP7,value=27).pack()
        self.rdioFourP7 = tk.Radiobutton(self.P7,text="cat greatest.txt | sort",variable=self.radioValueP7,value=28).pack()

        self.P8=tk.Frame(self.ventanaEvaluacion)
        self.lblP8=ttk.Label(self.P8,text="Pregunta 8: ¿Qué significa s en la parte 's/Hopsin/Kanye' de sed 's/Hopsin/Kanye'?").pack()
        self.radioValueP8=tk.IntVar()
        self.rdioOneP8 = tk.Radiobutton(self.P8,text="Severo.",variable=self.radioValueP8,value=29).pack()
        self.rdioTwoP8 = tk.Radiobutton(self.P8,text="Secundario.",variable=self.radioValueP8,value=30).pack()
        self.rdioThreeP8 = tk.Radiobutton(self.P8,text="Sustituir.",variable=self.radioValueP8,value=31).pack()
        self.rdioFourP8 = tk.Radiobutton(self.P8,text="Sondar.",variable=self.radioValueP8,value=32).pack()

        self.P9=tk.Frame(self.ventanaEvaluacion)
        self.lblP9=ttk.Label(self.P9,text="Pregunta 9: ¿Qué hace el símbolo <?").pack()
        self.radioValueP9=tk.IntVar()
        self.rdioOneP9 = tk.Radiobutton(self.P9,text="Redireccionar la entrada a un comando.",variable=self.radioValueP6,value=33).pack()
        self.rdioTwoP9 = tk.Radiobutton(self.P9,text="Comandos de salida.",variable=self.radioValueP6,value=34).pack()
        self.rdioThreeP9 = tk.Radiobutton(self.P9,text="1 y 2.",variable=self.radioValueP6,value=35).pack()
        self.rdioFourP9 = tk.Radiobutton(self.P9,text="Agregar el comando a un archivo.",variable=self.radioValueP6,value=36).pack()

        self.P10=tk.Frame(self.ventanaEvaluacion)
        self.lblP10=ttk.Label(self.P10,text="Pregunta 10: ¿Cómo canalizarías los resultados de un comando a otro?").pack()
        self.radioValueP10=tk.IntVar()
        self.rdioOneP10 = tk.Radiobutton(self.P10,text="command >> command",variable=self.radioValueP10,value=37).pack()
        self.rdioTwoP10 = tk.Radiobutton(self.P10,text="command | command",variable=self.radioValueP10,value=38).pack()
        self.rdioThreeP10 = tk.Radiobutton(self.P10,text="command < command",variable=self.radioValueP10,value=39).pack()
        self.rdioFourP10 = tk.Radiobutton(self.P10,text="command > command",variable=self.radioValueP10,value=40).pack()
            
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
        self.btnTerminarIntento = Button(self.ventanaEvaluacion,text="Terminar intento",command=self.Terminar).pack(side= BOTTOM)
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
        self.notebook.pack()
            
    def Revisar(self):
        global puntos
        if(self.radioValueP1.get()==1):
            puntos+=2
        elif(self.radioValueP2.get()==8):
            puntos+=2
        elif(self.radioValueP3.get()==10):
            puntos+=2
        elif(self.radioValueP4.get()==15):   
            puntos+=2
        elif(self.radioValueP5.get()==19):
            puntos+=2
        elif(self.radioValueP6.get()==21):
            puntos+=2
        elif(self.radioValueP7.get()==28):
            puntos+=2
        elif(self.radioValueP8.get()==31):
            puntos+=2
        elif(self.radioValueP9.get()==33):
            puntos+=2
        elif(self.radioValueP10.get()==38):
            puntos+=2
    def Terminar(self):
        MsgBox = tk.messagebox.askquestion ('Terminar Intento','¿Esta seguro que desea terminar este intento?',icon = 'warning')
        if MsgBox == 'yes':
            if(puntos==20):
                messagebox.showinfo(message="Excelente, 10/10 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos>=10 and puntos < 20):
                messagebox.showinfo(message="Muy bien, minimo 5/10 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos>=6 and puntos <10):
                messagebox.showinfo(message="Bien, minimo 3/10 respuestas correctas.", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
            elif(puntos>=0 and puntos <6):
                messagebox.showinfo(message="Mal, no ha alcanzado el minimo para aprobar, intente nuevamente", title="Nota")
                self.ventanaEvaluacion.destroy()
                self.k.deiconify()
                
        else:
            tk.messagebox.showinfo('Regreso','Ahora va a volver a la ventana de evaluacion.')
            self.k.deiconify()