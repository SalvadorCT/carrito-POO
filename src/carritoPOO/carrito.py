from producto import Producto

class CarritoDeCompras:
    def __init__(self):
        # Lista de productos
        self.items = []

    def agregar_producto(self, producto, cantidad=1):
        """Agrega un producto al carrito con una cantidad especificada."""
        if cantidad > 0 and producto.cantidad_disponible >= cantidad:
            for item in self.items:
                if item['producto'] == producto:
                    item['cantidad'] += cantidad
                    break
            else:
                self.items.append({'producto': producto, 'cantidad': cantidad})
            producto.cantidad_disponible -= cantidad
        else:
            print("No se puede agregar el producto al carrito.")

    def quitar_producto(self, producto, cantidad=1):
        """Quita un producto del carrito con una cantidad especificada."""
        for item in self.items:
            if item['producto'] == producto:
                if cantidad >= item['cantidad']:
                    self.items.remove(item)
                else:
                    item['cantidad'] -= cantidad
                producto.cantidad_disponible += cantidad
                break

    def calcular_total(self):
        """Calcula el total de la compra en el carrito."""
        total = 0
        for item in self.items:
            producto = item['producto']
            cantidad = item['cantidad']
            precio_con_descuento = producto.precio * (1 - producto.descuento / 100)
            total += precio_con_descuento * cantidad
        return total

    def mostrar_carrito(self):
        """Muestra los productos en el carrito y la cantidad."""
        print("Carrito de Compras:")
        for item in self.items:
            producto = item['producto']
            cantidad = item['cantidad']
            print(f'{producto.nombre} x{cantidad}')
