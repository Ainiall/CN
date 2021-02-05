# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 15:15:24 2019

@author: UO270318
"""

import numpy as np
import matplotlib.pyplot as plt

import sympy as sym
import scipy.optimize as op


#METODO DE LA SECANTE
f = lambda x :x**3 -10*x**2 +5
a=-15
b=15
dx=0.1
x0=0
x1=-1
tol=10**-12
maxiter=100
def secante(f,x0,x1,tol,maxiter):
    a=min(x0,x1)
    b=max(x0,x1)
    x=np.linspace(a,b)
    plt.plot(x,f(x),'b')
    plt.plot(x,0*x,'k') #eje x
    for i in range(0,maxiter):
        x2=x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
        error = abs(x2-x1)
        plt.plot([x1,x1],[0,f(x1)],'g')
        plt.plot([x0,x0],[0,f(x0)],'g')
        plt.plot([x1,x0],[f(x1),f(x0)],'r')
        if error < tol:
            plt.plot(x2,0,'ro')
            plt.show()
            return x2,i+1
        else:
            x0=x1
            x1=x2
    plt.show()
    print('No se ha obtenido una aproximacion.')
    return None, maxiter

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
            print('Existe cambio de signo en [%.1f, %.1f]' % (x0,x1))
            v= np.append(v,[x0,x1])
        else:
            break
    return v
   
 
v=CambiosSigno(f,-15,15,0.1)
n=int(len(v)/2)
M=np.zeros((3,2))
for i in range(0,n):
    #fila i esima de la matriz m
    M[i,:]=secante(f,v[2*i],v[2*i+1],tol,maxiter)
   
## PUNTO FIJO
#Se sustituye f(x)=0 por el equivalente g(x)=x, g(a)=a
# f(a)=0, de forma que x1= g(x0), x2= g(x1), x3=g(x2)
    
def puntoFijo(g,x0,tol,maxiter):
    for i in range(0,maxiter):
        x1=g(x0)
        error = abs(x1-x0)
        if error < tol:
            return x1,i+1
        else:
            x0=x1
    print('No se ha obtenido una aproximacion.')
    return None, maxiter
    
g= lambda x: np.exp(-x)

def aplicarPuntoFijo(g,a,b,dx,tol,maxiter):
    f= lambda x: g(x)-x
    v = CambiosSigno(f,a,b,dx)
    n= int(len(v)/2)
    M= np.zeros((n,2))
    for i in range(0,n):
        M[i,:]= puntoFijo(g,v[2*i],tol,maxiter)
    return M

g1= lambda x: 2*x-np.cos(x)
M=aplicarPuntoFijo(g1,-20,20,0.01,10**-12,500)


x=sym.Symbol('x',real=True)
f_sim=x**3+sym.log(x+7)*sym.cos(4*x)-1
df_sim=sym.diff(f_sim,x)
df2_sim=sym.diff(f_sim,x,2)

f=sym.lambdify([x],f_sim,'numpy')
df=sym.lambdify([x],df_sim,'numpy')
df2=sym.lambdify([x],df2_sim,'numpy')
xx=np.linspace(-2,2)
plt.show()
plt.plot(xx,df(xx))
plt.show()
plt.plot(xx,f(xx))
plt.plot(xx,0*xx,'k')

aprox=np.array([-1.5,-0.9,0,0.9])

r=np.zeros(len(aprox))
for i in range(0,len(aprox)):
    r[i]=op.newton(df,aprox[i],fprime=df2,tol=10**-12,maxiter=200)   
    plt.plot(r[i],f(r[i]),'ro')
plt.show()