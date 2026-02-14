class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("❌ Error: El ID ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            print("✅ Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("🗑️ Producto eliminado.")
        else:
            print("❌ Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            print("🔄 Producto actualizado.")
        else:
            print("❌ Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("🔍 No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if not self.productos:
            print("📭 El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)


# Interfaz de usuario en la consola
def menu():
    inventario = Inventario()
    while True:
        print("\n---  GESTIÓN DE INVENTARIO ---")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                id_p = input("ID único: ")
                nom = input("Nombre: ")
                cant = int(input("Cantidad: "))
                prec = float(input("Precio: "))
                nuevo = Producto(id_p, nom, cant, prec)
                inventario.agregar_producto(nuevo)
            except ValueError:
                print("⚠️ Error: Cantidad y Precio deben ser números.")

        elif opcion == '2':
            id_p = input("ID del producto a eliminar: ")

            inventario.eliminar_producto(id_p)

        elif opcion == '3':
            id_p = input("ID del producto a actualizar: ")
            print("Deje en blanco para no modificar.")
            cant_in = input("Nueva cantidad: ")
            prec_in = input("Nuevo precio: ")

            # Solo convertimos si el usuario escribió algo
            cant = int(cant_in) if cant_in != "" else None
            prec = float(prec_in) if prec_in != "" else None

            inventario.actualizar_producto(id_p, cant, prec)

        elif opcion == '4':
            nom = input("Nombre a buscar: ")
            inventario.buscar_producto(nom)

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            print("Saliendo del sistema... ¡Adiós!")
            break
        else:
            print("Opcion no válida, intente de nuevo.")


if __name__ == "__main__":
    menu()