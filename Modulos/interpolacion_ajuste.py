# Polinomial simple

import sympy as sp
import numpy as np

def Gauss_s(A,b,xo,tol):
    
    cont = 0
    
    D= np.diag(np.diag(A))
    L=D-np.tril(A)
    U=D-np.triu(A)
    Tg=np.dot(np.linalg.inv(D-L),U)
    Cg=np.dot(np.linalg.inv(D-L),b)
    lam,vec = np.linalg.eig(Tg) #calcula los valores propios
    radio = max(abs(lam)) #calcula el radio espectral
    if radio<1:
        x1=np.dot(Tg, xo)+Cg
        cont+=1
        while(max(np.abs((x1-xo)))>tol):
            #print(f'iteración: {cont}\n vector: {x1}\n error: {max(abs(x1 - xo))}')
            xo=x1
            x1=np.dot(Tg,xo)+Cg
            cont+=1
        #print(f'iteración: {cont}\n vector: {x1}\n error: {max(abs(x1 - xo))}')
        return x1
    else:
        print('El sistema iterativo no converge a la solución única del sistema')

#devuelve un arreglo con los coeficientes del polinomio
def Pol_simple(x_data, y_data):
    #---------------------
    #x_data: la variable independiente
    #y_data: la variable dependiente
    #--------------------
    n=len(x_data)
    xo=np.zeros(n)
    M_p=np.zeros([n,n])
    for i in range(n):
        M_p[i,0]=1
        for j in range(1,n):
            M_p[i,j]=M_p[i,j-1]*x_data[i]
    #a_i=Gauss_s(M_p,y_data,xo,1e-6)
    a_i = np.linalg.solve(M_p, y_data)
    return a_i


#-----------------------
#Lo que se le debe pasar a la función Polu luego de calcular los coeficientes

#a_i=Pol_simple(Px,Ty) 
#ux=np.linspace(min(Px),max(Px),1000)
#--------------------------


#construye el polinomio con los coeficientes hallados
def Poly(a_i,ux):
    P=0
    for i in range(len(a_i)):
        P=P+a_i[i]*ux**i
        
    return P




x = sp.symbols('x')

def Pol_lagrange(x_d, y_d):
    #se calcula la suma y la productoria
    n = len(x_d)
    S = 0 #contador de la suma
    for i in range(n):
        pr = 1 #contador de la productoria
        for j in range(n):
            if (j!=i):
                pr = pr*((x-x_d[j])/(x_d[i]-x_d[j]))
        S = S + pr*y_d[i]
        #print(S)
    return(S.expand()) #retorna el polinomio simplificado para comparar con polinomial simple



#minimos cuadrados
def min_c(xd, yd):
    #--------------------------
    #xd: datos independientes
    #yd: datos dependientes
    #--------------------------
    n = len(xd)
    sx = sum(xd)
    sf = sum(yd)
    sx2 =sum(xd**2)
    sfx = sum(xd*yd)
    
    ao = (sf*sx2-sx*sfx)/(n*sx2-(sx)**2) #intercepto de la recta
    a1 = (n*sfx-sf*sx)/(n*sx2-(sx)**2) #pendiente de la recta
    
    return ao,a1

#grafica
import matplotlib.pyplot as plt
def transformaciones(x_a,y_p, xlabel, ylabel):
    plt.figure(figsize =(9,9), dpi = 100)

    plt.subplot(331)
    plt.plot(x_a,y_p,'pb', label= "Datos observados")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()

    plt.subplot(332)
    plt.plot(x_a**2,y_p,'pr', label= "$x^2")
    plt.xlabel(xlabel)
    plt.ylabel("latidos")
    plt.legend()

    plt.subplot(333)
    plt.plot(x_a**3,y_p,'dr', label= "$x^3")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()

    plt.subplot(334)
    plt.plot(x_a,np.sqrt(y_p),'dr', label= "$sqrt(y)")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()

    plt.subplot(335)
    plt.plot(x_a,1./np.sqrt(y_p),'dr', label= "1/$sqrt(y)")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()

    plt.subplot(336)
    plt.plot(np.log(x_a),y_p,'dr', label= "$log(x)")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()

    plt.subplot(337)
    plt.plot(np.log(x_a),np.log(y_p),'dr', label= "$log(x), $log(y)")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()

    plt.subplot(338)
    plt.plot(x_a,np.log(y_p),'dr', label= "$log(y)")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()


    plt.subplot(339)
    plt.plot(x_a,y_p**2,'dr', label= "$y^2")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()