from envios import *


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
    forma_pago = int(input("Ingrese Forma De Pago (1 o 2): "))
    envio = Envios(codigo_postal, direccion_fis, tipo_envio, forma_pago)
    vec.append(envio)
    print("Envio Agregado con exitos!")


def agregar_envio(vec):
    archivo = open("envios-tp3.txt", "r")
    m = archivo.read()
    n_envios = 0
    for i in archivo:
        if n_envios >= 1:
            cp = i[0:9].strip()
            direccion = i[9:29].strip()
            tipo = i[29].strip()
            pago = i[30].strip()
        for car in i:
            es_digito(car)
            es_mayuscula(car)

        if n_envios == 0:
            obtener_tipo_control(i)
        n_envios += 1

    codigo_postal = cp
    direccion_fis = direccion
    tipo_envio = tipo
    forma_pago = pago
    envio = Envios(codigo_postal, direccion_fis, tipo_envio, forma_pago)
    vec.append(envio)
    m.close
    print("Envio Agregado con exitos!")


def mostrar_arreglo(vec):
    if len(vec) == 0:
        print("No Hay Envios Cargados")
    else:
        for envio in vec:
            print("Codigo Postal: ", envio.codigo_postal, "Direccion Fisica: ", envio.codigo_postal, "Tipo de Envio: ",
                  envio.codigo_postal, "Forma De Pago: ", envio.codigo_postal)


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


def principal():
    vec = []
    opcion = 0
    opcion = menu()
    while opcion != 0:

        if opcion == 1:
            if len(vec) > 0:
                vec = agregar_envio(vec)
            else:
                eliminar_arreglo = input("Desea Eliminar el Arreglo? (S/N) ")
                eliminar_arreglo.lower()
                if eliminar_arreglo == "s":
                    vec = agregar_envio_manual(vec)
                elif eliminar_arreglo == "n":
                    opcion = menu()

        elif opcion == 2:
            if len(vec) > 0:
                mostrar_arreglo(vec)
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
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
