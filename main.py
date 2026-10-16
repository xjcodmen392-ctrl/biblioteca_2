from modelos.libro import Libro
from modelos.prestamo import Prestamo
from modelos.usuario import Usuario
from servicios.biblioteca import Biblioteca

def mostrar_menu():
    print("\n=================================")
    print("      GESTIÓN DE BIBLIOTECA")
    print("=================================")
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Buscar libro")
    print("4. Listar libros")
    print("5. Realizar préstamo")
    print("6. Registrar devolución")
    print("7. Mostrar préstamos activos")
    print("8. Mostrar préstamos de un usuario")
    print("9. Guardar datos")
    print("0. Salir")
    print("=================================\n")

def registrar_libro(biblioteca):
    isbn = input("Isbn: ").strip()
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    anio = input("Año: ").strip()
    genero = input("Género: ").strip()

    libro = Libro(isbn, titulo, autor, anio, genero)
    biblioteca.registrar_libro(libro)

def registrar_usuario(biblioteca):
    iD = input("ID: ")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    email = input("Email: ")

    usuario = Usuario(iD, nombre, apellidos, email)
    biblioteca.registrar_usuario(usuario)

def buscar_libro(biblioteca):
    isbn = input("ISBN del libro: ")
    libro = biblioteca.buscar_libro_isbn(isbn)

    if libro is not None:
        return libro

    print(f"El libro con el isbn {isbn} no está en la biblioteca.")
    return None

def listar_libros(biblioteca):
    biblioteca.listar_libros()

def registrar_prestamo(biblioteca):
    iD_usuario = input("Insertar ID de usuario: ")
    isbn = input("Insertar isbn del libro a solicitar: ")
    usuario = biblioteca.buscar_usuario_id(iD_usuario)
    if usuario is None:
        print(f"No se ha encontrado el usuario con ID {iD_usuario}.")
        return
    
    libro = biblioteca.buscar_libro_isbn(isbn)
    if libro is None:
        print(f"No se ha encontrado el libro con ISBN {isbn}.")
        return

    fecha_prestamo = input("Fecha del préstamo (yyyy-mm-dd): ")
    prestamo_nuevo = Prestamo(usuario, libro, fecha_prestamo)

    biblioteca.registrar_prestamo(prestamo_nuevo)

def registrar_devolucion(biblioteca):
    iD_usuario = input("Insertar ID de usuario: ")
    isbn = input("Insertar isbn del libro a devolver: ")

    usuario = biblioteca.buscar_usuario_id(iD_usuario)
    if usuario is None:
        print(f"No se ha encontrado el usuario con ID {iD_usuario}.")
        return
    
    libro = biblioteca.buscar_libro_isbn(isbn)
    if libro is None:
        print(f"No se ha encontrado el libro con ISBN {isbn}.")
        return

    biblioteca.registrar_devolucion(usuario, libro)

def mostrar_prestamos_activos(biblioteca):
    biblioteca.mostrar_prestamos_activos()

def mostrar_prestamos_usuario(biblioteca):

    iD_usuario = input("ID del usuario del que quiere ver los préstamos: ")
    usuario = biblioteca.buscar_usuario_id(iD_usuario)
    
    if usuario is None:
        print(f"No se ha encontrado el usuario con ID {iD_usuario}.")
        return

    biblioteca.mostrar_prestamos_usuario(usuario)

def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Opción: ")

        if opcion == "1":
            registrar_libro(biblioteca)
        elif opcion == "2":
            registrar_usuario(biblioteca)
        elif opcion == "3":
            libro = buscar_libro(biblioteca)
            if libro is not None:
                print(libro)
        elif opcion == "4":
            listar_libros(biblioteca)
        elif opcion == "5":
            registrar_prestamo(biblioteca)
        elif opcion == "6":
            registrar_devolucion(biblioteca)
        elif opcion == "7":
            mostrar_prestamos_activos(biblioteca)
        elif opcion == "8":
            mostrar_prestamos_usuario(biblioteca)
        elif opcion == "9":
            pass
        elif opcion == "0":
            break
        else:
            print("OPCIÓN NO VÁLIDA.")

if __name__ == "__main__":
    main()