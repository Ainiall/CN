# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:06:48 2019

@author: UO270318
"""
import numpy as np
import pprint

np.set_printoptions(precision = 2)   # solo dos decimales
np.set_printoptions(suppress = True) # no usar notación exponencial

################### SUSTITUCION PROGRESIVA #########################

#trabajamos con una matriz triangular inferior

L = np.array([[2, 0, 0], [1, 2, 0], [1, 1, 2]])
b = np.array([2, -1, 0])
################### EJERCICIO 1 #########################

def sust_prog(L,b):
    x=np.zeros(len(b))
    #for i in range(0,len(b)):
    #    sumatorio=0
    #    for j in range(0, i): #i-1
    #        sumatorio=sumatorio+L[i][j]*x[j]
    #    x[i]=(b[i]-sumatorio)/L[i][i]
    #return x

    ##### PARA MENOR COMPLEJIDAD #####
    for i in range(0,len(b)):
        if L[i][i]==0:
            print('El sistema no es compatible determinado')
            return None
        
        x[i]=(b[i]-np.dot(L[i,0:i],x[0:i]))/L[i,i]
    return x

print ('L:')
pprint.pprint(L)
print ('b:')
pprint.pprint(b)
print('Sustitucion progesiva:')
pprint.pprint(sust_prog(L,b))
print('----------------------------------------------------------------------')
print('COMPROBACION: L*x=b')
pprint.pprint(np.dot(L,sust_prog(L,b)))



n = 5
np.random.seed(1)           # para que los números aleatorios se repitan
L1 = np.random.random((n,n)) # genera una matriz aleatoria nxn
L1 = np.tril(L1)              # hacer cero los elementos por encima de la diagonal
b1 = np.random.random((n,))  # genera un vector aleatorio de dimensión n
print('\n')
print ('L1:')
pprint.pprint(L1)
print ('b1:')
pprint.pprint(b1)
print('Sustitucion progesiva:')
pprint.pprint(sust_prog(L1,b1))


################### SUSTITUCION REGRESIVA #########################

#trabajamos con una matriz triangular superior

U = np.array([[2, 1, 1], [0, 2, 1], [0, 0, 2]])
################### EJERCICIO 2 #########################
def sust_regre(U,b):
    x=np.zeros(len(b))
    for i in range(len(b)-1,-1,-1): #3 i para hacer for inverso
        if U[i][i]==0:
            print('El sistema no es compatible determinado')
            return None
        
        x[i]=(b[i]-np.dot(U[i,i+1:len(b)],x[i+1:len(b)]))/U[i,i]
    return x



n = 5
np.random.seed(2)           
U2 = np.random.random((n,n)) 
U2 = np.triu(U2)              # Haz cero los elementos bajo la diagonal
b2 = np.random.random((n,))  
print('\n')
print('U2')
pprint.pprint(U2)
print('b2')
pprint.pprint(b2)
print('Sustitucion regresiva:')
pprint.pprint(sust_regre(U2,b2))
print('----------------------------------------------------------------------')
print('COMPROBACION: U*x=b')
pprint.pprint(np.dot(U2,sust_regre(U2,b2)))


################### FACTORIZACION LU #########################

#A es un producto de matrices: una superior y otra inferior
A= np.array([[2, 1, 1], [1, 2, 2], [1, 1, 2]])
b3 = np.array([2, 4, 6])
################### EJERCICIO 3 #########################

def LU(A):
    U = np.zeros_like(A)
    L = np.eye(len(A)) #matriz identidad
    
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            U[i][j]=A[i][j]-np.dot(L[i,0:i],U[0:i,j])
            L[j][i]=A[j][i]-np.dot(L[j,0:i],U[0:i,i])/U[i][i]
    return L,U
        
print('\n')
L3,U3=LU(A)
print(L)
print(U)
y=sust_prog(L3,b3)
x=sust_regre(U,y)

