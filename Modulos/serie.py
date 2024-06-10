from sympy import *
import numpy as np
from math import factorial
#--------------------------
x = symbols('x')
#--------------


"""
######################

SERIE DE TAYLOR
Datos de entrada:
f:funcion
x0 = punto entorno al cual se construye el polinomio
n=grado del polinomio

######################

"""


def S_taylor(f,x0,n):
    p = 0 #acumulador del polinomio
    
    for k in range(n+1):
        df = diff(f,x,k)
        dfx0 = df.subs(x,x0)
        p += dfx0*(x-x0)**k/factorial(k)
    return p
        
    
"""
###

Calculo de la cota de la derivada

###
"""
    
def cota_t(f,x0,xp,n):
    m = min(x0,xp)
    M = max(x0,xp)
    u = np.linspace(m,M,500)
    df = diff(f,x,n+1)
    df = lambdify(x,df)
    Mc = np.max(np.abs(df(u)))
    return Mc*np.abs((xp-x0)**(n+1)/factorial(n+1))


