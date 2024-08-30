from envios import *
import os

def obtener_tipo_control(linea):
    anterior = ""
    for i in linea:
        if i == "c" or i == "C":
            if anterior == "h" or anterior == "H":
                print("hard control")
                return "Hard Control"
            if anterior == "s" or anterior == "S":
                print("soft control")
                return "Soft Control"
        anterior = i


def es_mayuscula(car):
    return 'A' <= car <= 'Z'


def es_digito(car):
    return '0' <= car <= '9'


def solo_digit(car):
    for caracter in car:
        if not ('0' <= caracter <= '9'):
            return False
    return True


def calcular_importe(tipo, cp, pago):
    precio = 0
    tipo = int(tipo)
    if tipo == 0:
        precio = 1100
    elif tipo == 1:
        precio = 1800
    elif tipo == 2:
        precio = 2450
    elif tipo == 3:
        precio = 8300
    elif tipo == 4:
        precio = 10900
    elif tipo == 5:
        precio = 14300
    elif tipo == 6:
        precio = 17900

    if len(cp) == 9:
        region = int(cp[0])
        if region in (0, 1, 2, 3):
            precio *= 1.25
        elif region in (4, 5, 6, 7):
            precio *= 1.3
        else:
            precio *= 1.20
    else:
        precio *= 1.20

    if pago == 1:
        precio *= 0.90
    else:
        precio *= 1.5

    return precio


def agregar_envio_manual(vec):
    codigo_postal = input("Ingrese los 9 caracteres del Codigo Postal: ")
    direccion_fis = input("Ingrese Los 20 caracteres de la Direccion Fisica Del Destino: ")
    tipo_envio = int(input("Ingrese tipo de envio (Entre 0 y 6): "))
    while tipo_envio < 0 or tipo_envio > 6:
        tipo_envio = int(input("Error!!! Ingrese tipo de envio (Entre 0 y 6): "))
    forma_pago = int(input("Ingrese Forma De Pago (1 o 2): "))
    while forma_pago != 1 and forma_pago != 2:
        forma_pago = int(input("Error!!! Ingrese Forma De Pago (1 o 2): "))

    envio = Envios(codigo_postal, direccion_fis, tipo_envio, forma_pago)
    vec.append(envio)
    print("Envio Agregado con exitos!")
    return vec


def agregar_envio(vec):
    archivo = open("envios-tp3.txt", "rt")
    n_envios = 0
    for i in archivo:
        if n_envios == 0:
            obtener_tipo_control(i)
        else:
            if len(i) >= 31:
                cp = i[0:9].strip()
                direccion = i[9:29].strip()
                tipo = i[29].strip()
                pago = i[30].strip()

                envio = Envios(cp, direccion, tipo, pago)
                vec.append(envio)

        n_envios += 1

    archivo.close()
    print("Envios cargados con éxito desde el archivo!")
    return vec


def mostrar_arreglo(vec):
    for envio in vec:
        print("Codigo Postal: ", envio.codigo_postal, "Direccion Fisica: ", envio.direccion_fis, "Tipo de Envio: ",
              envio.tipo_envio, "Forma De Pago: ", envio.forma_pago)


def mostrar_arreglo_shellsort(vec): #PUNTO 3    PUNTO 3     PUNTO 3     PUNTO 3  
    encontrados = ""
    vec = ordenar_codigo_postal(vec)
    opcion = input("¿Desea mostrar todos los registros o solo los primeros m? (todos/m): ")
    if opcion == "m":
        m = int(input("Ingrese el número de registros a mostrar: "))
        if m > len(vec):
            m = len(vec)
    else:
        m = len(vec)

    for i in range(m):
        envio = vec[i]
        pais = obtener_paises(envio.codigo_postal)
        print("Codigo Postal: ", envio.codigo_postal, "Direccion Fisica: ", envio.direccion_fis, "Tipo de Envio: ",
              envio.tipo_envio, "Forma De Pago: ", envio.forma_pago, "Pais: ", pais)


    return


def menu():
    print("--Menu de opciones--")
    print("1. Agregar Envio")
    print("2. Mostrar Envios")
    print("3. Buscar Envios")
    print("4. Eliminar Envio")
    print("5. punto 5")
    print("6. punto 6")
    print("7. punto 7")
    print("8. punto 8")
    print("9. punto 9")
    print("0. Salir")
    return int(input("Ingrese Opcion: "))


def ordenar_codigo_postal(vec):
    n = len(vec)
    medio = n // 2
    while medio > 0:
        for i in range(medio, n):
            temp = vec[i]
            j = i
            while j >= medio and vec[j - medio].codigo_postal > temp.codigo_postal:
                vec[j] = vec[j - medio]
                j -= medio
            vec[j] = temp
        medio //= 2
    return vec

def obtener_paises(cp): #PUNTO 3    PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3
    pais = ""
    provincia = ""
    if len(cp) == 9 and cp[0].isalpha():
        if cp[1].isdigit() and cp[2].isdigit() and cp[3].isdigit() and cp[4].isdigit():
            if cp[5].isalpha() and cp[6].isalpha() and cp[7].isalpha():
                pais = "Argentina"

                if cp[0] == "A":
                    provincia = "Salta"
                elif cp[0] == "B":
                    provincia = "Provincia de Buenos Aires"
                elif cp[0] == "C":
                    provincia = "Ciudad Autónoma de Buenos Aires"
                elif cp[0] == "D":
                    provincia = "San Luis"
                elif cp[0] == "E":
                    provincia = "Entre Ríos"
                elif cp[0] == "F":
                    provincia = "La Rioja"
                elif cp[0] == "G":
                    provincia = "Santiago del Estero"
                elif cp[0] == "H":
                    provincia = "Chaco"
                elif cp[0] == "J":
                    provincia = "San Juan"
                elif cp[0] == "K":
                    provincia = "Catamarca"
                elif cp[0] == "L":
                    provincia = "La Pampa"
                elif cp[0] == "M":
                    provincia = "Mendoza"
                elif cp[0] == "N":
                    provincia = "Misiones"
                elif cp[0] == "P":
                    provincia = "Formosa"
                elif cp[0] == "Q":
                    provincia = "Neuquén"
                elif cp[0] == "R":
                    provincia = "Río Negro"
                elif cp[0] == "S":
                    provincia = "Santa Fe"
                elif cp[0] == "T":
                    provincia = "Tucumán"
                elif cp[0] == "U":
                    provincia = "Chubut"
                elif cp[0] == "V":
                    provincia = "Tierra del Fuego"
                elif cp[0] == "W":
                    provincia = "Corrientes"
                elif cp[0] == "X":
                    provincia = "Córdoba"
                elif cp[0] == "Y":
                    provincia = "Jujuy"
                elif cp[0] == "Z":
                    provincia = "Santa Cruz"
    elif len(cp) == 4 and cp[0].isdigit() and cp[1].isdigit() and cp[2].isdigit() and cp[3].isdigit():
        pais = "Bolivia"

    elif len(cp) == 5 and cp[0].isdigit() and cp[1].isdigit() and cp[2].isdigit() and cp[3].isdigit() and cp[4].isdigit():
        pais = "Uruguay"

    elif len(cp) == 6 and cp[0].isdigit() and cp[1].isdigit() and cp[2].isdigit() and cp[3].isdigit() and cp[4].isdigit() and cp[5].isdigit():
        pais = "Paraguay"

    elif len(cp) == 7 and cp[0].isdigit() and cp[1].isdigit() and cp[2].isdigit() and cp[3].isdigit() and cp[4].isdigit() and cp[5].isdigit() and cp[6].isdigit():
        pais = "Chile"

    elif len(cp) == 9 and cp[0].isdigit() and cp[1].isdigit() and cp[2].isdigit() and cp[3].isdigit() and cp[4].isdigit() and cp[5] == "-" and cp[6].isdigit() and cp[7].isdigit() and cp[8].isdigit():
        pais = "Brasil"
    else:
        pais = "Otro"

    return pais or provincia

def buscar_envio_por_direccion_y_tipo(vec): #PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4
    if len(vec) == 0:
        print("No hay envíos cargados para buscar.")
        return
    direccion_buscar = input("Ingrese la Dirección de Envío a buscar: ")
    tipo_envio_buscar = int(input("Ingrese el Tipo de Envío a buscar (ENTRE 0 Y 6): "))

    for envio in vec:
        if envio.direccion_fis == direccion_buscar and envio.tipo_envio == tipo_envio_buscar:
            print("Registro encontrado:")
            print("Codigo Postal: ", envio.codigo_postal, "Direccion Fisica: ", envio.direccion_fis, "Tipo de Envio: ",
                  envio.tipo_envio, "Forma De Pago: ", envio.forma_pago)
            return

    print("No se encontró ningún envío con la dirección y tipo de envío especificados.")


def principal():
    vec = []
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            if len(vec) == 0:
                vec = agregar_envio(vec)
            eliminar_arreglo = input("Desea Eliminar el Arreglo? (S/N) ")
            if eliminar_arreglo.lower() == "s":
                vec = []
                print("ARREGLO ELIMINADO")
            opcion = menu()

        elif opcion == 2:
            vec = agregar_envio_manual(vec)
            mostrar_arreglo(vec)
            opcion = menu()

        elif opcion == 3:
            if len(vec) > 0:
                vec = ordenar_codigo_postal(vec)
                mostrar_arreglo_shellsort(vec)
            else:
                print("No hay envíos para mostrar.")
            opcion = menu()

        elif opcion == 4:
            buscar_envio_por_direccion_y_tipo(vec)
            opcion = menu()
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:
            pass
        elif opcion == 9:
            pass
        elif opcion == 0:
            break
        else:
            print("Opcion Invalida")
            opcion = menu()


if __name__ == '__main__':
    principal()
