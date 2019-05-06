"""

"""

from agentes_sensores.proxy_bateria import *
from agentes_actuadores.visualizador_bateria import *
from entidades.bateria import *


class GestorBateria:

    def __init__(self):
        self._bateria = Bateria()
        self._proxy_bateria = ProxyBateria()
        self._visualizador_bateria = VisualizadorBateria()
        return

    def verificar_nivel_de_carga(self):
        self._bateria.nivel_de_carga = self._proxy_bateria.leer_carga()
        return

    def obtener_nivel_de_carga(self):
        return self._bateria.nivel_de_carga

    def mostrar_nivel_de_carga(self):
        self._visualizador_bateria.mostrar_tension(self._bateria.nivel_de_carga)
        return

    def mostrar_indicador_de_carga(self):
        self._visualizador_bateria.mostrar_indicador(self._bateria.indicador)