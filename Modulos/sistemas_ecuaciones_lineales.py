import numpy as np


def Eliminacion_Gaussiana(A, b):
    #------------------------
    #A: matriz A
    #b: matriz b
    #------------------------
    n = len(b)
    #se declara el arreglo de los valores de x
    x = np.zeros(n)

    for k in range(0, n - 1):  #llega hasta n-1 porque debajo del ultimo elemento no hay nada, no tiene que ser 0
        #print(k)
        for i in range(k + 1, n):
            #Se encuentra el factor (lambda)
            lam = A[i][k] / (A[k][k])
            #se actualiza la fila
            A[i][k:n] = A[i][k:n] - lam * A[k][k:n]
            b[i] = b[i] - lam * b[k]

    for k in range(n - 1, -1, -1):
        x[k] = (b[k] - np.dot(A[k][k + 1:n], x[k + 1:n])) / (A[k][k])

    #print('x=',x[0],'y=',x[1],'z=',x[2])
    return x


#Gauss - Seidel matricialmente
#import numpy as np


def Gauss_s(A, b, xo, tol):
    #------------------------------
    #A: la matriz A. Debe ingresarse como un arreglo de numpy np.array([],[],[])
    #b: vector b. También debe ser un arreglo de numpy np.array([])
    #xo: el vector semilla (suele ser el vectr nulo)
    #tol: tolerancia
    #-------------------------------

    cont = 0
    error = []  #lista que guarda los errores

    D = np.diag(np.diag(A))
    L = D - np.tril(A)
    U = D - np.triu(A)

    Tg = np.dot(np.linalg.inv(D - L), U)  #(D-L)^-1 U
    Cg = np.dot(np.linalg.inv(D - L), b)  #(D-L)^-1 b

    lam, vec = np.linalg.eig(Tg)  #calcula los valores propios
    radio = max(abs(lam))  #calcula el radio espectral

    x_it = []

    if radio < 1:
        x1 = np.dot(Tg, xo) + Cg
        x_it.append(x1)
        cont += 1
        while (max(np.abs((x1 - xo))) > tol):
            #print(f'iteración: {cont}\n vector: {x1}\n error: {max(abs(x1 - xo))}')
            error.append(max(abs(x1 - xo)))
            xo = x1
            x1 = np.dot(Tg, xo) + Cg
            x_it.append(x1)  #guarda el vector de las x en la iteracion i
            cont += 1
        #print(f'iteración: {cont}\n vector: {x1}\n error: {max(abs(x1 - xo))}')
        return x_it
    else:
        return f'El sistema iterativo no converge a la solución única del sistema'


def Gauss_s_sumas(A, b, xo, tol):
    n = len(b)
    error = []  #lista que guarda los errores en cada iteracion

    while True:
        for i in range(n):
            xo[i] = (b[i] - (np.dot(A[i, :], xo) - A[i][i] * xo[i])) / A[i][i]
        r = b - np.dot(A, xo)
        error.append(abs(r[0]))
        if (np.abs(r[0]) <= tol):
            break

    return xo


'''        
#Gauss - Seidel con sumas (este no funciona, es muy inestable
def Gauss_s_sumas(A,b,xo,tol,M):
    #------------------------------
    #A: la matriz A. Debe ingresarse como un arreglo de numpy np.array([],[],[])
    #b: vector b. También debe ser un arreglo de numpy np.array([])
    #xo: el vector semilla (suele ser el vector nulo)
    #tol: tolerancia
    #M: número máximo de iteraciones
    #-------------------------------
    

    n=len(b)
    x = xo.copy()
    x1 = np.zeros(n)
    
    cont = 0
    norm = 2


    while(norm>tol) and (cont<M):
        for i in range(n):
            aux = 0
            for j in range(n):
                if(i!=j):
                    aux = aux-A[i,j]*xo[j]
            x1[i]=(b[i]+aux)/A[i,i]
            #print(x1)
            #x = xo
            norm=np.max(np.abs(x1-x))
            x = xo.copy()
            #print(norm)
            xo=x1
            cont+=1
    print(cont)
    #print(x1)
    return x1
'''
