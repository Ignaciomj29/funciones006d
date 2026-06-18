#funciones
#opcion 2: Buscar mascota
def buscar_mascota(lista_m, nombre_m):
    #recorrer y devolver la posicion
    for i in range(len(lista_m)):
        if lista_m[i]["nombre"] == nombre_m:
            return i #retorno la posicion
    return -1 #se termino el ciclo por tanto no se encontro

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
#opcion 4
def actualizar_vacunas(lista_m):
    for m in lista_m:
        #preguntamos por la edad para validar
        if m["edad"] >= 1:
            m["vacunada"] = True
        else:
            m["vacunada"] = False
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
        print("**** Buscar mascota ****")
        #solicitar el nombre de la mascota a buscar
        nom = input("Ingrese el nombre de la mascota a buscar:\n")
        posicion = buscar_mascota(datos_mascotas, nom)
        if posicion != -1:
            #guardar en un variable el diccionario de la mascota en la posicion de la lista
            m = datos_mascotas[posicion]
            print(f"Mascota encontrada en la posicion: {posicion}")
            print(f"Nombre mascota: {m['nombre']}")
            print(f"Especie mascota: {m['especie']}")
            print(f"Edad mascota: {m['edad']}")
            print(f"Vacunada: {m['vacunada']}")
        else:
            print(f"No se encontro la mascota con el nombre: {nom}")
    elif op == 3:
        print("**** Eliminar mascota ****")
        #solicitar el nombre de la mascota a buscar
        nom = input("Ingrese el nombre de la mascota a eliminar:\n")
        posicion = buscar_mascota(datos_mascotas, nom)
        if posicion != -1:
            #procedemos a eliminarla
            datos_mascotas.pop(posicion)
            print("Mascota eliminada correctamente")
        else:
            print(f"La mascota '{nom}' no se encuentra registrada")
    elif op == 4:
        actualizar_vacunas(datos_mascotas)
        print("Estado de vacunas actualizadas")
    elif op == 5:
        #actualizar el estado de las vacunas
        actualizar_vacunas(datos_mascotas)
        #mostrar sus datos
        if len(datos_mascotas) == 0:
            print("No hay datos en la lista")
        else:
            print("== Lista de Mascotas ==")
            for m in datos_mascotas:
                print(f"Nombre mascota: {m['nombre']}")
                print(f"Especie mascota: {m['especie']}")
                print(f"Edad mascota: {m['edad']}")
                #variable para cambiar el valor de vacunada
                estado = "AL DIA" if m["vacunada"] else "PENDIENTE"
                print(f"Estado vacuna: {estado}")
    elif op == 6:
        print("Gracias por usar el sistema.Vuelva pronto")