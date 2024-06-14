# Proyecto Final Análisis Numérico 2024-1

Trabajo realizado por: Tatiana Murillo Mosquera y Valentina Miranda Garcés

## Como ingresar los datos

- **Series de Taylor:** Ingresar la función como una función de sympy, ejemplot: <<sp.exp(x)>>
- **Ceros de Funciones:** Ingresar la función como una función de sympy si se utiliza el método de Newton, de lo contrario 
use funciones de numpy
- **Sistemas de Ecuaciones Lineales:** Ingresar las matrices como listas, no como arrays de numpy u otro tipo de estructuras de datos
- **Interpolación y ajuste:** Ingresar los datos como listas, no como arrays de numpy u otro tipo de eestructuras de datos
- **Ecuaciones diferenciales:** Ingresar las funciones como funciones de numpy. El número de condiciones iniciales deben de ser mayor a 1

## Estructura del programa

### Carpeta Modulos
Contiene las rutinas necesarias para la ejecución del código:

- **Ceros.py:** Contiene las rutinas para encontrar ceros de funciones por los métodos de: Bisección, Secante, Falsa Posición y Newton.
- **ecuaciones_diferenciales.py:** Contiene las rutinas de Euler y Rugekutta, ambas de orden 4. Además, contiene una función para graficar la solución de la ecuación.
- **interpolacion_ajuste.py:** Contiene las rutinas para hacer interpolación por los métodos Polinomial simple y Langrange; y ajuste por medio de mínimos cuadrados.
- **serie:** Contiene la rutina para encontrar el polinomio de Taylor de una función.
- **sistemas_ecuaciones_lineales** Contiene la rutina para encontrar la solución de un sistema de ecuaciones lineales por los métodos de: Eliminación Gaussiana, Pivoteo y Gauss Seidel (matricial).
## Archivo GUI

Es el archivo donde se realizó toda la lógica de la interfaz gráfica.


## Requerimientos del programa

Para poder ejecutar este programa el computador debe tener instalado: 
- Sympy
- Numpy
- Matplotlib
En caso de que no venga por defecto en su instalación de python, también se debe instalar tkinter.


## Como ejecutar el programa

- Cree una carpeta y dirijase a ella desde la terminal
- Clone el repositorio de Github
- En su consola ejecute el comando: <<git clone (link del repositorio de github) >>
- Para ejecutar la interfaz gráfica, ejecute el comando: `python ./ProyectoFinalAnalisisNumerico/GUI.py `