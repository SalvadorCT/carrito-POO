from persona import Persona

class Administrador(Persona):
    def __init__(self, nombre, apellido, edad, cargo):
        super().__init__(nombre, apellido, edad)
        self.cargo = cargo

    def __str__(self):
        return f'Administrador: {super().__str__()},\nCargo: {self.cargo}'
