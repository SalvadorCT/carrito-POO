class Producto:
    def __init__(self, nombre, precio, cantidad_disponible, descuento=0):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
        self.descuento = descuento

    def aplicar_descuento(self, porcentaje):
        self.descuento = porcentaje

    def __str__(self):
        return f'{self.nombre} - Precio: ${self.precio:.2f}, Disponible: {self.cantidad_disponible}, Descuento: {self.descuento}%'
