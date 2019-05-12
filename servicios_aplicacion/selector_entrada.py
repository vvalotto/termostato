"""

"""
from agentes_sensores.proxy_seteo_temperatura import *
from agentes_sensores.proxy_selector_temperatura import *
from gestores_entidades.gestor_ambiente import *


class SelectorEntradaTemperatura:

    def __init__(self, gestor_ambiente):
        self._seteo_temperatura = SeteoTemperatura()
        self._selector_temperatura = SelectorTemperatura()
        self._gestor_ambiente = gestor_ambiente
        return

    def ejecutar(self):
        # ver si seleccion para setear temperatura
        # si se setea temperatura
        #    muestra temperatura deseadead
        #    espera seteo

        while self._selector_temperatura.obtener_selector() == "deseada":
            self._gestor_ambiente.indicar_temperatura_a_mostrar = "deseada"
            self._gestor_ambiente.mostrar_temperatura()
            if self._seteo_temperatura.obtener_seteo() == "aumentar":
                self._gestor_ambiente.aumentar_temperatura_deseada()
            if self._seteo_temperatura.obtener_seteo() == "disminuir":
                self._gestor_ambiente.disminuir_temperatura_deseada()
        return

