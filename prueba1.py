#funciones
def mostrar_menu():
    print("=============================")
    print("|| 1.- Agregar mascota      ||")
    print("|| 2.- Buscar mascota       ||")
    print("|| 3.- Eliminar mascota     ||")
    print("|| 4.- Marcar como vacunada ||")
    print("|| 5.- Mostrar mascota      ||")
    print("|| 6.- Salir                ||")
    print("=============================")

def solicitar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion:\n"))
            if opcion < 1 or opcion > 6:
                print("Debe seleccionar una opcion del 1 al 6")
            else:
                break
        except ValueError:
            print("Debe ingresar un numero")
    return opcion

#codigo principal
#declarar la lista de mascotas
datos_mascotas = []
op = 0
while op != 6:
    mostrar_menu()
    op = solicitar_opcion()