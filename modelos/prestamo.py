from datetime import date


class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo=None, fecha_devolucion = None):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = (fecha_prestamo if fecha_prestamo is not None else date.today())
        self.fecha_devolucion = fecha_devolucion

    @property
    def activo(self):
        return self.fecha_devolucion is None

    def __str__(self) -> str:
        estado = "Activo" if self.activo else f"Devuelto ({self.fecha_devolucion})"

        return f" - Usuario: {self.usuario.nombre} {self.usuario.apellidos}\n - Libro: {self.libro.titulo}\n - Fecha de Prestamo: {self.fecha_prestamo}\n - Préstamo: {estado}"
