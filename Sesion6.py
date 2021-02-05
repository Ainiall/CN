# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:11:11 2019

@author: UO270318
"""

import numpy as np
import matplotlib.pyplot as plt

from scipy import integrate #integrales


x=np.linspace(-1,1,5) #de -1 a 1 con 5 puntos equidistantes
f= lambda x:np.cos(x)
y=f(x)

## METODO QUE DEVUELVE LAS MATRICES B Y N 
def Matrices(x,y,gr):
    m= len(x)
    #columna es grado mas 1 y fila es longitud de x
    M=np.zeros((m,gr+1))
    
    for i in range(0,m):
        #tambien se puede poner M[:,j] para recorrerlo
         for j in range(0,gr+1):
           M[i,j]=x[i]**j
    aux= np.transpose(M) #transpuesta M
    N= np.dot(aux,M) #producto matricial transpuesta m con m
    B = np.dot(aux,y) #producto matricial transpuesta m con y
    
    return N,B
    

N,B=Matrices(x,y,2)    

def PolinomioAprox(x,y,gr):
    N, B = Matrices(x,y,gr)
    aux= np.linalg.solve(N,B)
    A= aux[::-1] #invierte el vector
    return A

xp=np.linspace(-1,1) #todos los puntos
plt.plot(x,np.polyval(PolinomioAprox(x,y,2),x),'ro',label='nodos') #puntos = nodos
plt.plot(xp,np.polyval(PolinomioAprox(x,y,2),xp),'b', label='funcion aproximada')
plt.legend()
plt.show()

#----------------------  Error 1
Er1 = np.linalg.norm(f(xp)-np.polyval(PolinomioAprox(x,y,2),xp))/np.linalg.norm(f(xp))
print('Er1 = ', Er1)


x=np.linspace(-1,1,10)
f = lambda x:np.cos(np.arctan(x))-np.exp(x**2)*np.log(x+2)
y=f(x)
xp=np.linspace(-1,1) #todos los puntos
plt.plot(x,np.polyval(PolinomioAprox(x,y,4),x),'ro',label='nodos') #puntos = nodos
plt.plot(xp,np.polyval(PolinomioAprox(x,y,4),xp),'b', label='funcion aproximada')
plt.legend()
plt.show()


## APROXIMACION POLINOMICA CONTINUA
def Matrices_Cont(f,a,b,gr):
    n=gr+1
    N=np.zeros((n,n))
    B=np.zeros(n)
    for i in range(0,n):
        h= lambda z: f(z)*z**(i)
        B[i]= integrate.quad(h,a,b)[0]
        for j in range(0,n):
            g=lambda z: z**(i+j)
            N[i,j]=integrate.quad(g,a,b)[0] #matriz de coeficientes
    return N,B 

def PolinomioAprox_Cont(f,a,b,gr):
    N, B = Matrices_Cont(f,a,b,gr)
    aux= np.linalg.solve(N,B) #solucion sistema
    A= aux[::-1] #invierte el vector
    return A 

plt.plot()
x=np.linspace(-1,1)
f = lambda x:np.cos(x)
y=f(x)
xp=np.linspace(-1,1) #todos los puntos
plt.plot(x,np.polyval(PolinomioAprox_Cont(f,-1,1,2),x),'r',label='nodos') #puntos = nodos
plt.plot(xp,np.polyval(PolinomioAprox_Cont(f,-1,1,2),xp),'b', label='funcion aproximada')
plt.legend()
plt.show()