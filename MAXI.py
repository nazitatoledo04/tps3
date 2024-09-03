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


def calcular_importe(tipo, cp, pago):
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
    if len(vec) == 0:
        print("No hay envíos cargados para mostrar.")
        return

    print("=" * 80)
    print(f"{'| Código Postal |':^15}{'Dirección Física':^25}{'| Tipo de Envío |':^15}{'Forma de Pago |':^15}")
    print("=" * 80)

    for envio in vec:
        print(f"{envio.cod:^15}{envio.direc:^25}{envio.tipo:^15}{envio.form:^15}")

    print("=" * 80)
    print(f"Total de envíos: {len(vec)}")



def mostrar_arreglo_shellsort(vec): #PUNTO 3    PUNTO 3     PUNTO 3     PUNTO 3 PUNTO 3    PUNTO 3     PUNTO 3     PUNTO 3 PUNTO 3    PUNTO 3     PUNTO 3     PUNTO 3
    if len(vec) == 0:
        print("No hay envíos cargados para mostrar.")
        return
    vec = ordenar_codigo_postal(vec)
    opcion = input("¿Desea mostrar todos los registros o solo los primeros m? (todos/m): ")
    if opcion == "m":
        m = int(input("Ingrese el número de registros a mostrar: "))
        if m > len(vec):
            m = len(vec)
    else:
        m = len(vec)

    print("=" * 90)
    print(f"{'| Código Postal |':^15}{'Dirección Física':^25}{'| Tipo de Envío |':^20}{'Forma de Pago |':^15}{'País':^15}{'|':^0}")
    print("=" * 90)

    for i in range(m):
        envio = vec[i]
        pais = obtener_paises(envio.cod)
        print(f"{envio.cod:^15}{envio.direc:^25}{envio.tipo:^15}{envio.form:^20}{pais:^15}")

    return


def menu():
    print("-- Menu de Opciones --")
    print("1. Crear el arreglo de registros desde el archivo de texto (Elimina los registros previos).")
    print("2. Cargar datos de un envío manualmente y agregar al arreglo (Mantiene registros previos).")
    print("3. Mostrar todos los registros ordenados por código postal (opción de mostrar solo los primeros m).")
    print("4. Buscar un registro por dirección y tipo de envío.")
    print("5. Buscar un registro por código postal y cambiar la forma de pago.")
    print("6. Determinar cantidad de envíos por tipo de envío (dependiendo del tipo de control).")
    print("7. Determinar el importe acumulado por tipo de envío (dependiendo del tipo de control).")
    print("8. Mostrar tipo de envío con mayor importe acumulado y su porcentaje del total.")
    print("9. Calcular el importe promedio y cantidad de envíos por debajo del promedio.")
    print("0. Salir")

def ordenar_codigo_postal(vec):
    n = len(vec)
    medio = n // 2
    while medio > 0:
        for i in range(medio, n):
            temp = vec[i]
            j = i
            while j >= medio and vec[j - medio].cod > temp.cod:
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


def buscar_envio_por_direccion_y_tipo(vec): #PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4 PUNTO 4
    if len(vec) == 0:
        print("No hay envíos cargados para buscar.")
        return

    direccion_buscar = input("Ingrese la Dirección de Envío a buscar: ")
    tipo_envio_buscar = int(input("Ingrese el Tipo de Envío a buscar (ENTRE 0 Y 6): "))

    print("=" * 80)
    print(f"{'| Código Postal |':^15}{'Dirección Física':^25}{'| Tipo de Envío |':^15}{'Forma de Pago':^15}")
    print("=" * 80)

    for envio in vec:
        if envio.direc == direccion_buscar and envio.tipo == tipo_envio_buscar:

            print(f"{envio.cod:^15}{envio.direc:^25}{envio.tipo:^15}{envio.form:^15}")
            print("=" * 80)
            print("Registro encontrado.")
            return

    print("No se encontró ningún envío con la dirección y tipo de envío especificados.")
    print("=" * 80)

def cambiar_forma_pago(vec): # PUNTO 5-------------------------PUNTO 5-------------------------PUNTO 5-------------------------PUNTO 5-------------------------PUNTO 5
    if len(vec) == 0:
        print("No hay envíos cargados para modificar.")
        return

    cp_buscar = input("Ingrese el Código Postal del envío a modificar: ")

    print("=" * 80)
    print(f"{'| Código Postal |':^15}{'Dirección Física':^25}{'| Tipo de Envío |':^15}{'Forma de Pago':^15}")
    print("=" * 80)

    for envio in vec:
        if envio.cod == cp_buscar:
            if envio.form == 1:
                envio.form = 2
            else:
                envio.form = 1

            print(f"{envio.cod:^15}{envio.direc:^25}{envio.tipo:^15}{envio.form:^15}")
            print("=" * 80)
            print("Registro Encontrado - Forma de pago modificada con éxito.")
            return

    print("No se encontró ningún envío con el código postal especificado.")
    print("=" * 80)


def contar_envios_por_tipo(vec, tipo_control):
    # PUNTO 6------PUNTO 6 PUNTO 6------PUNTO 6 PUNTO 6------PUNTO 6 PUNTO 6------PUNTO 6PUNTO 6------PUNTO 6
    conteo_envios = [0] * 7
    for envio in vec:
        direccion_valida = es_direccion_valida(envio.direc)
        if tipo_control == "HC" and direccion_valida:
            conteo_envios[envio.tipo] += 1
        elif tipo_control == "SC":
            conteo_envios[envio.tipo] += 1

    print("Conteo de envíos por tipo:")
    for tipo in range(len(conteo_envios)):
        print("Tipo " + str(tipo) + ": " + str(conteo_envios[tipo]))

    return conteo_envios


def es_direccion_valida(direccion):  # PUNTO 6------PUNTO 6 PUNTO 6------PUNTO 6 PUNTO 6------PUNTO 6 PUNTO 6------PUNTO 6PUNTO 6------PUNTO 6
    return len(direccion) <= 20


def calcular_importe_acumulado(vec, tipo_control):
    # -------------PUNTO 7-------------PUNTO 7-------------PUNTO 7-------------PUNTO 7-------------PUNTO 7
    importe_acumulado = [0] * 7
    for envio in vec:
        direccion_valida = es_direccion_valida(envio.direc)
        if tipo_control == "HC" and direccion_valida:
            importe_acumulado[envio.tipo] += calcular_importe(envio.tipo, envio.cod, envio.form)
        elif tipo_control == "SC":
            importe_acumulado[envio.tipo] += calcular_importe(envio.tipo, envio.cod, envio.form)

    print("Importe acumulado por tipo de envío:")
    for tipo in range(len(importe_acumulado)):
        print("Tipo " + str(tipo) + ": " + str(importe_acumulado[tipo]))

    return importe_acumulado


def mayor_importe(vec, tipo_control): # -------------PUNTO 8-------------PUNTO 8-------------PUNTO 8-------------PUNTO 8-------------PUNTO 8
    importe_acumulado = calcular_importe_acumulado(vec, tipo_control)
    
    max_importe = importe_acumulado[0]
    mayor_importe = 0
    
    for i in range (1, len(importe_acumulado)):
        if importe_acumulado[i] > max_importe:
            max_importe = importe_acumulado[i]
            mayor_importe = i
            
    importe_total = 0
    for i in importe_acumulado:
        importe_total += i
        
    porcentaje = (max_importe / importe_total) * 100 if importe_total != o else 0
    
    print(f"Tipo de envío con mayor importe acumulado: {mayor_importe}")
    print(f"Importe acumulado: ${max_importe:.2f}")
    print(f"Porcentaje del total: {porcentaje:.2f}%")
def calcular_promedio(vec, tipo_control): # -------------PUNTO 9-------------PUNTO 9-------------PUNTO 9-------------PUNTO 9-------------PUNTO 9
   pass

def principal():
    vec = []
    tipo_control = "HC"
    op = -1
    band1 = True

    while op != 0:
        menu()
        print("")
        op = int(input("ingrese opcion a cargar: "))

        if op == 1:

            if band1:
                vec, tipo_control = agregar_envio(vec)
                band1 = False

            else:
                eliminar_arreglo = input("Desea Eliminar el Arreglo? (S/N) ")

                if eliminar_arreglo.lower() == "s":
                    vec = []
                    print("ARREGLO ELIMINADO")

        elif op == 2:

            if band1:
                vec, tipo_control = agregar_envio(vec)
                vec = agregar_envio_manual(vec)

            else:
                vec = agregar_envio_manual(vec)

            mostrar_arreglo(vec)

        elif op == 3:

            if len(vec) > 0:
                vec = ordenar_codigo_postal(vec)
                mostrar_arreglo_shellsort(vec)
            else:
                print("No hay envíos para mostrar.")

        elif op == 4:
            buscar_envio_por_direccion_y_tipo(vec)

        elif op == 5:
            cambiar_forma_pago(vec)

        elif op == 6:
            contar_envios_por_tipo(vec, tipo_control)

        elif op == 7:
            calcular_importe_acumulado(vec,tipo_control)

        elif op == 8:
            mayor_importe(vec, tipo_control)

        elif op == 9:
            pass

        elif op == 0:
            print("Gracias por usar nuestro menu, vuelva pronto")

        else:
            print("Opcion Invalida")


if __name__ == '__main__':
    principal()
