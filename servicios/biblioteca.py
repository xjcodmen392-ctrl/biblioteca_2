from modelos.libro import Libro
from datetime import date

class Biblioteca:
    def __init__(self) -> None:
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def registrar_libro(self, libro_nuevo):
        if self.buscar_libro(libro_nuevo):
            print("El libro ya está en la lista")
            return
        self.libros.append(libro_nuevo)
        print("El libro ha sido registrado correctamente.")

    def buscar_libro(self, libro_nuevo):
        for libro in self.libros:
            if libro.__eq__(libro_nuevo):
                return libro
        return None

    def buscar_libro_isbn(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def buscar_libro_titulo(self, titulo):
        libros_titulo = [libro for libro in self.libros if libro.titulo == titulo]
        if not libros_titulo:
            print("No se han encontrado libros de ese titulo. ")
            return
        for libro in libros_titulo:
            print(libro)

    def buscar_libro_autor(self, autor):
        libros_autor = [libro for libro in self.libros if autor == libro.autor]
        if not libros_autor:
            print("No se han encontrado libros de ese autor.")
            return
        for libro in libros_autor:
            print(libro)
    
    def listar_libros(self):
        for libro in self.libros:
            print(libro)


    def listar_libros_prestados(self):
        prestados = [libro for libro in self.libros if not libro.disponible]
        if not prestados:
            print("No se han encontrado libros prestados.")
            return
        for libro in prestados:
            print(libro)

    def listar_libros_disponibles(self):
        disponibles = [libro for libro in self.libros if libro.disponible]
        if not disponibles:
            print("No se han encontrado libros disponibles.")
            return
        for libro in disponibles:
            print(libro)


    def registrar_usuario(self, usuario_nuevo):
        if self.buscar_usuario(usuario_nuevo):
            print("El usuario ya está registrado")
            return
        self.usuarios.append(usuario_nuevo)
        print("El usuario ha sido registrado correctamente.")

    def buscar_usuario(self, usuario_nuevo):
        for usuario in self.usuarios:
            if usuario.__eq__(usuario_nuevo):
                return usuario
        return None

    def buscar_usuario_id(self, iD_usuario):
        for usuario in self.usuarios:
            if usuario.id == iD_usuario:
                return usuario
        return None

    

    def registrar_prestamo(self, nuevo_prestamo):
        if self.buscar_prestamo(nuevo_prestamo):
            print("El libro ha sido prestado y aún no se ha devuelto.")
            return
        nuevo_prestamo.libro.disponible = False
        self.prestamos.append(nuevo_prestamo)
        print("El préstamo ha sido registrado correctamente.")
        

    def buscar_prestamo(self, prestamo_nuevo):
        for prestamo in self.prestamos:
            if prestamo.libro == prestamo_nuevo.libro and prestamo.fecha_devolucion is None:
                return prestamo
        return None

    def registrar_devolucion(self, usuario, libro):
        for prestamo in self.prestamos:
            if prestamo.usuario == usuario and prestamo.libro == libro and prestamo.fecha_devolucion is None:
                prestamo.fecha_devolucion = date.today()
                prestamo.libro.disponible = True
                print("La devolución ha sido registrada correctamente.")
                return
        print("No se ha encontrado el préstamo para registrar la devolución.")

    def mostrar_prestamos_activos(self):
        prestados_activos = [prestamo for prestamo in self.prestamos if prestamo.activo]
        if not prestados_activos:
            print("No se han encontrado prestamos activos.")
            return
        for prestamo in prestados_activos:
            print(prestamo)

    def mostrar_prestamos_usuario(self,usuario):
        activos = [p for p in self.prestamos if p.usuario == usuario and p.fecha_devolucion is None]
        if not activos:
            print("Este usuario no tiene préstamos activos.")
            return
        for prestamo in activos:
            print(prestamo)