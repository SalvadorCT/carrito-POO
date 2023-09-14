# Archivo para la gestion de archivos

from users.persona import Persona
from producto import Producto
import csv

class Archivo:
    def __init__(self, archivo_personas, archivo_productos):
        self.archivo_personas = archivo_personas
        self.archivo_productos = archivo_productos

    def cargar_personas(self):
        personas = []
        try:
            with open(self.archivo_personas, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    nombre = row['Nombre']
                    apellido = row['Apellido']
                    edad = int(row['Edad'])
                    personas.append(Persona(nombre, apellido, edad))
        except FileNotFoundError:
            print(f'El archivo {self.archivo_personas} no existe.')
        return personas

    def cargar_productos(self):
        productos = []
        try:
            with open(self.archivo_productos, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    nombre = row['Nombre']
                    precio = float(row['Precio'])
                    cantidad_disponible = int(row['Cantidad Disponible'])
                    descuento = float(row['Descuento'])
                    productos.append(Producto(nombre, precio, cantidad_disponible, descuento))
        except FileNotFoundError:
            print(f'El archivo {self.archivo_productos} no existe.')
        return productos

    def guardar_personas(self, personas):
        with open(self.archivo_personas, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nombre', 'Apellido', 'Edad'])
            for persona in personas:
                writer.writerow([persona.nombre, persona.apellido, persona.edad])

    def guardar_productos(self, productos):
        with open(self.archivo_productos, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nombre', 'Precio', 'Cantidad Disponible', 'Descuento'])
            for producto in productos:
                writer.writerow([producto.nombre, producto.precio, producto.cantidad_disponible, producto.descuento])

