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

def on_number_of_equations_change(event):
    try:
        num_eqs = int(entry_num_eqs.get())
        for widget in frame_equations.winfo_children():
            widget.destroy()

        for i in range(num_eqs):
            label = tk.Label(frame_equations, text=f"Ecuación {i + 1}:")
            label.grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(frame_equations, width=50)
            entry.grid(row=i, column=1, padx=5, pady=5)
            equation_entries.append(entry)
    except ValueError:
        pass

def on_number_of_conditions_change(event):
    try:
        num_conds = int(entry_num_conds.get())
        for widget in frame_conditions.winfo_children():
            widget.destroy()

        for i in range(num_conds):
            label = tk.Label(frame_conditions, text=f"Condición inicial {i + 1}:")
            label.grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(frame_conditions, width=50)
            entry.grid(row=i, column=1, padx=5, pady=5)
            condition_entries.append(entry)
    except ValueError:
        pass
def show_solution_window(solution):
    solution_window = tk.Toplevel(root)
    solution_window.title("Solución")

    label_solution = tk.Label(solution_window, text="Solución:")
    label_solution.pack(pady=10)

    solution_str = solution
    entry_solution = tk.Entry(solution_window, width=50)
    entry_solution.insert(0, solution_str)
    entry_solution.config(state='readonly')
    entry_solution.pack(pady=10)

def open_differential_eq_window():
    window = tk.Toplevel(root)
    window.title("Ecuaciones Diferenciales")

    global entry_num_eqs, entry_num_conds, frame_equations, frame_conditions
    global equation_entries, condition_entries
    equation_entries = []
    condition_entries = []

    label_num_eqs = tk.Label(window, text="Número de ecuaciones diferenciales:")
    label_num_eqs.pack(pady=10)
    entry_num_eqs = tk.Entry(window, width=50)
    entry_num_eqs.pack(pady=10)
    entry_num_eqs.bind("<Return>", on_number_of_equations_change)

    frame_equations = tk.Frame(window)
    frame_equations.pack(pady=10)

    label_num_conds = tk.Label(window, text="Número de condiciones iniciales:")
    label_num_conds.pack(pady=10)
    entry_num_conds = tk.Entry(window, width=50)
    entry_num_conds.pack(pady=10)
    entry_num_conds.bind("<Return>", on_number_of_conditions_change)

    frame_conditions = tk.Frame(window)
    frame_conditions.pack(pady=10)

    label_method = tk.Label(window, text="Método:")
    label_method.pack(pady=10)
    methods = ["Euler de orden 4", "Runge Kutta de orden 4"]
    method_combobox = ttk.Combobox(window, values=methods)
    method_combobox.pack(pady=10)

    save_button = tk.Button(window, text="Resolver",
                            command=lambda: save_differential_eq(equation_entries, condition_entries,
                                                                 method_combobox.get()))
    save_button.pack(pady=10)

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

def save_differential_eq(equations, conditions, method):
    eqs = [entry.get() for entry in equation_entries]
    conds = [entry.get() for entry in condition_entries]
    # Aquí puedes procesar las ecuaciones y condiciones
    solution =
    show_solution_window("Solución de prueba")

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
