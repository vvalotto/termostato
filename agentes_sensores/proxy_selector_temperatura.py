"""

"""


class SelectorTemperatura:

    @staticmethod
    def obtener_selector():
        try:
            archivo = open("tipo_temp", "r")
            tipo_temperatura = archivo.read()
            archivo.close()
        except IOError:
            raise ("Error al leer el tipo de temperatura")
        return tipo_temperatura
