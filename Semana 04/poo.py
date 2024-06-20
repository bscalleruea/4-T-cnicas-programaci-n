# Clase para representar un cliente del hotel
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}"

# Clase para representar una habitación del hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.esta_ocupada = False

    def __str__(self):
        estado = "Ocupada" if self.esta_ocupada else "Disponible"
        return f"Habitacion {self.numero} ({self.tipo}) - {estado}, Precio: ${self.precio}"

# Clase para gestionar las reservas
class Reserva:
    def __init__(self, cliente, habitacion):
        self.cliente = cliente
        self.habitacion = habitacion

    def confirmar_reserva(self):
        if not self.habitacion.esta_ocupada:
            self.habitacion.esta_ocupada = True
            return f"Reserva confirmada para {self.cliente.nombre} en la habitación {self.habitacion.numero}."
        else:
            return f"Lo siento, la habitación {self.habitacion.numero} ya está ocupada."

# Ejemplo de uso de las clases
if __name__ == "__main__":
    # Crear un cliente
    cliente1 = Cliente("Juan Perez", "juan.perez@example.com")
    print(cliente1)

    # Crear habitaciones
    habitacion1 = Habitacion(150, "Individual", 80)
    habitacion2 = Habitacion(102, "Doble", 80)
    print(habitacion1)
    print(habitacion2)

    # Crear una reserva
    reserva1 = Reserva(cliente1, habitacion1)
    print(reserva1.confirmar_reserva())

    # Intentar reservar la misma habitación nuevamente
    reserva2 = Reserva(cliente1, habitacion1)
    print(reserva2.confirmar_reserva())
