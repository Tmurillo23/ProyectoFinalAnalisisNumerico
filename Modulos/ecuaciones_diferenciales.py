# Euler
import numpy as np

def Euler(f,a,b,co,h):
    #----------------
    #f: funcion
    #a: límite inferior
    #b: límite superior
    #h:
    #co: condicion inicial
    #---------------------
    n = int((b-a)/h)
    t = np.linspace(a,b,n+1)
    yeu = [co]
    for i in range(n):
        yeu.append(yeu[i]+h*f(t[i],yeu[i]))
    t = np.linspace(a,b,n+1)
    return t,yeu

def RungeKutta(f,a,b,h,c0):
    n = int((b-a)/h)
    yrk=[c0]
    t = np.linspace(a,b,n+1)
    for i in range(n):
        k1 = h*f(t[i],yrk[i])
        k2 = h*f(t[i]+h/2,yrk[i]+1/2*k1)
        k3 = h*f(t[i]+h/2, yrk[i]+1/2*k2)
        k4 = h*f(t[i+1],yrk[i]+k3)
        yn = yrk[i]+(k1+2*k2+2*k3+k4)/6
        yrk.append(yn)
    return yrk,t

