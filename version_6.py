# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 09:33:45 2022

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




suma=lambda x,y: x+y
divi=lambda x,y: x/y

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
            n1=int(input("Introduce un número: "))    
            n2=int(input("Introduce un número: "))   
            print( f"la suma de {n1} + {n2}= ",suma(n1,n2))
            
        elif opcion == 2:        
            restarPidiendo()
            
        elif opcion == 3:
            multiplicarPidiendo()
            
        elif opcion==4:
            print("")
            n1 = float(input("Introduce tu primer número: ") )
            n2 = float(input("Introduce tu segundo número: ") )
            if n2==0:
                  print("No se puede dividir por cero")
            else: 
                print(f"la división entre {n1} y {n2} = ", divi(n1,n2))
            
        elif opcion == 5:
               cociPidiendo()
               
        elif opcion == 6:
               restoPidiendo()
               
        elif opcion == 7:
            expPidiendo()
            
        elif opcion==8:
            areatriPidiendo()
            
        elif opcion==9:
            areacuaPidiendo()
            
        elif opcion==10:
            arearecPidiendo()
            
        elif opcion==11:
            areacirPidiendo()
            
        elif opcion == 12:
            break
        else:
            print("Opción incorrecta")