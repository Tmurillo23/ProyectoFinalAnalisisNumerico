import ast
import tkinter as tk
import numpy as np
from tkinter import ttk
import Modulos
from Modulos import Ceros
from Modulos import serie as sr
from Modulos import sistemas_ecuaciones_lineales as se
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
                              text="Intervalo (si el método es diferente de  Newton) o dato inicial(si el método es Newton):")
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

    label = tk.Label(window, text="Datos:")
    label.pack(pady=10)
    entry_data = tk.Entry(window, width=50)
    entry_data.pack(pady=10)

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
                            command=lambda: save_interpolation(entry_data.get(), entry_approx.get(),
                                                               method_combobox.get()))
    save_button.pack(pady=10)

def on_num_eq_change(event):
    num_eq = int(entry_num_eq.get())
    for widget in frame_eq.winfo_children():
        widget.destroy()
    for i in range(num_eq):
        label_eq = tk.Label(frame_eq, text=f"Ecuación {i+1}:")
        label_eq.grid(row=i, column=0, pady=5)
        entry_eq = tk.Entry(frame_eq, width=50)
        entry_eq.grid(row=i, column=1, pady=5)
        eq_entries.append(entry_eq)

def on_num_cond_change(event):
    num_cond = int(entry_num_cond.get())
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

# Configuración de la ventana principal
root = tk.Tk()
root.title("Solver de Ecuaciones Diferenciales")

main_button = tk.Button(root, text="Abrir ventana de ecuaciones diferenciales", command=open_differential_eq_window)
main_button.pack(pady=20)


# Funciones para guardar los datos ingresados
def save_taylor(function, x_0, degree):
    poli = sr.S_taylor(function, float(x_0), int(degree))
    result_window = tk.Toplevel(root)
    result_window.title("Resultado de la Serie de Taylor")
    result_label = tk.Label(result_window, text=f"Función: {poli}\nGrado: {degree}")
    result_label.pack(pady=10)
    grafica = sr.grafica_polinomio(function, float(x_0), 1, int(degree))


def save_zeros(function, interval, accuracy, method):
    if method == 'Bisección':
        sol, cont = Modulos.Ceros
    print(f"Función: {function}, Intervalo: {interval}, Exactitud: {accuracy}, Método: {method}")


def save_linear_systems(system, method, b, x0, tol):
    A = np.array(ast.literal_eval(system))
    B = np.array(ast.literal_eval(b))
    match method:
        case "Eliminación Gaussiana":
            solution = se.Eliminacion_Gaussiana(A,B)
            show_solution_window(solution)
        case "Pivoteo":
            solution = se.pivoteo(A,B)
            show_solution_window(solution)
        case "Gauss Seidel":
            X0 = np.array(ast.literal_eval(x0))
            solution = se.Gauss_s(A,B,X0,float(tol))
            show_solution_window(solution)
        case _:
            print("Seleccione un método correcto")



def save_interpolation(data, approx, method):
    print(f"Datos: {data}, Aproximación: {approx}, Método: {method}")

def save_differential_eq(eq_entries, cond_entries, method, a, b, h):
    equations = [entry.get() for entry in eq_entries]
    conditions = [float(entry.get()) for entry in cond_entries]
    a = float(a)
    b = float(b)
    h = float(h)
    match method:
        case "Euler de orden 4":
            t, result = ed.Euler(eq_entries, a, b, cond_entries, h)
            grafica = ed.graficar(result,t)
        case "Runge Kutta de orden 4":
            t, result = ed.RungeKutta(eq_entries, a, b, h, cond_entries)
            grafica = ed.graficar(result,t)
        case _:
            print("Seleccione un método correcto")

        # Mostrar resultados en una nueva ventana
    result_window = tk.Toplevel(root)
    result_window.title("Solución")

    label_result = tk.Label(result_window, text="Solución:")
    label_result.pack(pady=10)

    result_str = f"Tiempo: {t}\nY(t): {result[:, 0]}\nYp(t): {result[:, 1]}"
    result_text = tk.Text(result_window, height=15, width=80)
    result_text.pack(pady=10)
    result_text.insert(tk.END, result_str)

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
