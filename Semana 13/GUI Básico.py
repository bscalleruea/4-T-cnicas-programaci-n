import tkinter as tk
from tkinter import ttk

# Funciones
def agregar_dato():
    dato = campo_texto.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        campo_texto.delete(0, tk.END)

def limpiar_datos():
    lista_datos.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Gestión de Datos")

# Etiquetas
etiqueta_instrucciones = tk.Label(ventana, text="Ingrese un dato:")
etiqueta_instrucciones.pack(pady=10)

# Campo de texto
campo_texto = tk.Entry(ventana, width=50)
campo_texto.pack(pady=5)

# Botón Agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Botón Limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
boton_limpiar.pack(pady=5)

# Lista para mostrar datos
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
