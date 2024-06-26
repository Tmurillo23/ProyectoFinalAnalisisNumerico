import numpy as np

import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols("x")

def biseccion(f, a, b, tolerancia):
    #------------------
    #f: función a la que se van a hallar los ceros
    #a: límite inferior del intervalo
    #b límite superior del intervalo
    #tolerancia
    #------------------
    contador = 0

    if f(a)*f(b)<0:
        while abs(a-b)>tolerancia:
            contador+=1
            c= (a+b)/2

            if f(a)*f(c)<0:
                b=c
            else:
                a=c
        #return c, contador
        return c
    else:
        print("No cumple el teorema")

#posicion falsa


def pos_falsa(f, a, b, tolerancia):
    #------------------
    #f: función a la que se van a hallar los ceros
    #a: límite inferior del intervalo
    #b límite superior del intervalo
    #tolerancia
    #------------------
    contador =0

    c= a-((f(a)*(a-b))/(f(a)-f(b)))

    if f(a)*f(b)<0:
        #while abs(a-b)>tolerancia:
        while abs(f(c))>tolerancia:
            contador+=1
            #c= (a+b)/2
            c= a-((f(a)*(a-b))/(f(a)-f(b)))
            if f(a)*f(c)<0:
                b=c
            else:
                a=c
        #return c, contador
        return c
    else:
        print("No cumple el teorema")



def Newton(f, x0, tol):
    #--------------------
    #f: funcion
    #x0: semilla
    #tol: tolerancia
    contador=0
    df=sp.diff(f,x)
    NewT=x-f/df
    NewT=sp.lambdify(x,NewT)
    x1=NewT(x0)
    while (abs(x1-x0)>tol):
        x0=x1
        x1=NewT(x0)
        #print(x1)
        contador+=1
    #print("La raiz es", x1)
    #return x1,contador
    return x1

def secante(f, h0, h1,tolerancia):
    contador = 0
    while(abs(h0-h1)>tolerancia):
        h2 =h1-(f(h1)*(h0-h1))/(f(h0)-f(h1))
        h0=h1
        h1=h2
        contador+=1
    #return h1, contador
    return h1

def graficar_ceros(solution, function):
    x_values = np.linspace(solution - 1, solution + 1, 400)
    plt.plot(x_values, function(x_values), label=f'f(x)')
    plt.axhline(0, color='green')
    plt.plot(solution, function(solution), '*', label = 'raíz')
    plt.grid()
    plt.legend()
    plt.show()
