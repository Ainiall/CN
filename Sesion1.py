# -*- coding: utf-8 -*-
"""
06/02/19

@autor Ángela López UO270318
"""

import numpy as np
import matplotlib.pyplot as plt

#np.exp(n)
#np.sqrt(n)

#Definir una funcion tipo lambda
f=lambda x:np.exp(x)

#Dibujar la funcion exp en cierto intervalo
a=-1; b=1; #declaracion de variables
x=np.linspace(a,b) #de a hasta b, con n puntos (array desde pos 0)

##si se usan posiciones negativas ej x[-1] muestra las posiciones empezando por la ultima

for i in range(0,len(x)):
    print(x[i]) #print actua como println, salto de linea entre ans
y=f(x)
plt.plot(x,y,'g*',label='Grafuca de exponencial')
 # * representa los puntos mostrando ese simbolo
plt.plot(x,0*x,'r+',label='Eje OX') #k para usar el color negro
plt.legend()
plt.plot(x,np.sin(x),'p-',label='Seno')
plt.legend()
plt.show() #devuelve en una ventana lo surgido hasta la fecha, y en una nueva lo posterior
plt.plot(x,np.tan(x),'yo',label='Tangente')
plt.show()

#FUNCION A TROZOS
def trozos(x):
    y=0*x
    for i in range(0,len(x)): 
        if x[i]> 1/2: 
            y[i]=x[i]
        else:
            y[i]=1-x[i]
    
    return y
plt.plot(x,trozos(x),'b')
plt.show()

#POLINOMIO DE TAYLOR
def Poli_Taylor(x0,gr):
    polinomio=0
    factorial=1
    for i in range(0,gr+1): # ** elevado
        polinomio=polinomio+x0**i/factorial
        factorial=factorial*(i+1)
        
    return polinomio

plt.plot(x,Poli_Taylor(x,4),'r',label='Polinomio de Taylor')
plt.plot(x,np.exp(x),'b--',label='Exponencial') #-- trazo discontinuo
plt.legend()
for i in range(0,6):
    plt.plot(x,Poli_Taylor(x,i),label='Polinomio de Taylor de orden '+str(i))
plt.legend()
plt.show()


##### EJERCICIOS PROPUESTOS #####
tol=1.*10**(-6)

def FunAprox(x0,tol):
    sumando=1
    factorial=1
    polinomio= sumando
    maxNumSum=100
    nSumandos=1
    while abs(sumando) > tol and nSumandos < maxNumSum:
        sumando = (x0**nSumandos)/factorial #al utilizar array se asigna un array a sumando
        polinomio=polinomio+sumando
        factorial=factorial*(nSumandos+1)
        nSumandos=nSumandos+1
    return polinomio, nSumandos


maxNumSum=100
def FunAproxMod(x,tol):
    sumando=1
    factorial=1
    polinomio=sumando
    maxNumSum=100
    nSumandos=1
    #al usar un array se pone np.max(abs(sumando))
    while np.max(abs(sumando)) > tol and nSumandos < maxNumSum:
        sumando = (x**nSumandos)/factorial
        polinomio=polinomio+sumando
        factorial=factorial*(nSumandos+1)
        nSumandos=nSumandos+1
    return polinomio
   
    

def FunExp(x,tol,maxNumSum):
    sumando=1
    factorial=1
    polinomio=sumando
    nSumandos=1
    #al usar un array se pone np.max(abs(sumando))
    while np.max(abs(sumando)) > tol and nSumandos < maxNumSum:
        sumando = (x**nSumandos)/factorial
        polinomio=polinomio+sumando
        factorial=factorial*(nSumandos+1)
        nSumandos=nSumandos+1
    return polinomio

plt.plot(x,FunExp(x,10**-6,100),'r',label='Aproximacion')
plt.plot(x,y,'b--',label='Funcion exponencial')
plt.legend()
plt.show()







        
        
        
