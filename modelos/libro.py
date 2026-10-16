class Libro:
    def __init__(self, isbn, titulo, autor,  anio, genero, disponible=True) -> None:
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.disponible = disponible

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "Prestado"
        return f"\n - Isbn: {self.isbn}\n - Título:{self.titulo}\n - Autor: {self.autor}\n - Género: {self.genero}\n - Año de publicación: {self.anio}\n - Disponible: {estado}\n"

    def __eq__(self, value):
        return self.isbn == value.isbn