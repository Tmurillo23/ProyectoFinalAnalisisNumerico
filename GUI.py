import tkinter as tk
from tkinter import ttk
from Modulos import Ceros
from Modulos import serie as sr

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

    label_interval = tk.Label(window, text="Intervalo (si el método es diferente de  Newton) o dato inicial(si el método es Newton):")
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

    label_method = tk.Label(window, text="Ingrese el método:")
    label_method.pack(pady=10)
    methods = ["Eliminación Gaussiana", "Pivoteo", "Gauss Seidel"]
    method_combobox = ttk.Combobox(window, values=methods)
    method_combobox.pack(pady=10)

    save_button = tk.Button(window, text="Resolver",
                            command=lambda: save_linear_systems(entry_system.get(), method_combobox.get()))
    save_button.pack(pady=10)


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


def open_differential_eq_window():
    window = tk.Toplevel(root)
    window.title("Ecuaciones Diferenciales")

    label = tk.Label(window, text="La ecuación diferencial de primer orden:")
    label.pack(pady=10)
    entry_equation = tk.Entry(window, width=50)
    entry_equation.pack(pady=10)

    label_conditions = tk.Label(window, text="Condiciones iniciales:")
    label_conditions.pack(pady=10)
    entry_conditions = tk.Entry(window, width=50)
    entry_conditions.pack(pady=10)

    label_method = tk.Label(window, text="Método:")
    label_method.pack(pady=10)
    methods = ["Euler de orden 4", "Runge Kutta de orden 4"]
    method_combobox = ttk.Combobox(window, values=methods)
    method_combobox.pack(pady=10)

    save_button = tk.Button(window, text="Resolver",
                            command=lambda: save_differential_eq(entry_equation.get(), entry_conditions.get(),
                                                                 method_combobox.get()))
    save_button.pack(pady=10)


# Funciones para guardar los datos ingresados
def save_taylor(function, x_0, degree):
    poli = sr.S_taylor(function, float(x_0), int(degree))
    result_window = tk.Toplevel(root)
    result_window.title("Resultado de la Serie de Taylor")
    result_label = tk.Label(result_window, text=f"Función: {poli}\nGrado: {degree}")
    result_label.pack(pady=10)
    #print(f"Función: {poli}, Grado: {degree}")


def save_zeros(function, interval, accuracy, method):
    if method == 'Bisección':
        sol, cont = Modulos.Ceros()
    print(f"Función: {function}, Intervalo: {interval}, Exactitud: {accuracy}, Método: {method}")


def save_linear_systems(system, method):
    print(f"Sistema de Ecuaciones: {system}, Método: {method}")


def save_interpolation(data, approx, method):
    print(f"Datos: {data}, Aproximación: {approx}, Método: {method}")


def save_differential_eq(equation, conditions, method):
    print(f"Ecuación: {equation}, Condiciones Iniciales: {conditions}, Método: {method}")


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
