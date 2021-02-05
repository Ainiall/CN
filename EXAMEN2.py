# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:58:29 2019

@author: UO270318
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate #integrales

############################ EXAMEN 2 #########################################

# Segundo parcial de laboratorio, Computacion Numerica 24/04/19

########################### EJERCICIO 1########################################

# f = funcion positiva
f= lambda x: np.exp(-x**2)
f2 = lambda x: np.exp(x**2)-6

# a y b = extremos del intervalo
a = -2
b = 2
# n numero de puntos
n=10000
# maxf = valor maximo de la funcion
maxf= 1 #exponencial elevada a numero negativo

#Integral exacta
I = integrate.quad(f,a,b)
I2 = integrate.quad(f2,a,b)
# Integral aproximada
   
def Montecarlo(f,a,b,n,maxf):
    p_aleatorios_intervalo = np.random.rand(n)*(b-a)+a
    p_aleatorios_eje= np.random.rand(n)*(maxf-0)
    cont_rojos=0
    cont_verdes=0
    
    xp= np.linspace(a,b)
    
    for i in range(0,n):
        if(p_aleatorios_intervalo[i] > p_aleatorios_eje[i]):
            cont_rojos = cont_rojos+1;
            plt.plot(p_aleatorios_intervalo[i],f(p_aleatorios_intervalo[i]),'ro')
        else:
            cont_verdes= cont_verdes +1;
            plt.plot(p_aleatorios_intervalo[i],f(p_aleatorios_intervalo[i]),'go')
    area= (cont_rojos/n)*((b-a)*maxf)
    
    plt.plot(xp,f(xp),'b')
    plt.plot(xp,0*xp,'k',label='Eje X')
    plt.show()   
    
    return area
    
print('El valor exacto de la integral es %f' % (I[0]))
print('El valor aproximado de la integral es %f' % Montecarlo(f,a,b,n,maxf))

########################### EJERCICIO 2 #######################################
#n = dimension de banda
# k numero de subdiagonales no nulas por debajo de la diagonal 
# v = vector de coeficientes


def mbanda(n,k,v):
    S1 = np.eye(n)
    for i in range(0,n):
        S1[i][i]= v[0] #diagonal
        #mientras haya k se rellena la siguiente subdiagonal
            
            
                
        
    return S1
        
    
    

# con mbanda se obtiene s1, se pretende resolver el sistema usando factorizacion lu
def LU(S1):
    U = np.zeros_like(S1)
    L = np.eye(len(S1)) #matriz identidad
    for i in range(0,len(S1)):
        for j in range(0,len(S1)):
            U[i][j]=S1[i][j]-np.dot(L[i,0:i],U[0:i,j])
            L[j][i]=S1[j][i]-np.dot(L[j,0:i],U[0:i,i])/U[i][i]
    return L,U


L,U=LU(S1)
print(L)
print(U)

# Una vez obtenidas las matrices triangulares se puede resolver la x e y usando sustituciones progresiva y regresiva

def sust_prog(L,b):
    x=np.zeros(len(b))
    for i in range(0,len(b)):
        if L[i][i]==0:
            print('El sistema no es compatible determinado')
            return None
        
        x[i]=(b[i]-np.dot(L[i,0:i],x[0:i]))/L[i,i]
    return x

def sust_regre(U,b):
    x=np.zeros(len(b))
    for i in range(len(b)-1,-1,-1): #3 i para hacer for inverso
        if U[i][i]==0:
            print('El sistema no es compatible determinado')
            return None
        
        x[i]=(b[i]-np.dot(U[i,i+1:len(b)],x[i+1:len(b)]))/U[i,i]
    return x

y=sust_prog(L,b)
x=sust_regre(U,y)
    
    