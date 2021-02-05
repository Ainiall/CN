# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:02:35 2019

@author: UO270318
"""

import numpy as np
import matplotlib.pyplot as plt

################### INTEGRALES #########################

f= lambda x: np.exp(x)
I_exacta=np.exp(3)-1
a=0
b=3
xp=np.linspace(a,b)

################### PUNTO MEDIO #########################

def punto_medio(f,a,b) :
      return f((a+b)/2)*(b-a)  
   
I_PM= punto_medio(f,a,b)
print('Valor exacto de la integral = ',I_exacta)
print('Valor numerico usando FPM = ',I_PM)
print('---------------------------------\n')

################### TRAPECIO #########################

def trapecio(f,a,b):
    return (f(a)+f(b))*(b-a)/2

I_T= trapecio(f,a,b)
print('Valor exacto de la integral = ',I_exacta)
print('Valor numerico usando FT = ',I_T)
print('---------------------------------\n')

################### SIMPSON #########################

def simpson(f,a,b):
    return ((b-a)/6)*(f(a)+4*f((a+b)/2)+f(b))

I_S= simpson(f,a,b)
print('Valor exacto de la integral = ',I_exacta)
print('Valor numerico usando FS = ',I_S)
print('---------------------------------\n')

################### PUNTO MEDIO COMPUESTO #########################

def punto_medio_comp(f,a,b,n):
    ##n es el numero de subintervalos que vamos a utilizar
    x=0
    h=(b-a)/n
    for i in range(0,n):
        ai=a+i*h #nodos 
        bi=a+(i+1)*h
        x= x+ punto_medio(f,ai,bi)
    return x
I_PMC= punto_medio_comp(f,a,b,5)
print('Valor exacto de la integral = ',I_exacta)
print('Valor numerico usando FPMC = ',I_PMC)
print('---------------------------------\n')

################### TRAPECIO COMPUESTO #########################

def trapecio_comp(f,a,b,n):
    ##n es el numero de subintervalos que vamos a utilizar
    x=0
    h=(b-a)/n
    for i in range(0,n):
        ai=a+i*h #nodo inicial
        bi=a+(i+1)*h #nodo final
        x= x+ trapecio(f,ai,bi)
    return x
I_TC= trapecio_comp(f,a,b,4)
print('Valor exacto de la integral = ',I_exacta)
print('Valor numerico usando FTC = ',I_TC)
print('---------------------------------\n')


################### SIMPSON COMPUESTO #########################

def simpson_comp(f,a,b,n):
    ##n es el numero de subintervalos que vamos a utilizar
    x=0
    h=(b-a)/n
    for i in range(0,n):
        ai=a+i*h #nodo inicial
        bi=a+(i+1)*h #nodo final
        x= x+ simpson(f,ai,bi)
    return x
I_SC= simpson_comp(f,a,b,4)
print('Valor exacto de la integral = ',I_exacta)
print('Valor numerico usando FSC = ',I_SC)
print('---------------------------------\n')


################### FORMULAS DE CUADRATURA GAUSSIANAS #########################

#importante trabajar con un intervalo simetrico
#al usar el intervalo -1,1 las impares no hace falta calcularlas

    # Gauss con 1 punto es igual que el punto medio
n=1
[x,w]=np.polynomial.legendre.leggauss(n)
print('w con un punto\n',w)
print('x con un punto\n',x)
    # Gauss con 2 puntos
n2 = 2 
[x, w] = np.polynomial.legendre.leggauss(n2)
print('w con dos puntos\n',w)
print('x con dos puntos\n',x)
    
def gauss(f,a,b,n):
    # n es el numero de puntos que se van a utilizar en la cuadratura
    suma=0
    [x,w]=np.polynomial.legendre.leggauss(n)
    y=((b-a)/2)*x+((a+b)/2)
    for i in range(0,len(y)):
       
        suma= suma+ f(y[i])*w[i]
    return ((b-a)/2)*suma


I_G= np.zeros(3)
for i in range(0,3):
    I_G[i]=gauss(f,a,b,i+1)
    print('Valor exacto de la integral = ',I_exacta)
    print('Valor numerico usando FG con '+str(i+1)+' puntos ',I_G[i])
    print('---------------------------------')
    
























