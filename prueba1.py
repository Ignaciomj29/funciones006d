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
#fuciones de validaciones
def validar_nombre(name):
    #strip() -> sirve para eliminar todos los espacios en blanco al inicio y al final de un string
    #retorna True si es valido o False si no
    return name.strip() != ""

def validar_especie(especie):
    especies_validas = ["perro", "gato", "ave"]
    #retorna True si lo consigue o False si no
    return especie.strip().lower() in especies_validas

def validar_edad(edad):
    #isdigit() -> revisa si un string contiene solo digitos
    return edad.isdigit() and int(edad) > 0


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
#Funcion para la opcion 1
def agregar_mascota(lista_m):
    #solicitamos los datos
    nombre = input("Ingrese el nombre de la mascota:\n")
    correcta = validar_nombre(nombre)
    if not correcta:
        print("El nombre no puede estar en blanco")
        return
    especie = input("Ingrese la especie (perro,gato o ave):\n")
    correcta = validar_especie(especie)
    if not correcta:
        print("La especie solo puede ser perro, gato o ave")
        return
    edad = input("Ingrese la edad de la mascota:\n")
    correcta = validar_edad(edad)
    if not correcta:
        print("La edad debe ser un numero entero mayor a cero")
        return
    #agregar los datos al diccionario
    mascota = {
        "nombre": nombre.strip(),
        "especie": especie.strip(),
        "edad": int(edad),
        "vacunada": False
    }
    lista_m.append(mascota)
    print("Mascota agregada correctamente")
#codigo principal
#declarar la lista de mascotas
datos_mascotas = []
op = 0
while op != 6:
    mostrar_menu()
    op = solicitar_opcion()

    if op == 1:
        agregar_mascota(datos_mascotas)
    elif op == 2:
        print("")
    elif op == 3:
        print("")
    elif op == 4:
        print("")
    elif op == 5:
        print("")
    elif op == 6:
        print("Gracias por usar el sistema.Vuelva pronto")