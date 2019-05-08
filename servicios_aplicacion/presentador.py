"""
Clase que expone o visualiza los parametros al usuario
"""


class Presentador():

    def __init__(self, gestor_bateria,
                 gestor_ambiente
                 ):
        self._gestor_bateria = gestor_bateria
        self._gestor_ambiente = gestor_ambiente
        return

    def ejecutar(self):
        self._gestor_bateria.mostrar_nivel_de_carga()
        self._gestor_ambiente.mostrar_temperatura_ambiente()
        return
