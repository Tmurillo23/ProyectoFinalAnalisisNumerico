from sympy import *
import numpy as np
import math
from math import factorial
import matplotlib.pyplot as plt
from sympy.utilities.lambdify import lambdify
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


"""
###

Grafica del polinomio vs la función


"""

def grafica_polinomio(f,x0,xp,n):
    x = symbols('x')
    w = np.linspace(x0, xp, 100)
    P = S_taylor(f, x0, n)

    custom_funcs = {'acos': np.arccos, 'cos': np.cos, 'sin': np.sin, 'log': np.log, 'exp': np.exp}

    P_lambdified = lambdify(x, P, modules=[custom_funcs, 'numpy'])
    F_lambdified = lambdify(x, f, modules=[custom_funcs, 'numpy'])

    plt.plot(w, P_lambdified(w), label=f'Polinomio de grado {n}')
    plt.plot(w, F_lambdified(w), 'o', label='Función')
    plt.legend()
    plt.show()
