class Usuario:
    def __init__(self, id, nombre, apellidos, email) -> str:
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

    def __str__(self) -> str:
        return f" - ID: {self.id}\n - Nombre: {self.nombre}\n - Apellidos: {self.apellidos}\n - Email: {self.email}"

    def __eq__(self, value):
        return self.id == value.id
