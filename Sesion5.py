# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:38:12 2019

@author: UO270318
"""
import numpy as np
import matplotlib.pyplot as plt

## MATRIZ DE VANDERMONDE
def Vandermonde(x):
    n= len(x)
    v = np.zeros((n,n))
    for i in range(0,n):
        for j in range(0,n):
            v[i,j]=x[i]**j
    return v
    
x=np.array([2,3,4,5,6])  
y=np.array([2,6,5,5,6]) 
V=Vandermonde(x)

#al evaluar el polinomio en un punto devuelve su imagen
def polVandermonde(x,y):
    v=Vandermonde(x)
    p= np.linalg.solve(v,y)
    P= p[::-1] ##invierte el orden del vector
    return P
p=polVandermonde(x,y)
plt.plot(x,y,'r*')
xp=np.linspace(min(x),max(x))
plt.plot(xp,np.polyval(p,xp),'b')
plt.title('Vandermonde')
plt.show()

### POLINOMIOS FUNDAMENTALES DE LAGRANGE
def lagrange_fund(x,k,z):
   prod=1
   for i in range(0,len(x)):
       if i != k:
           prod = prod*(z-x[i])/(x[k]-x[i])
   return prod


for i in range(0,len(x)):   
    plt.plot(xp,lagrange_fund(x,i,xp),'g')
    plt.plot(xp,0*xp,'k')
    plt.plot(x,lagrange_fund(x,i,x),'ro')
    plt.title('L'+str(i))
    plt.show()
    
### POLINOMIO INTERPOLADOR DE LAGRANGE
def polinomio_lagrange(x,y,z):
    suma=0
    for i in range(0,len(x)):
        suma=suma + y[i]*lagrange_fund(x,i,z)
    return suma



plt.plot(xp,polinomio_lagrange(x,y,xp),'b')
plt.plot(xp,0*xp,'k')
plt.plot(x,polinomio_lagrange(x,y,x),'ro')
plt.title('Polinomio de Lagrange')
plt.show()