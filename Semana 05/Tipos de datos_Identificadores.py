"""
Este programa calcula el área de un círculo y de un rectángulo.
El usuario puede elegir qué área calcular y proporcionar los valores necesarios.
"""

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    :param radio: Radio del círculo (float)
    :return: Área del círculo (float)
    """
    import math
    return math.pi * (radio ** 2)

def calcular_area_rectangulo(largo, ancho):
    """
    Calcula el área de un rectángulo dado su largo y ancho.
    :param largo: Largo del rectángulo (float)
    :param ancho: Ancho del rectángulo (float)
    :return: Área del rectángulo (float)
    """
    return largo * ancho

def obtener_datos_float(mensaje):
    """
    Solicita un valor float al usuario.
    :param mensaje: Mensaje a mostrar al usuario (string)
    :return: Valor float ingresado por el usuario
    """
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Por favor, ingrese un número válido.")

def main():
    """
    Función principal que ejecuta el programa.
    """
    print("Seleccione la figura para calcular el área:")
    print("1. Círculo")
    print("2. Rectángulo")

    opcion = input("Ingrese el número de su opción: ")

    if opcion == "1":
        radio = obtener_datos_float("Ingrese el radio del círculo: ")
        area = calcular_area_circulo(radio)
        figura = "círculo"
    elif opcion == "2":
        largo = obtener_datos_float("Ingrese el largo del rectángulo: ")
        ancho = obtener_datos_float("Ingrese el ancho del rectángulo: ")
        area = calcular_area_rectangulo(largo, ancho)
        figura = "rectángulo"
    else:
        print("Opción no válida. Saliendo del programa.")
        return

    print(f"El área del {figura} es: {area}")

if __name__ == "__main__":
    main()
