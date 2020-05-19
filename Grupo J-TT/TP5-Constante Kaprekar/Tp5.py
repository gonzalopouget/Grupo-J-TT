#Tp 5 Kaprekar-Metodología de la Investigación
from functools import reduce
def main():
    print("Ingrese la cantidad de numeros en los cuales desee averiguar su constante de Kaprekar.")
    Iteraciones=[]
    cantNumeros=(int(input("Cantidad => ")))#Aqui se pide el dato de cuantos numeros van usarse
    for _ in range(cantNumeros):#Este bucle va a estar funcionando hasta que se hayan ingresado la cantidad de numeros solicitados anteriormente
        num = input("Numero/s => ")#Aqui se piden los numeros de 4 digitos que uno desee
        cantIteraciones=0
        if(num=='6174'):#Si el numero ingresado es 6174, la cantidad de Iteraciones que necesita va a ser 0 ya que ese es el numero final al que se llega aplicando kaprekar
            cantIteraciones=0
        #Si es un repdigit, la cantidad de Iteraciones pasa a ser 8 porque no se puede sacar el kaprekar en dichos numeros
        elif(num=='0000' or num=='1111' or num=='2222' or num=='3333' or num=='4444' or num=='5555' or num =='6666' or num=='7777' or num=='8888' or num=='9999'):
            cantIteraciones=8

        elif(len(num)<4 or len(num) > 4):#Si por error se escribio un numero con 3 o menos o con 5 o mas lanza este error ya que si o si debe tener 4 para sacar kaprekar
            print("ERROR, numero con menos o con mas de 4 cifras.")
        else:
            cantIteraciones=0
    #mostrarNumeroIteraciones(Iteraciones,cantIteraciones)

def mostrarNumeroIteraciones(Iteraciones,cantIteraciones):#Aqui lo unico que hace es recorre la lista pasada como primer parametro a traves del segundo parametro que es un int
    for cantIteraciones in Iteraciones:
        print("Iteraciones => ", cantIteraciones)#Finalmente muestra una por una la cantidad de iteraciones que deben hacer los numeros para alcanzar la constante kaprekar

#main()