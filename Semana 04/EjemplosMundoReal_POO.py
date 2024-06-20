class Habitacion:
    def __init__(self, numero, tipo):
        """
        Inicializa una habitación con un número y un tipo.
        El tipo puede ser 'individual', 'doble', 'suite', etc.
        """
        self.numero = numero
        self.tipo = tipo
        self.disponible = True

    def __str__(self):
        """
        Devuelve una representación en cadena de la habitación.
        """
        estado = "Disponible" if self.disponible else "Reservada"
        return f"Habitación {self.numero} ({self.tipo}) - {estado}"

class Reserva:
    def __init__(self, nombre_huesped, habitacion):
        """
        Inicializa una reserva con el nombre del huésped y la habitación reservada.
        """
        self.nombre_huesped = nombre_huesped
        self.habitacion = habitacion

    def __str__(self):
        """
        Devuelve una representación en cadena de la reserva.
        """
        return f"Reserva: {self.nombre_huesped} ha reservado la {self.habitacion}"

class Hotel:
    def __init__(self, nombre):
        """
        Inicializa un hotel con un nombre y una lista de habitaciones y reservas.
        """
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        """
        Agrega una habitación a la lista de habitaciones del hotel.
        """
        self.habitaciones.append(habitacion)

    def hacer_reserva(self, nombre_huesped, numero_habitacion):
        """
        Realiza una reserva para un huésped en una habitación específica.
        """
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion:
                if habitacion.disponible:
                    habitacion.disponible = False
                    nueva_reserva = Reserva(nombre_huesped, habitacion)
                    self.reservas.append(nueva_reserva)
                    print(f"Reserva exitosa para {nombre_huesped} en la habitación {numero_habitacion}")
                    return
                else:
                    print(f"La habitación {numero_habitacion} ya está reservada.")
                    return
        print(f"La habitación {numero_habitacion} no existe en el hotel.")

    def cancelar_reserva(self, numero_habitacion):
        """
        Cancela una reserva en una habitación específica.
        """
        for reserva in self.reservas:
            if reserva.habitacion.numero == numero_habitacion:
                reserva.habitacion.disponible = True
                self.reservas.remove(reserva)
                print(f"Reserva en la habitación {numero_habitacion} ha sido cancelada.")
                return
        print(f"No hay ninguna reserva para la habitación {numero_habitacion}.")

    def mostrar_habitaciones(self):
        """
        Muestra el estado de todas las habitaciones del hotel.
        """
        for habitacion in self.habitaciones:
            print(habitacion)

    def mostrar_reservas(self):
        """
        Muestra todas las reservas realizadas en el hotel.
        """
        for reserva in self.reservas:
            print(reserva)

# Ejemplo de uso del sistema de reservas del hotel
hotel = Hotel("Hotel POO")

# Agregar habitaciones al hotel
hotel.agregar_habitacion(Habitacion(101, "individual"))
hotel.agregar_habitacion(Habitacion(102, "doble"))
hotel.agregar_habitacion(Habitacion(201, "suite"))

# Mostrar habitaciones disponibles
print("Estado inicial de las habitaciones:")
hotel.mostrar_habitaciones()

# Realizar reservas
hotel.hacer_reserva("Juan Pérez", 101)
hotel.hacer_reserva("María López", 201)

# Mostrar reservas realizadas
print("\nReservas realizadas:")
hotel.mostrar_reservas()

# Mostrar habitaciones después de realizar reservas
print("\nEstado de las habitaciones después de las reservas:")
hotel.mostrar_habitaciones()

# Cancelar una reserva
hotel.cancelar_reserva(101)

# Mostrar estado final de las habitaciones y reservas
print("\nEstado final de las habitaciones:")
hotel.mostrar_habitaciones()

print("\nReservas finales:")
hotel.mostrar_reservas()
