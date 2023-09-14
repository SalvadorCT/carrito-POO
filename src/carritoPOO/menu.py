from carrito import CarritoDeCompras
from producto import Producto
from users.cliente import Cliente
from archivo import Archivo

def menu_principal():
    print("Bienvenido al Carrito de Compras")
    print("1. Agregar producto al carrito")
    print("2. Quitar producto del carrito")
    print("3. Ver carrito")
    print("4. Calcular total")
    print("5. Salir")

def main():
    archivo = Archivo('personas.csv', 'productos.csv')
    personas = archivo.cargar_personas()
    productos = archivo.cargar_productos()

    print("Ingrese su nombre:")
    nombre = input()
    print("Ingrese su apellido:")
    apellido = input()
    print("Ingrese su edad:")
    edad = int(input())

    cliente = Cliente(nombre, apellido, edad, correo="correo@ejemplo.com")

    carrito = CarritoDeCompras()

    while True:
        menu_principal()
        opcion = input("Elija una opción: ")

        if opcion == "1":
            print("Productos disponibles:")
            for i, producto in enumerate(productos, start=1):
                print(f"{i}. {producto.nombre} - Precio: ${producto.precio:.2f} - Disponible: {producto.cantidad_disponible}")
            seleccion = int(input("Seleccione un producto para agregar al carrito (número): "))
            cantidad = int(input("Ingrese la cantidad: "))
            producto_seleccionado = productos[seleccion - 1]
            carrito.agregar_producto(producto_seleccionado, cantidad)

        elif opcion == "2":
            carrito.mostrar_carrito()
            seleccion = int(input("Seleccione un producto para quitar del carrito (número): "))
            cantidad = int(input("Ingrese la cantidad a quitar: "))
            producto_seleccionado = carrito.items[seleccion - 1]['producto']
            carrito.quitar_producto(producto_seleccionado, cantidad)

        elif opcion == "3":
            carrito.mostrar_carrito()

        elif opcion == "4":
            total = carrito.calcular_total()
            print(f"Total de la compra: ${total:.2f}")

        elif opcion == "5":
            archivo.guardar_personas(personas)
            archivo.guardar_productos(productos)
            break

if __name__ == "__main__":
    main()
