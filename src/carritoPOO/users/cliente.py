from persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, edad, correo):
        super().__init__(nombre, apellido, edad)
        self.correo = correo

    def __str__(self):
        return f'Cliente: {super().__str__()},\nCorreo: {self.correo}'
    

