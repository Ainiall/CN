# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:05:23 2019

@author: uo270318
"""

# TEOREMA DE BOLZANO -> METODO DE LA BISECCION

import numpy as np
import matplotlib.pyplot as plt



#Calcular de forma aproximada las raices de la ecuacion usando una grafica
x =np.linspace(-1,2)
g = lambda x :x**3 -2*x**2 +1
ox = 0*x
plt.plot(x,g(x))
plt.plot(x,ox,'k--')
plt.show()

#Busca las raices de la funcion f entre el 
# intervalo a,b con dx longitud de intervalos
f = lambda x :x**3 -10*x**2 +5
a=-15
b=15
dx=0.1
x0=0
x1=0

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


#print('Existe una raiz en[%.1f, %.1f]' % (x0,x1))

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
   
def Biseccion(f,a,b,tol,maxiter):   
    if f(a)*f(b)>0:
        print('La funcion no cambia de signo')
        return None;0
    elif f(a)==0:
        print('Raiz exacta')
        return a,0
    elif f(b)==0:
        print('Raiz exacta')
        return b,0
    elif abs(b-a) < tol:
        print('Raiz aproximada')
        return a,0
        
    for i in range(0,maxiter): #de 0 a maxiter-1
         c=(a+b)/2
         error = abs(c-a)
         if error < tol or f(c)==0:
             print('Raiz aproximada')
             return c,i+1 
         elif f(a)*f(c) <0:
             b=c
         elif f(a)*f(c)>0:
             a=c
    print('No se ha encontrado la raiz en '+str(maxiter)+' iteraciones')
    return None,maxiter

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
df= lambda x: 3*x**2-20*x
#imprimir usando los elementos del vector v
n = int(len(v)/2)
for i in range(0,n):
    print('Existe cambio de signo en [%.1f, %.1f]' % (v[2*i],v[2*i+1]))
    print(Biseccion(f,v[2*i],v[2*i+1],10**-12,200))
    #el numero de iteraciones se guarda en la pos 1 del array
    print(Newton(f,df,(v[2*i]+v[2*i+1])/2,10**-12,200))
   

