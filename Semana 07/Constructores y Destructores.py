class Archivo:
    def __init__(self, nombre_archivo):
        """
        Constructor que inicializa el nombre del archivo y abre el archivo para escribir.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(nombre_archivo, 'w')
        print(f"Archivo '{self.nombre_archivo}' abierto para escritura.")

    def escribir(self, texto):
        """
        Método para escribir texto en el archivo.
        """
        self.archivo.write(texto + '\n')

    def __del__(self):
        """
        Destructor que cierra el archivo.
        """
        self.archivo.close()
        print(f"Archivo '{self.nombre_archivo}' cerrado.")

class BaseDeDatos:
    def __init__(self, nombre_db):
        """
        Constructor que inicializa el nombre de la base de datos y simula la conexión.
        """
        self.nombre_db = nombre_db
        self.conectar()
        print(f"Conexión a la base de datos '{self.nombre_db}' establecida.")

    def conectar(self):
        """
        Método que simula la conexión a la base de datos.
        """
        self.conexion_activa = True

    def desconectar(self):
        """
        Método que simula la desconexión de la base de datos.
        """
        self.conexion_activa = False
        print(f"Conexión a la base de datos '{self.nombre_db}' cerrada.")

    def __del__(self):
        """
        Destructor que asegura que la base de datos esté desconectada.
        """
        if self.conexion_activa:
            self.desconectar()

# Uso de las clases
if __name__ == "__main__":
    # Crear y usar un objeto de la clase Archivo
    archivo = Archivo('mi_archivo.txt')
    archivo.escribir('Hola, este es un texto de prueba.')
    archivo.escribir('Escribiendo más líneas en el archivo.')
    # El archivo se cerrará automáticamente cuando el objeto 'archivo' sea destruido

    # Crear y usar un objeto de la clase BaseDeDatos
    db = BaseDeDatos('mi_base_de_datos')
    # Realizar algunas operaciones simuladas con la base de datos
    # La conexión se cerrará automáticamente cuando el objeto 'db' sea destruido
