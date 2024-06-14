import ast
import tkinter as tk
import numpy as np
import sympy as sp
from tkinter import ttk
from tkinter import messagebox
import Modulos
from Modulos import serie as sr
from Modulos import interpolacion_ajuste as i_a
from Modulos import sistemas_ecuaciones_lineales as se
import Modulos.Ceros
from Modulos import ecuaciones_diferenciales as ed


# Funciones para abrir las ventanas de cada funcionalidad
def open_taylor_window():
    window = tk.Toplevel(root)
    window.title("Serie de Taylor")
    label = tk.Label(window, text="La función en x_0 ")
    label.pack(pady=10)
    entry_function = tk.Entry(window, width=50)
    entry_function.pack(pady=10)
    label_x0 = tk.Label(window, text="X_0")
    label_x0.pack(pady=10)
    entry_x0 = tk.Entry(window, width=50)
    entry_x0.pack(pady=10)
    label_degree = tk.Label(window, text="Grado del polinomio:")
    label_degree.pack(pady=10)
    entry_degree = tk.Entry(window, width=50)
    entry_degree.pack(pady=10)
    save_button = tk.Button(window, text="Calcular",
                            command=lambda: save_taylor(entry_function.get(), entry_x0.get(), entry_degree.get()))
    save_button.pack(pady=10)


def open_zeros_window():
    window = tk.Toplevel(root)
    window.title("Ceros de Funciones")

    label = tk.Label(window, text="Función:")
    label.pack(pady=10)
    entry_function = tk.Entry(window, width=50)
    entry_function.pack(pady=10)

    label_interval = tk.Label(window,
                              text="Intervalo (si el método es diferente de Newton, ingréselo como una lista [a,b])\n o dato inicial (si el método es Newton, ingréselo como un valor normal):")
    label_interval.pack(pady=10)
    entry_interval = tk.Entry(window, width=50)
    entry_interval.pack(pady=10)

    label_accuracy = tk.Label(window, text="Exactitud:")
    label_accuracy.pack(pady=10)
    entry_accuracy = tk.Entry(window, width=50)
    entry_accuracy.pack(pady=10)

    label_method = tk.Label(window, text="Método:")
    label_method.pack(pady=10)
    methods = ["Bisección", "Newton", "Falsa Posición", "Secante"]
    method_combobox = ttk.Combobox(window, values=methods)
    method_combobox.pack(pady=10)

    save_button = tk.Button(window, text="Calcular",
                            command=lambda: save_zeros(entry_function.get(), entry_interval.get(), entry_accuracy.get(),
                                                       method_combobox.get()))
    save_button.pack(pady=10)


def open_linear_systems_window():
    window = tk.Toplevel(root)
    window.title("Sistemas de Ecuaciones Lineales")

    label = tk.Label(window, text="Ingrese el sistema de ecuaciones lineales:")
    label.pack(pady=10)
    entry_system = tk.Entry(window, width=50)
    entry_system.pack(pady=10)

    label_b = tk.Label(window, text="Ingrese la matriz b:")
    label_b.pack(pady=10)
    entry_b = tk.Entry(window, width=50)
    entry_b.pack(pady=10)

    label_method = tk.Label(window, text="Ingrese el método:")
    label_method.pack(pady=10)
    methods = ["Eliminación Gaussiana", "Pivoteo", "Gauss Seidel"]
    global method_combobox
    method_combobox = ttk.Combobox(window, values=methods)
    method_combobox.pack(pady=10)
    method_combobox.bind("<<ComboboxSelected>>", on_method_change)

    global label_x0, entry_x0, label_tol, entry_tol

    label_x0 = tk.Label(window, text="Ingrese el vector x0:")
    entry_x0 = tk.Entry(window, width=50)

    label_tol = tk.Label(window, text="Ingrese la tolerancia:")
    entry_tol = tk.Entry(window, width=50)

    save_button = tk.Button(window, text="Resolver", command=lambda: save_linear_systems(entry_system.get(), method_combobox.get(), entry_b.get(), entry_x0.get(), entry_tol.get()))
    save_button.pack(pady=10, side=tk.BOTTOM)


def show_solution_window(solution):
    solution_window = tk.Toplevel(root)
    solution_window.title("Solución")

    label_solution = tk.Label(solution_window, text="Solución:")
    label_solution.pack(pady=10)

    solution_str = ', '.join([str(s) for s in solution])
    entry_solution = tk.Entry(solution_window, width=50)
    entry_solution.insert(0, solution_str)
    entry_solution.config(state='readonly')
    entry_solution.pack(pady=10)

def show_solution_roots(solution):
    solution_roots_window = tk.Toplevel(root)
    solution_roots_window.title("Solución")

    label_solution_roots = tk.Label(solution_roots_window, text=f"Solución:{solution}")
    label_solution_roots.pack(pady=10)

def show_solution_int_ajuste(polinomio, aproximacion):
    solution_int_ajuste_window = tk.Toplevel(root)
    solution_int_ajuste_window.title("Solución")

    label_solution_int_ajuste = tk.Label(solution_int_ajuste_window, 
    text=f"Solución:{polinomio}")
    label_solution_int_ajuste.config(text= f"Polinomio: {polinomio}")
    label_solution_int_ajuste.pack(pady=10)

    label_approx_int_ajuste = tk.Label(solution_int_ajuste_window, 
    text=f"La aproximación es y = {aproximacion}")
    label_approx_int_ajuste.pack(pady=10)


def show_solution_min_c(intercept, slope_min_c, aproximacion):
    solution_min_c_window = tk.Toplevel(root)
    solution_min_c_window.title("Solución")

    label_solution_min_c = tk.Label(solution_min_c_window, 
    text=f"Solución:{intercept}+ ({slope_min_c})x")
    label_solution_min_c.pack(pady=10)

    label_approx_min_c = tk.Label(solution_min_c_window, 
    text=f"La aproximación es y = {aproximacion}")
    label_approx_min_c.pack(pady=10)


def on_method_change(event):
    selected_method = method_combobox.get()
    if selected_method == "Gauss Seidel":
        label_x0.pack(pady=10)
        entry_x0.pack(pady=10)
        label_tol.pack(pady=10)
        entry_tol.pack(pady=10)
    else:
        label_x0.pack_forget()
        entry_x0.pack_forget()
        label_tol.pack_forget()
        entry_tol.pack_forget()

def open_interpolation_window():
    window = tk.Toplevel(root)
    window.title("Interpolación y ajuste")

    label_datos_x = tk.Label(window, text="Datos (x)\n Por favor ingréselos como una lista [x1, x2, ...]")
    label_datos_x.pack(pady=10)
    entry_datos_x = tk.Entry(window, width=50)
    entry_datos_x.pack(pady=10)

    label_datos_y = tk.Label(window, text="Datos (y)\n Por favor ingréselos como una lista [x1, x2, ...]")
    label_datos_y.pack(pady=10)
    entry_datos_y = tk.Entry(window, width=50)
    entry_datos_y.pack(pady=10)

    label_approx = tk.Label(window, text="Dato que se desea aproximar:")
    label_approx.pack(pady=10)
    entry_approx = tk.Entry(window, width=50)
    entry_approx.pack(pady=10)

    label_method = tk.Label(window, text="Método:")
    label_method.pack(pady=10)
    methods = ["Polinomial simple", "Lagrange", "Mínimos cuadrados"]
    method_combobox = ttk.Combobox(window, values=methods)
    method_combobox.pack(pady=10)

    save_button = tk.Button(window, text="Calcular",
                            command=lambda: save_interpolation(entry_datos_x.get(), entry_datos_y.get(), entry_approx.get(), method_combobox.get()))
    save_button.pack(pady=10)

def on_num_eq_change(event):
    try:
        num_eq = int(entry_num_eq.get())
        if num_eq <= 0:
            raise ValueError("El número de ecuaciones debe ser un entero positivo.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return

    for widget in frame_eq.winfo_children():
        widget.destroy()
    for i in range(num_eq):
        label_eq = tk.Label(frame_eq, text=f"Ecuación {i+1}:")
        label_eq.grid(row=i, column=0, pady=5)
        entry_eq = tk.Entry(frame_eq, width=50)
        entry_eq.grid(row=i, column=1, pady=5)
        eq_entries.append(entry_eq)

def on_num_cond_change(event):
    try:
        num_cond = int(entry_num_cond.get())
        if num_cond <= 0:
            raise ValueError("El número de condiciones iniciales debe ser un entero positivo.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return

    for widget in frame_cond.winfo_children():
        widget.destroy()
    for i in range(num_cond):
        label_cond = tk.Label(frame_cond, text=f"Condición {i+1}:")
        label_cond.grid(row=i, column=0, pady=5)
        entry_cond = tk.Entry(frame_cond, width=50)
        entry_cond.grid(row=i, column=1, pady=5)
        cond_entries.append(entry_cond)

def open_differential_eq_window():
    window = tk.Toplevel(root)
    window.title("Ecuaciones Diferenciales")

    global entry_num_eq, frame_eq, eq_entries, entry_num_cond, frame_cond, cond_entries
    eq_entries = []
    cond_entries = []

    label_num_eq = tk.Label(window, text="Número de ecuaciones diferenciales:")
    label_num_eq.pack(pady=10)
    entry_num_eq = tk.Entry(window, width=10)
    entry_num_eq.pack(pady=10)
    entry_num_eq.bind("<Return>", on_num_eq_change)

    frame_eq = tk.Frame(window)
    frame_eq.pack(pady=10)

    label_num_cond = tk.Label(window, text="Número de condiciones iniciales:")
    label_num_cond.pack(pady=10)
    entry_num_cond = tk.Entry(window, width=10)
    entry_num_cond.pack(pady=10)
    entry_num_cond.bind("<Return>", on_num_cond_change)

    frame_cond = tk.Frame(window)
    frame_cond.pack(pady=10)

    # Labels and entries for a, b, h
    label_a = tk.Label(window, text="a:")
    label_a.pack(pady=5)
    entry_a = tk.Entry(window, width=10)
    entry_a.pack(pady=5)

    label_b = tk.Label(window, text="b:")
    label_b.pack(pady=5)
    entry_b = tk.Entry(window, width=10)
    entry_b.pack(pady=5)

    label_h = tk.Label(window, text="h:")
    label_h.pack(pady=5)
    entry_h = tk.Entry(window, width=10)
    entry_h.pack(pady=5)

    label_method = tk.Label(window, text="Método:")
    label_method.pack(pady=10)
    methods = ["Euler de orden 4", "Runge Kutta de orden 4"]
    method_combobox = ttk.Combobox(window, values=methods)
    method_combobox.pack(pady=10)

    save_button = tk.Button(window, text="Resolver",
                            command=lambda: save_differential_eq(eq_entries, cond_entries,
                                                                  method_combobox.get(),
                                                                  entry_a.get(), entry_b.get(), entry_h.get()))
    save_button.pack(pady=10)

def get_sympy_f(function):
    try:
        f_sympy = sp.sympify(function, locals={'x':x, 'sp':sp})
        if not isinstance(f_sympy, sp.core.basic.Basic):
            raise InvalidSPFunctionError("La expresión no es un tipo SymPy válido.")
        return f_sympy
    except Exception as e:
        raise InvalidSPFunctionError(f"Función inválida. Por favor ingrese una función matemática válida. Error: {str(e)}")


# Funciones para guardar los datos ingresados
def save_taylor(function, x_0, degree):
    try:
        float(x_0)
        int(degree)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos para x_0 y el grado.")
        return

    try:
        function = get_sympy_f(function)
        poli = sr.S_taylor(function, float(x_0), int(degree))
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error al calcular la serie de Taylor: {e}")
        return

    result_window = tk.Toplevel(root)
    result_window.title("Resultado de la Serie de Taylor")
    result_label = tk.Label(result_window, text=f"Función: {poli}\nGrado: {degree}")
    result_label.pack(pady=10)
    grafica = sr.grafica_polinomio(function, float(x_0), 1, int(degree))


class InvalidIntervalError(Exception):
    pass

# Función para verificar que el intervalo ingresado o el valor inicial son correctos y retornarlos
def get_interval(entry_interval, method):
    try:
        interval = eval(entry_interval, {"np":np})
    except:
        raise InvalidIntervalError("Input inválido")

    if method != "Newton":
        if not(isinstance(interval, list) and len(interval) == 2):
            raise InvalidIntervalError("Por favor ingrese una lista válida [a,b]")
        return interval
    else:
        if not (isinstance(interval,(int, float))):
            raise InvalidIntervalError("Por favor ingrese un número válido (entero o decimal)")
        return interval
    

class TeoremaCerosError(Exception):
    pass

def verificar_teorema(f, a, b):
    if f(a)*f(b)>0:
        raise TeoremaCerosError("El teorema no se cumple\nIngrese un intervalo válido")
    
class InvalidNumberError(Exception):
    pass

class InvalidSPFunctionError(Exception):
    pass
    
def get_accuracy(accuracy):
    try:
        return float(accuracy)
    except ValueError:
        raise InvalidNumberError("Toleracia inválida. Por favor ingrese un número válido (por ejemplo, 0.001 o 1e-6).")

x = sp.symbols('x')    


   

def save_zeros(function, interval, accuracy, method):
    try:
        ret_interval = get_interval(interval, method)
        tol = get_accuracy(accuracy)
        match method:
            case "Bisección" | "Falsa Posición"| "Secante":
                a = ret_interval[0]
                b = ret_interval[1]
                f = eval(f"lambda x: {function}", {"np": np})
                try:
                    verificar_teorema(f, a, b)
                    
                    match method:
                        case "Bisección":
                            sol = Modulos.Ceros.biseccion(f, a, b,tol)
                            show_solution_roots(sol)
                        case "Falsa Posición":
                            sol = Modulos.Ceros.pos_falsa(f, a, b,tol)
                            show_solution_roots(sol)
                        case "Secante":
                            sol = Modulos.Ceros.secante(f, a, b,tol)
                            show_solution_roots(sol)
                except TeoremaCerosError as e:
                    messagebox.showerror("Error", str(e))
            case "Newton":
                try:
                    f_sympy = get_sympy_f(function)
                    sol = Modulos.Ceros.Newton(f_sympy,ret_interval, tol)
                    show_solution_roots(sol)
                except InvalidSPFunctionError as e:
                    messagebox.showerror("Error", str(e))
            case _:
                messagebox.showerror("Error", "Seleccione un método válido.")
    except (InvalidIntervalError,InvalidNumberError) as e:
        messagebox.showerror("Error", str(e))
        


def save_linear_systems(system, method, b, x0, tol):
    try:
        A = np.array(ast.literal_eval(system))
        B = np.array(ast.literal_eval(b))
    except (ValueError, SyntaxError):
        messagebox.showerror("Error", "Por favor ingrese una matriz válida para el sistema de ecuaciones o b.")
        return

    if method == "Gauss Seidel":
        try:
            X0 = np.array(ast.literal_eval(x0))
            tol = float(tol)
        except (ValueError, SyntaxError):
            messagebox.showerror("Error", "Por favor ingrese un vector x0 válido y un valor numérico válido para la tolerancia.")
            return

    match method:
        case "Eliminación Gaussiana":
            try:
                solution = se.Eliminacion_Gaussiana(A, B)
                show_solution_window(solution)
            except Exception as e:
                messagebox.showerror("Error", f"Se produjo un error al resolver el sistema: {e}")
        case "Pivoteo":
            try:
                solution = se.pivoteo(A, B)
                show_solution_window(solution)
            except Exception as e:
                messagebox.showerror("Error", f"Se produjo un error al resolver el sistema: {e}")
        case "Gauss Seidel":
            try:
                solution = se.Gauss_s(A, B, X0, tol)
                show_solution_window(solution)
            except Exception as e:
                messagebox.showerror("Error", f"Se produjo un error al resolver el sistema: {e}")
        case _:
            messagebox.showerror("Error", "Seleccione un método válido.")

#error cuando los datos de x, y tienen diferentes tamaños
class SizeYXError(Exception):
    pass

class InvalidCoefficientsError(Exception):
    pass

def format_polynomial(coefficients):
    try:
        polynomial = sum(coef * x**i for i, coef in enumerate(coefficients))
        return polynomial
        #return sp.pretty(polynomial)
    except Exception as e:
        raise InvalidCoefficientsError(f"Error al formatear los coeficientes del polinomio. Error: {str(e)}")

'''
def format_polynomial(coefficients):
    try:
        polynomial = sp.Poly(coefficients[::-1], x)  # coefficients[::-1] to reverse the order for Poly
        return sp.pretty(polynomial)
    except Exception as e:
        raise InvalidCoefficientsError(f"Error al formatear los coeficientes del polinomio. Error: {str(e)}")
'''


def save_interpolation(data_x, data_y, approx, method):
    try:
        data_x = ast.literal_eval(data_x)
        data_y = ast.literal_eval(data_y)
        approx = float(approx)
        if (not isinstance(data_x, list)) or (not isinstance(data_y, list)):
            raise ValueError
        if not len(data_x)==len(data_y):
            raise(SizeYXError)
        
        data_x = np.array(data_x)
        data_y = np.array(data_y)
        
        match method:
            case "Polinomial simple":
                try:
                    coefficients = i_a.Pol_simple(data_x, data_y)
                    dato_aproximado = i_a.Poly(coefficients, float(approx))
                    polynomial_str = format_polynomial(coefficients)
                    show_solution_int_ajuste(polynomial_str, dato_aproximado)
                    #how_solution_int_ajuste(format_polynomial)
                except InvalidCoefficientsError as e:
                    messagebox.showerror("Error", str(e))
            case "Lagrange":
                poly = i_a.Pol_lagrange(data_x, data_y)
                P_x = sp.lambdify(x, poly)
                dato_aproximado = P_x(float(approx))
                polynomial_str = sp.pretty(poly)
                #print(polynomial_str)
                show_solution_int_ajuste(polynomial_str, dato_aproximado)

            case "Mínimos cuadrados":
                intercept, slope_min_c = i_a.min_c(data_x, data_y)
                dato_aproximado = intercept + slope_min_c*float(approx)
                show_solution_min_c(intercept, slope_min_c, dato_aproximado)
            case _:
                messagebox.showerror("Error", "Seleccione un método válido.")
    except (ValueError, SyntaxError):
        messagebox.showerror("Error", "Por favor ingrese datos válidos.")
    except (SizeYXError):
        messagebox.showerror("Error", "los datos de x y y debe tener el mismo tamaño")
    


def save_differential_eq(eq_entries, cond_entries, method, a, b, h):
    if len(eq_entries) == 0 or len(cond_entries) == 0:
        messagebox.showerror("Error", "El número de ecuaciones y el número de condiciones iniciales no pueden ser cero.")
        return

    try:
        equations = [eval(f"lambda x, y: {entry.get()}") for entry in eq_entries]
        conditions = [float(entry.get()) for entry in cond_entries]
        a = float(a)
        b = float(b)
        h = float(h)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos para las condiciones iniciales, a, b y h.")
        return

    co = np.array(conditions)

    def f(t, y, eq=equations):
        n = len(y)
        F = np.zeros(n)
        for i in range(n):
            for j in range(len(eq)):
                F[i] = eq[j](t, y[i])
        return F

    match method:
        case "Euler de orden 4":
            try:
                t, result = ed.Euler(f, a, b, co, h)
                grafica = ed.graficar(result, t, len(conditions))
            except Exception as e:
                messagebox.showerror("Error", f"Se produjo un error al resolver la ecuación diferencial: {e}")
        case "Runge Kutta de orden 4":
            try:
                result, t = ed.RungeKutta(f, a, b, h, co)
                grafica = ed.graficar(result, t, len(conditions))
            except Exception as e:
                messagebox.showerror("Error", f"Se produjo un error al resolver la ecuación diferencial: {e}")
        case _:
            messagebox.showerror("Error", "Seleccione un método válido.")


# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz Principal")

# Crear un marco para los botones
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

# Lista de textos para los botones
button_texts = [
    ("Serie de Taylor", open_taylor_window),
    ("Ceros de Funciones", open_zeros_window),
    ("Sistemas de Ecuaciones Lineales", open_linear_systems_window),
    ("Interpolación y ajuste", open_interpolation_window),
    ("Ecuaciones Diferenciales", open_differential_eq_window)
]

# Crear los botones con textos encima
for i, (text, command) in enumerate(button_texts):
    button = tk.Button(frame, text=text, command=command)
    button.grid(row=i, column=0, pady=5, padx=10, sticky=(tk.W, tk.E))

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
