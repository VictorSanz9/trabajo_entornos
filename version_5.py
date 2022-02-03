# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:07:19 2022

@author: VíctorSanzMiguens
"""


import math
def sumarPidiendo():
    print(" ")
    n1=int(input("Introduce un número: "))    
    n2=int(input("Introduce un número: "))    
    print(f"{n1}+{n2}={n1+n2}")
    return n1+n2  
def restarPidiendo():
    print("")
    n1=int(input("Introduce un número: "))    
    n2=int(input("Introduce un número: "))    
    print(f"{n1}-{n2}={n1-n2}")
    return n1-n2  

def multiplicarPidiendo():
    print("")
    n1=int(input("Introduce un número: "))    
    n2=int(input("Introduce un número: "))    
    print(f"{n1}*{n2}={n1*n2}")
    return n1*n2  

def divPidiendo():
    print("")
    n1 = float(input("Introduce tu primer número: ") )
    n2 = float(input("Introduce tu segundo número: ") )
    if n2==0:
          print("No se puede dividir por cero")
    else: 
          print("Resultado: la division de", n1,"/",n2,"es igual a", n1/n2)
    return n1/n2  

def cociPidiendo():
    print("")
    n1 = float(input("Introduce tu primer número: ") )
    n2 = float(input("Introduce tu segundo número: ") )
    print("Resultado: el cociente de", n1,"//",n2,"es igual a", n1//n2)
    return n1//n2 
 
def restoPidiendo():
    print("")
    n1 = float(input("Introduce tu primer número: ") )
    n2 = float(input("Introduce tu segundo número: ") )
    print("Resultado: resto de", n1,"%",n2,"es igual a", n1%n2)
    return n1%n2  

 
def expPidiendo():
    print("")
    n1 = float(input("Introduce tu primer número: ") )
    n2 = float(input("Introduce tu segundo número: ") )
    print("Resultado: exponencial de", n1,"**",n2,"es igual a", n1**n2)
    return n1**n2  

def areatriPidiendo():
    print("")
    n1 = float(input("Introduce base triangulo: ") )
    n2 = float(input("Introduce altura del traingulo: ") )
    print ("el area del triángulo es:",n1*n2/2)
    return n1*n2/2 

def areacuaPidiendo():
    print("")
    n1=float(input("introduce lado del cuadrado "))
    print ("el area del cuadrado es",n1**2)
    return n1**2

def arearecPidiendo():
    print("")
    n1 = float(input("Introduce base del rectangulo: ") )
    n2 = float(input("Introduce altura del rectangulo: ") )
    print ("el area del rectangulo es:",n1*n2)
    return n1*n2

def areacirPidiendo():
    print("")
    n1 = float(input("Introduce radio del circulo: ") )
    print ("el area del circulo es:",round(math.pi*n1**2,2))
    
    return math.pi*n1**2


while True:
        print("""
    -------------------------------------------------------------------------------          
        Dime, ¿qué quieres hacer?
        
        1) Sumar los dos números
        2) Restar los dos números
        3) Multiplicar los dos números
        4) Dividir los dos números 
        5) Cociente de los números
        6) Resto de los números
        7) Exponencial de los números
        8) Area triangulo
        9) Area cuadrado
        10) Area rectángulo
        11) Area círculo
        12) Apagar 
    -------------------------------------------------------------------------------    
        
        """)
        opcion = int(input("Elige una opción: ") )     

        if opcion == 1:            
            print(" ")
          
            
        elif opcion == 2:        
            print("")
            
        elif opcion == 3:
            print("")
            
        elif opcion==4:
            print("")
    
        elif opcion == 5:
            print("")
               
        elif opcion == 6:
               print("")
               
        elif opcion == 7:
            print("")
            
        elif opcion==8:
            print("")
            
        elif opcion==9:
            print("")
            
        elif opcion==10:
            print("")

            
        elif opcion==11:
            print("")
           
        elif opcion == 12:
           break
        else:
           print("Opción incorrecta")
#arreglado bug del menú 