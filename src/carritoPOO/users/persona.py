class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f'\nNombre: {self.nombre}\n,Apellido: {self.apellido},\nEdad: {self.edad} años'




