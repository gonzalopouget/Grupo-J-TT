#Tp 5 Kaprekar-Metodología de la Investigación
# usamos el IDLE y el Visual Studio Code para hacer el trabajo, editarlo y ejecutarlo
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
            while num != '6174':#Aqui se toma el caso que falta que es cuando cumple las necesidades de 4 cifras y no ser ninguno de los otros caso, y entra en bucle hasta llegar a 6174
                ordenadoMenorMayor=ordenarLasCifras(num,0)#Se crea el menor numero posible ordenando las cifras de menor a mayor
                ordenadoMayorMenor=ordenarLasCifras(num,1)#Se crea el mayor numero posible ordenando las cifras de mayor a menor
                num=agregarCerosAlFinal(str(ordenadoMayorMenor-ordenadoMenorMayor))#Se hace la resta y se agregan 0 al final en caso de necesitarlo
                cantIteraciones+=1#Se va incrementando esta variable cada vez que reste los numeros y no se haya llegado a 6174 como resultado
        Iteraciones.append(cantIteraciones)#Aqui se agregan las cantidades de iteraciones por cada numero ingresado
    mostrarNumeroIteraciones(Iteraciones,cantIteraciones)#Finalmente se muestran

def ordenarLasCifras(num, orden):#En esta funcion se ordenan las cifras del numero pasado como primer parametro, y el segundo parametro es para aplicar el orden en el que se van a ordenar
    if orden == 0:#Si es 0 se ordenan las cifras de menor a mayor para formar el menor numero posible
        lista = sorted([c for c in num], reverse=False)
        cifrasOrdenadas = int(reduce(lambda x, y: x + y, lista))
    elif orden == 1:#Si es 1 se ordenan de mayor a menor formando asi el mayor numero posible
        lista = sorted([c for c in num], reverse=True)
        cifrasOrdenadas = int(reduce(lambda x, y: x + y, lista))
    return cifrasOrdenadas#Finalmente se retorna el valor que se haya formado en alguno de los casos


def agregarCerosAlFinal(num):#En esta funcion lo que se hace es agregarle 0 al final al numero que se pase por parametro 
    if len(num) < 4:
        num += '0' * (4 - len(num))
    return num
    

def mostrarNumeroIteraciones(Iteraciones,cantIteraciones):#Aqui lo unico que hace es recorre la lista pasada como primer parametro a traves del segundo parametro que es un int
    for cantIteraciones in Iteraciones:
        print("Iteraciones => ", cantIteraciones)#Finalmente muestra una por una la cantidad de iteraciones que deben hacer los numeros para alcanzar la constante kaprekar

main()