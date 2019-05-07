""""

"""

import time


from gestores_entidades.gestor_bateria import *
from gestores_entidades.gestor_sensor_temperatura import *


class Operador():

    def __init__(self):
        self._gestor_bateria = GestorBateria()
        self._gestor_sensor_temperatura = GestorSensorTemperatura()
        return

    def ejecutar(self):

        while True:

            self._gestor_bateria.verificar_nivel_de_carga()
            self._gestor_bateria.mostrar_nivel_de_carga()
            self._gestor_bateria.mostrar_indicador_de_carga()
            time.sleep(2)
            self._gestor_sensor_temperatura.leer_temperatura_ambiente()
            self._gestor_sensor_temperatura.mostrar_temperatura_ambiente()
            time.sleep(2)

        return

