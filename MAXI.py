from envios import *
import os

def obtener_tipo_control(linea):
    anterior = ""
    for i in linea:
        if i == "c" or i == "C":
            if anterior == "h" or anterior == "H":
                print("Hard Control")
                return "HC"
            if anterior == "s" or anterior == "S":
                print("Soft Control")
                return "SC"
        anterior = i
    return "HC"


def es_mayuscula(car):
    return 'A' <= car <= 'Z'


def es_digito(car):
    return '0' <= car <= '9'


def solo_digit(car):
    for caracter in car:
        if not ('0' <= caracter <= '9'):
            return False
    return True


def calcular_importe(tipo, cp, pago): # PUNTO 7-------------PUNTO 7-------------PUNTO 7-------------PUNTO 7-------------PUNTO 7
    precio = 0
    tipo = int(tipo)
    region = obtener_paises(cp)
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
    tipo_control = "HC"
    for i in archivo:
        if n_envios == 0:
            tipo_control = obtener_tipo_control(i)
        else:
            if len(i) >= 31:
                cp = i[0:9].strip()
                direccion = i[9:29].strip()
                tipo = int(i[29])
                pago = int(i[30])

                envio = Envios(cp, direccion, tipo, pago)
                vec.append(envio)

        n_envios += 1

    archivo.close()
    print("Envios cargados con éxito desde el archivo!")
    return vec, tipo_control

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

def obtener_paises(cp):  # PUNTO 3    PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3 PUNTO 3
    pais = ""
    provincia = ""
    region = 0
    if len(cp) == 9 and cp[0].isalpha():
        if cp[1].isdigit() and cp[2].isdigit() and cp[3].isdigit() and cp[4].isdigit():
            if cp[5].isalpha() and cp[6].isalpha() and cp[7].isalpha():
                pais = "Argentina"
                provincia = cp[0]
                if provincia == "A":
                    region = 1
                elif provincia == "B":
                    region = 2
                elif provincia == "C":
                    region = 3
                elif provincia == "D":
                    region = 4
                elif provincia == "E":
                    region = 5
                elif provincia == "F":
                    region = 6
                elif provincia == "G":
                    region = 7
                elif provincia == "H":
                    region = 8
                elif provincia == "J":
                    region = 9
                elif provincia == "K":
                    region = 10
                elif provincia == "L":
                    region = 11
                elif provincia == "M":
                    region = 12
                elif provincia == "N":
                    region = 13
                elif provincia == "P":
                    region = 14
                elif provincia == "Q":
                    region = 15
                elif provincia == "R":
                    region = 16
                elif provincia == "S":
                    region = 17
                elif provincia == "T":
                    region = 18
                elif provincia == "U":
                    region = 19
                elif provincia == "V":
                    region = 20
                elif provincia == "W":
                    region = 21
                elif provincia == "X":
                    region = 22
                elif provincia == "Y":
                    region = 23
                elif provincia == "Z":
                    region = 24
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

    return pais or region

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

def contar_envios_por_tipo(vec, tipo_control): #PUNTO 6------PUNTO 6 PUNTO 6------PUNTO 6 PUNTO 6------PUNTO 6 PUNTO 6------PUNTO 6PUNTO 6------PUNTO 6
    conteo_envios = [0] * 7
    for envio in vec:
        direccion_valida = es_direccion_valida(envio.direccion_fis)
        if tipo_control == "HC" and direccion_valida:
            conteo_envios[envio.tipo_envio] += 1
        elif tipo_control == "SC":
            conteo_envios[envio.tipo_envio] += 1

    print("Conteo de envíos por tipo:", conteo_envios)
    return conteo_envios


def es_direccion_valida(direccion): #PUNTO 6------PUNTO 6 PUNTO 6------PUNTO 6 PUNTO 6------PUNTO 6 PUNTO 6------PUNTO 6PUNTO 6------PUNTO 6
    return len(direccion) <= 20

def calcular_importe_acumulado(vec, tipo_control): # -------------PUNTO 7-------------PUNTO 7-------------PUNTO 7-------------PUNTO 7-------------PUNTO 7
    importe_acumulado = [0] * 7
    for envio in vec:
        direccion_valida = es_direccion_valida(envio.direccion_fis)
        if tipo_control == "HC" and direccion_valida:
            importe_acumulado[envio.tipo_envio] += calcular_importe(envio.tipo_envio, envio.codigo_postal, envio.forma_pago)
        elif tipo_control == "SC":
            importe_acumulado[envio.tipo_envio] += calcular_importe(envio.tipo_envio, envio.codigo_postal, envio.forma_pago)

    print("Importe acumulado por tipo de envío:", importe_acumulado)
    return importe_acumulado

def principal():
    vec = []
    opcion = menu()
    tipo_control = "HC"
    while opcion != 0:
        if opcion == 1:
            if len(vec) == 0:
                vec, tipo_control = agregar_envio(vec)
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
            contar_envios_por_tipo(vec, tipo_control)
            opcion = menu()
        elif opcion == 7:
            calcular_importe_acumulado(vec,tipo_control)
            menu()
        elif opcion == 8:
            pass
            opcion = menu()
        elif opcion == 9:
            pass
            opcion = menu()
        elif opcion == 0:
            break
        else:
            print("Opcion Invalida")
            opcion = menu()


if __name__ == '__main__':
    principal()
