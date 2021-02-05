# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:00:04 2019

@author: UO270318
"""

import numpy as np
import matplotlib.pyplot as plt

f= lambda x: np.cos(x)-x
df= lambda x: -np.sin(x)-1

a=0
b=1
x= np.linspace(a,b)
z=np.linspace(1,b,200)
ox=0*x
dx=0.1
x0=0.6
tol= 10**-12
MaxIter=100

###################### STEFFERSON ########################
def Steffenson(f,x0,Maxiter,tol):
    for i in range(0, Maxiter):
        x=x0-(f(x0)**2/f(x0+f(x0))-f(x0)) #??
        error= abs(x-x0)
        if error < tol:
            return x, i+1
        else:
            x0=x
    print('No se ha obtenido una aproximacion.')    
    return None, Maxiter

#raices de una ecuacion
plt.plot(x,f(x)) #funcion
plt.plot(x,ox,'k--')
plt.show() 

##################### convergencia ######################
 
##################### NEWTON ############################

#bolzano
def busquedaIncremental(f,a,b,dx):
    x0=a
    while x0<b: 
        # a --dx--- x1
        x1=x0+dx
        if f(x0)*f(x1)<0:
            return x0,x1
        else:
            x0=x1
    return None, None

def CambiosSigno(f,a,b,dx):
    v = np.array([]) #vector vacio
    x1=a
    while x1<=b: 
        x0,x1= busquedaIncremental(f,x1,b,dx)
        if x0 != None:
            v= np.append(v,[x0,x1])
        else:
            break
    return v

#newton
def Newton(f,dx,x0,tol,maxiter):
    for i in range(0,maxiter):
        x1=x0-f(x0)/df(x0)
        error = abs(x1-x0)
        if error < tol:
            return x1,i+1
        else:
            x0=x1
    print('No se ha obtenido una aproximacion.')
    return None, maxiter

v= CambiosSigno(f,a,b,dx)
n = int(len(v)/2)
for i in range(0,n):
    print('Cambio de signo en [%.1f, %.1f]' % (v[2*i],v[2*i+1]))
    print(Newton(f,df,(v[2*i]+v[2*i+1])/2,10**-12,200))
    print(Steffenson(f,(v[2*i]+v[2*i+1])/2,MaxIter,10**-12))
    
 ##################### MINIMO ############################ 
#lagrange para obtener el polinomio con el que calcular el error
def lagrange_fund(x,k,z):
   prod=1
   for i in range(0,len(x)):
       if i != k:
           prod = prod*(z-x[i])/(x[k]-x[i])
   return prod

def polinomio_lagrange(x,y,z):
    suma=0
    for i in range(0,len(x)):
        suma=suma + y[i]*lagrange_fund(x,i,z)
    return suma

def Minimo(f,a,b,z,tol):
   error= np.linalg.norm(abs(f(z)-polinomio_lagrange(a,b,z)))
   if error < tol:
       return 
       
   


   
