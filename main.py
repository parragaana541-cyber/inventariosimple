import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

    def a_linea_texto(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}\n"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = {}
        self.archivo = archivo
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos.values():
                    f.write(p.a_linea_texto())
            print("[SISTEMA] Cambios guardados en el archivo exitosamente.")
        except Exception as e:
            print(f"[ERROR] No se pudo guardar en el archivo: {e}")

    def cargar_desde_archivo(self):
        if not os.path.exists(self.archivo):
            try:
                open(self.archivo, "w", encoding="utf-8").close()
                print(f"[INFO] Archivo '{self.archivo}' creado.")
            except Exception as e:
                print(f"[ERROR] No se pudo crear el archivo: {e}")
            return

        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    if linea.strip():
                        id_p, nom, cant, prec = linea.strip().split(',')
                        nuevo_p = Producto(id_p, nom, int(cant), float(prec))
                        self.productos[id_p] = nuevo_p
            print("[INFO] Datos cargados correctamente.")
        except Exception as e:
            print(f"[ALERTA] Error al cargar datos (posible formato incorrecto): {e}")

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("[ERROR] El ID ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            print("[OK] Producto agregado.")
            self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("[OK] Producto eliminado.")
            self.guardar_en_archivo()
        else:
            print("[ERROR] Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            print("[OK] Producto actualizado.")
            self.guardar_en_archivo()
        else:
            print("[ERROR] Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("[BUSQUEDA] No se encontraron resultados.")

    def mostrar_inventario(self):
        if not self.productos:
            print("[INFO] El inventario está vacío.")
        else:
            print("\n--- INVENTARIO ACTUAL ---")
            for producto in self.productos.values():
                print(producto)


def menu():
    inventario = Inventario()
    while True:
        print("\n--- GESTION DE INVENTARIO ---")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            try:
                id_p = input("ID unico: ")
                nom = input("Nombre: ")
                cant = int(input("Cantidad: "))
                prec = float(input("Precio: "))
                nuevo = Producto(id_p, nom, cant, prec)
                inventario.agregar_producto(nuevo)
            except ValueError:
                print("[ERROR] Cantidad y Precio deben ser numeros.")

        elif opcion == '2':
            id_p = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_p)

        elif opcion == '3':
            id_p = input("ID del producto a actualizar: ")
            print("Deje en blanco para no modificar.")
            cant_in = input("Nueva cantidad: ")
            prec_in = input("Nuevo precio: ")
            try:
                cant = int(cant_in) if cant_in != "" else None
                prec = float(prec_in) if prec_in != "" else None
                inventario.actualizar_producto(id_p, cant, prec)
            except ValueError:
                print("[ERROR] Formato numerico invalido.")

        elif opcion == '4':
            nom = input("Nombre a buscar: ")
            inventario.buscar_producto(nom)

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            print("Saliendo... ¡Adios!")
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    menu()