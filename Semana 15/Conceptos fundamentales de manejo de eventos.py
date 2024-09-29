import tkinter as tk
from tkinter import messagebox

# Funciones de la lógica de la aplicación
def add_task(event=None):
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Debes escribir una tarea antes de añadirla.")

def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, f"[Completada] {task}")
    except IndexError:
        messagebox.showwarning("Selección de tarea", "Debes seleccionar una tarea para marcarla como completada.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selección de tarea", "Debes seleccionar una tarea para eliminarla.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")

# Entrada para escribir nuevas tareas
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10)
task_entry.bind("<Return>", add_task)  # Permite añadir la tarea presionando Enter

# Botones
add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.grid(row=0, column=1, padx=10)

mark_button = tk.Button(root, text="Marcar como Completada", command=mark_completed)
mark_button.grid(row=1, column=0, padx=10, pady=10)

delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.grid(row=1, column=1, padx=10, pady=10)

# Listbox para mostrar las tareas
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Iniciar el loop principal de la aplicación
root.mainloop()
