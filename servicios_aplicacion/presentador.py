"""
Clase que expone o visualiza los parametros al usuario
"""


class Presentador:

    def __init__(self, gestor_bateria,
                 gestor_ambiente,
                 gestor_climatizador
                 ):
        """
        Inyecta los gestores para que se visualicen
        los parámetros contenidos en las entidades que manejan
        :param gestor_bateria:
        :param gestor_ambiente:
        """
        self._gestor_bateria = gestor_bateria
        self._gestor_ambiente = gestor_ambiente
        self._gestor_climatizador = gestor_climatizador
        return

    def ejecutar(self):
        """
        Se sacan los valores de los parametros para que se
        muestren
        """
        self._gestor_bateria.mostrar_nivel_de_carga()
        self._gestor_ambiente.mostrar_temperatura()
        self._gestor_climatizador.mostrar_estado_climatizador()
        return
