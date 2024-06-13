import tkinter as tk
from src.model.huerta import Huerta

class MainFrame(tk.Frame):
    def __init__(self, master, huerta:Huerta):
        super().__init__(master)
        label = tk.Label(self,  text="Sistema de registro y seguimiento Ecohuerta UdeM", background="red", foreground="white", font="system")
        label.grid(column=2,row=1)
        label2=tk.Label(self, text="Bienvenido al sistema de registro y seguimiento de la Ecohuerta de la Universidad de Medellín. \n  Aquí podrá realizar las siguientes acciones:\n", font="system").grid(column=2, row=2)