class Envios:
    def __init__(self, codigo_postal, direccion_fis, tipo_envio, forma_pago):
        self.cod = codigo_postal
        self.direc = direccion_fis
        self.tipo = tipo_envio
        self.form = forma_pago

    def string(self):
        return self.cod + "," + self.direc + "," + self.tipo + "," + self.form