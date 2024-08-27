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



def principal():
    n_envios = 0
    archivo = open("envios-tp3.txt", "r")
    for i in archivo:
        for car in i:
            es_digito(car)
            es_mayuscula(car)

        if n_envios == 0:
            obtener_tipo_control(i)
        n_envios += 1

    print(n_envios)





if __name__ == '__main__':
    principal()
