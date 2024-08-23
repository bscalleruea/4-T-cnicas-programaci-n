class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y setters
    def get_id_producto(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        self.productos = []
        import os

        class Producto:
            def __init__(self, nombre, cantidad, precio):
                self.nombre = nombre
                self.cantidad = cantidad
                self.precio = precio

            def __str__(self):
                return f'{self.nombre},{self.cantidad},{self.precio}'

        class Inventario:
            def __init__(self, archivo='inventario.txt'):
                self.archivo = archivo
                self.productos = {}
                self.cargar_inventario()

            def cargar_inventario(self):
                if os.path.exists(self.archivo):
                    try:
                        with open(self.archivo, 'r') as file:
                            for linea in file:
                                nombre, cantidad, precio = linea.strip().split(',')
                                self.productos[nombre] = Producto(nombre, int(cantidad), float(precio))
                    except (FileNotFoundError, PermissionError) as e:
                        print(f'Error al cargar el archivo de inventario: {e}')
                else:
                    print('El archivo de inventario no existe. Se creará uno nuevo.')

            def guardar_inventario(self):
                try:
                    with open(self.archivo, 'w') as file:
                        for producto in self.productos.values():
                            file.write(f'{producto}\n')
                except (PermissionError, IOError) as e:
                    print(f'Error al guardar el archivo de inventario: {e}')

            def añadir_producto(self, producto):
                self.productos[producto.nombre] = producto
                self.guardar_inventario()
                print(f'Producto {producto.nombre} añadido exitosamente.')

            def actualizar_producto(self, nombre, cantidad, precio):
                if nombre in self.productos:
                    self.productos[nombre].cantidad = cantidad
                    self.productos[nombre].precio = precio
                    self.guardar_inventario()
                    print(f'Producto {nombre} actualizado exitosamente.')
                else:
                    print(f'Producto {nombre} no encontrado en el inventario.')

            def eliminar_producto(self, nombre):
                if nombre in self.productos:
                    del self.productos[nombre]
                    self.guardar_inventario()
                    print(f'Producto {nombre} eliminado exitosamente.')
                else:
                    print(f'Producto {nombre} no encontrado en el inventario.')

            def mostrar_inventario(self):
                for producto in self.productos.values():
                    print(producto)

        # Ejemplo de uso
        inventario = Inventario()
        inventario.añadir_producto(Producto('Manzana', 10, 0.5))
        inventario.actualizar_producto('Manzana', 20, 0.4)
        inventario.eliminar_producto('Manzana')
        inventario.mostrar_inventario()

    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id_producto() == producto.get_id_producto():
                print("Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado con éxito.")
                return
        print("Error: No se encontró un producto con ese ID.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado con éxito.")
                return
        print("Error: No se encontró un producto con ese ID.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for p in self.productos:
                print(p)
        else:
            print("El inventario está vacío.")


def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto")
        print("4. Buscar productos por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            print("Deje el campo en blanco si no desea actualizarlo.")
            cantidad = input("Ingrese la nueva cantidad del producto: ")
            precio = input("Ingrese el nuevo precio del producto: ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
