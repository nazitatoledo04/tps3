from funciones import *
import os


def principal():
    vec = []
    tipo_control = "HC"
    op = -1
    band1 = True

    while op != 0:
        menu()
        print("")
        op = int(input("ingrese opción a cargar: "))

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
            calcular_importe_acumulado(vec, tipo_control)

        elif op == 8:
            mayor_importe(vec, tipo_control)

        elif op == 9:
            calcular_promedio(vec, tipo_control)

        elif op == 0:
            print("Gracias por usar nuestro menu, vuelva pronto")

        else:
            print("Opcion Invalida")


if __name__ == '__main__':
    principal()
