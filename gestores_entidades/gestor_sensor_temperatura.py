"""

"""

from agentes_sensores.proxy_sensor_temperatura import *
from entidades.ambiente import *


class GestorSensorTemperatura:

    def __init__(self):
        self._ambiente = Ambiente()
        self._proxy_sensor_temperatura = ProxySensorTemperatua()
        return

    def leer_temperatura_ambiente(self):
        self._ambiente.temperatura_ambiente = self._proxy_sensor_temperatura.leer_temperatura()
        return

    def obtener_temperatura_ambiente(self):
        return self._ambiente.temperatura_ambiente

    def mostrar_temperatura_ambiente(self):
        print("Temperatura ambiente")
        return

    def poner_temperatura_deseada(self):
        return

    def obtener_temperatura_deseada(self):
        return

    def mostrar_temperatura_deseada(self):
        return
