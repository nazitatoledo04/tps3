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

    return "No anduvo"


def es_mayuscula(car):
    return 'A' <= car <= 'Z'


def es_digito(car):
    return '0' <= car <= '9'


def agregar_envio(vec):
    codigo_postal = input("")
    direccion_fis = input("")
    tipo_envio = int(input())
    forma_pago = int(input())
    envio = Envios(codigo_postal, direccion_fis, tipo_envio, forma_pago)
    vec.append(envio)
    print("Envio Agregado con exitos!")


def mostrar_arreglo(vec):
    if len(vec) == 0:
        print("No Hay Envios Cargados")
    else:
        for envio in vec:
            print("Codigo Postal: ", envio.codigo_postal, "Direccion Fisica: ", envio.codigo_postal, "Tipo de Envio: ",
                  envio.codigo_postal, "Forma De Pago: ", envio.codigo_postal)


def menu():
    print("Menu de opciones:")
    print("1-Agregar Envio")
    print("2-Mostrar Envios")
    print("3-Buscar Envios")
    print("4-Eliminar Envio")
    print("5-Salir")
    opcion = int(input("Ingrese Opcion: "))
    

def principal():
    vec = []
    n_envios = 0
    archivo = open("envios-tp3.txt", "r")
    for i in archivo:
        for car in i:
            es_digito(car)
            es_mayuscula(car)
            opcion= menu()
            if opcion == 1:
                pass
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                break
            else:
                print("Opcion Invalida")
        if n_envios == 0:
            obtener_tipo_control(i)
        n_envios += 1
    print(n_envios)

        

if __name__ == '__main__':
    principal()
