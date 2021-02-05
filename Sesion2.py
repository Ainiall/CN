# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 15:24:05 2019

@author: UO270318
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-1,1)
p=np.array([1.0,-1.0,2.0,-3.0,5.0,-2.0]) #float para que dibuje bien las graficas
q=np.copy(p)
#al definir un array por defecto es un vector fila
#para poder operar es mejor transponerlo
P=lambda x:np.dot(p,np.transpose([x**5,x**4,x**3,x**2,x**1,1]))
d1P=lambda x:np.dot(p,np.transpose([5*x**4,4*x**3,3*x**2,2*x,1,0])) #priemra derivada
d2P=lambda x:np.dot(p,np.transpose([20*x**3,12*x**2,6*x,2,0,0])) #segunda derivada


plt.plot(x,P(x),'b',label='Polinomio')
plt.plot(x,d1P(x),'y',label='Primera derivada')
plt.plot(x,d2P(x),'g--',label='Segunda derivada')
plt.plot(x,np.polyval(p,x),'r--',label='Polinomio con polyval') 
#polyval evalua el polinomio en un punto = P(x)
plt.plot(x,0*x,'k')
plt.legend()
plt.show()

#ALGORITMO DE HORNER
#se hace ruffini y se coge el resto como la imagen del polinomio en ese punto
def horner(p,x0):
    q=np.zeros_like(p)
    q[0]=p[0]
    for i in range(1,len(p)):
        q[i]=p[i]+q[i-1]*x0
    return q

Aux=horner(p,1)
#para buscar la ultima posicion del vector
#Aux[len(aux)-1] == Aux [-1]
#para obtener los valores de 0 a len-1
#Aux[0:-1] la ultima posicion no se incluye -> [1,0,2,-1,4] -> x^4 2x^2 -x +4

def HornerV(p,x):
    y=0*x 
    for i in range(0,len(x)):
        y[i]=horner(p,x[i])[-1]
    return y #evaluacion de p en cada pos de x

aux=HornerV(p,x)
plt.plot(x,aux,'g')

#misma grafica, distinto metodo
plt.plot(x,np.polyval(p,x),'y--')
plt.title('Polinomio P')
plt.show()

def derPol(p,x0):
    #devuelve la derivada 1,2,3,4,5
    der=np.zeros_like(p)
    factorial=1
    for i in range(0,len(p)):
        der[i]=horner(p,x0)[-1]*factorial #-1 para quedarse con la ultima evaluacion del vector
        factorial=factorial*(i+1)
        p=horner(p,x0)[0:-1] #coeficientes de 0 a len-1     
    return der

##### EJERCICIOS PROPUESTOS #####   
def derivadasSuc(p,x):
    #La variable de salida será una matriz Y que contendrá en la primera columna, los valores de P 
    #en los puntos de x, en la segunda columna, los valores de P′ en los puntos de x y así sucesivamente 
    #hasta la derivada n-ésima, siendo n el grado de P.
    y=np.zeros(len(x),n)
    i=1
    y[:,0]=HornerV(p,x)
    for i in range(0,len(p)):
        y[:,i]=derPol(p,i)
    return y
#dibujar los polinomios de p,p' y p''
p = np.array([1., -1., 2., -3., 5., -2.])

#??????
def hornerVect(p,x):
    y = np.zeros_like(x)
    q = np.zeros_like(p)
    
    for k in range(len(x)):
        x0 = x[k]
        
        q[0] = p[0]
        for i in range(1,len(p)):
            q[i] = q[i-1]*x0 + p[i]
        
        y[k] = q[-1]   
    return y   
