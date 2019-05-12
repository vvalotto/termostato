"""
Clase que es la responsable de manejar la entidad Ambiente.
- Obteniendo la temperatura desde el sensor externo
- Aceptando la determinación de la temperatura deseeada
- mostrando las temperaturas en los dispositivos de visualizacion
"""

from agentes_sensores.proxy_sensor_temperatura import *
from agentes_sensores.proxy_selector_temperatura import *
from agentes_sensores.proxy_seteo_temperatura import *
from entidades.ambiente import *
from agentes_actuadores.visualizador_temperatura import *


class GestorAmbiente:

    @property
    def ambiente(self):
        return self._ambiente

    def __init__(self):
        self._ambiente = Ambiente()
        self._proxy_sensor_temperatura = ProxySensorTemperatura()
        self._visualizador_temperatura = VisualizadorTemperaturas()
        self._selector_temperatura = SelectorTemperatura()
        self._seteo_temperatura = SeteoTemperatura()
        return

    def leer_temperatura_ambiente(self):
        try:
            self._ambiente.temperatura_ambiente = self._proxy_sensor_temperatura.leer_temperatura()
        except Exception:
            self._ambiente.temperatura_ambiente = None
        return

    def obtener_temperatura_ambiente(self):
        return self._ambiente.temperatura_ambiente

    def mostrar_temperatura_ambiente(self):
        self._visualizador_temperatura.mostrar_temperatura_ambiente(self._ambiente.temperatura_ambiente)
        return

    def seleccionar_temperatura(self):
        self._ambiente.temperatura_a_mostrar = self._selector_temperatura.obtener_selector()
        if self._ambiente.temperatura_a_mostrar == "deseada":
            if self._seteo_temperatura.obtener_seteo() == "aumentar":
                self.aumentar_temperatura_deseada()
            if self._seteo_temperatura.obtener_seteo() == "disminuir":
                self.disminuir_temperatura_deseada()
        return

    def aumentar_temperatura_deseada(self):
        self._ambiente.temperatura_deseada = +1
        return

    def disminuir_temperatura_deseada(self):
        self._ambiente.temperatura_deseada = -1
        return

    def obtener_temperatura_deseada(self):
        return self._ambiente.temperatura_deseada

    def mostrar_temperatura_deseada(self):
        self._visualizador_temperatura.mostrar_temperatura_ambiente(self._ambiente.temperatura_deseada)
        return

    def mostrar_temperatura(self):
        if self._ambiente.temperatura_a_mostrar == "ambiente":
            self._visualizador_temperatura.mostrar_temperatura_ambiente(self._ambiente.temperatura_ambiente)
        elif self._ambiente.temperatura_a_mostrar == "deseada":
            self._visualizador_temperatura.mostrar_temperatura_ambiente(self._ambiente.temperatura_deseada)
        return

    def indicar_temperatura_a_mostrar(self, tipo_temperatura):
        self.ambiente.temperatura_a_mostrar = tipo_temperatura
        return

