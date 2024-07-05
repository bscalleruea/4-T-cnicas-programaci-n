class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo encapsulado
        self.__edad = edad  # Atributo encapsulado

    def descripcion(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad} años"

    def sonido(self):
        pass  # Método que será sobrescrito en las clases derivadas

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def sonido(self):
        return "Ladra"

    def descripcion(self):
        return f"{super().descripcion()}, Raza: {self.raza}"
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def sonido(self):
        return "Maúlla"

    def descripcion(self):
        return f"{super().descripcion()}, Color: {self.color}"
def mostrar_animales(animales):
    for animal in animales:
        print(f"{animal.descripcion()}, Sonido: {animal.sonido()}")


def main():
    # Crear instancias de Perro y Gato
    perro = Perro("Bobby", 5, "Labrador")
    gato = Gato("Samy", 3, "Negro")

    # Lista de animales para la demostración (polimorfismo)
    animales = [perro, gato]

    # Mostrar descripciones y sonidos de los animales
    mostrar_animales(animales)


if __name__ == "__main__":
    main()
