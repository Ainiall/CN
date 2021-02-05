# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:10:11 2019

@author: UO270318
"""

################### DERIVADAS #########################

import numpy as np
import matplotlib.pyplot as plt

a=0
b=1
h=0.1
h2=0.01
f= lambda x: np.exp(x)
df= lambda x: np.exp(x)
xp=np.arange(a,b+h,h)
num_puntos=1/h +1
### DERIVADA PROGRESIVA ###
def df_p(f,x0,h):
    return (f(x0+h)-f(x0))/h

### DERIVADA REGRESIVA ###
def df_r(f,x0,h):
    return (f(x0)-f(x0-h))/h

### DERIVADA NUMERICA CENTRADA ###
def df_c(f,x0,h):
    return ((df_p(f,x0,h)+df_r(f,x0,h))/2)

###################### EJERCICIO 1 #######################

### CON H=01 ###
plt.plot(xp[1:-1],df(xp[1:-1]),label='derivada exacta') #evaluar de 0.1 a 0.9
plt.plot(xp[1:-1],df_p(f,xp[1:-1],h),label='derivada progresiva')
plt.plot(xp[1:-1],df_r(f,xp[1:-1],h),label='derivada regresiva')
plt.plot(xp[1:-1],df_c(f,xp[1:-1],h),label='derivada centrada')
plt.legend()
plt.title('Derivada con h=0.1')
plt.show()

errorP=abs(df(xp[1:-1])-df_p(f,xp[1:-1],h))
errorR=abs(df(xp[1:-1])-df_r(f,xp[1:-1],h))
errorC=abs(df(xp[1:-1])-df_c(f,xp[1:-1],h))


plt.plot(xp[1:-1],errorP,label='derivada progresiva')
plt.plot(xp[1:-1],errorR,label='derivada regresiva')
plt.plot(xp[1:-1],errorC,label='derivada centrada')
plt.legend()
plt.title('Error con h=0.1')
plt.show()

### CON H=0.01 ###
plt.plot(xp[1:-1],df(xp[1:-1]),label='derivada exacta') #evaluar de 0.1 a 0.9
plt.plot(xp[1:-1],df_p(f,xp[1:-1],h2),label='derivada progresiva')
plt.plot(xp[1:-1],df_r(f,xp[1:-1],h2),label='derivada regresiva')
plt.plot(xp[1:-1],df_c(f,xp[1:-1],h2),label='derivada centrada')
plt.legend()
plt.title('Derivada con h=0.01')
plt.show()

errorP2=abs(df(xp[1:-1])-df_p(f,xp[1:-1],h2))
errorR2=abs(df(xp[1:-1])-df_r(f,xp[1:-1],h2))
errorC2=abs(df(xp[1:-1])-df_c(f,xp[1:-1],h2))

plt.plot(xp[1:-1],errorP2,label='derivada progresiva')
plt.plot(xp[1:-1],errorR2,label='derivada regresiva')
plt.plot(xp[1:-1],errorC2,label='derivada centrada')
plt.legend()
plt.title('Error con h=0.01')
plt.show()

### ERROR RELATIVO ###
errorRelP= np.linalg.norm(df(xp[1:-1])-df_p(f,xp[1:-1],h))/np.linalg.norm(df(xp[1:-1]))
errorRelR= np.linalg.norm(df(xp[1:-1])-df_r(f,xp[1:-1],h))/np.linalg.norm(df(xp[1:-1]))
errorRelC= np.linalg.norm(df(xp[1:-1])-df_c(f,xp[1:-1],h))/np.linalg.norm(df(xp[1:-1]))

print('relativa progresiva',errorRelP)
print('relativa regresiva',errorRelR)
print('relativa centrada',errorRelC)


###################### EJERCICIO 2 #######################

def dfOrden2_p(f,x0,h):
    return (-3*f(x0)+4*f(x0+h)-f(x0+2*h))/(2*h)

def dfOrden2_r(f,x2,h):
    return (f(x2-2*h)-4*f(x2-h)+3*f(x2))/(2*h)

f= lambda x: 1/x
df= lambda x: -1/x**2
a=0.2
b=1.2
h=0.01
xp=np.arange(a,b+h,h)
dfa=np.zeros(len(xp))
dfa[0]=df_p(f,xp[0],h)
dfa[-1]=df_r(f,xp[-1],h)
dfa[1:-1]=df_c(f,xp[1:-1],h)
plt.plot(xp,dfa,label='derivada aproximada')
plt.legend()
plt.show()

dfb=np.zeros(len(xp))
dfb[0]=dfOrden2_p(f,xp[0],h)
dfb[-1]=dfOrden2_r(f,xp[-1],h)
dfb[1:-1]=df_c(f,xp[1:-1],h)
plt.plot(xp,dfa,label='derivada aproximada')
plt.legend()
plt.show()

Ea= np.linalg.norm(df(xp)-dfa)/np.linalg.norm(df(xp))
Eb= np.linalg.norm(df(xp)-dfb)/np.linalg.norm(df(xp))

print('relativa global con procedimiento a',Ea)
print('relativa',Eb)

###################### EJERCICIO 3 #######################
def D2f(f,x1,h):
    return (f(x1-h)-2*f(x1)+f(x1+h))/(h**2)


f=lambda x: np.sin(2*np.pi*x)
d2f=lambda x: -4*np.pi**2*np.sin(2*np.pi*x)
a=0;b=1;h=0.01
xp=np.arange(a,b+h,h)
d2_f=D2f(f,xp[1:-1],h)
plt.plot(xp[1:-1],d2f(xp[1:-1]),label='derivada 2exacta')
plt.plot(xp[1:-1],d2_f,label='derivada 2 numerica')
plt.legend()
plt.show()
Ec= np.linalg.norm(d2f(xp[1:-1])-d2_f)/np.linalg.norm(d2f(xp[1:-1]))
print('Error relativo global de D2f es',Ec)
