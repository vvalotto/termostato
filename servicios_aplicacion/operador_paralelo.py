"""

"""

import time
import threading


from gestores_entidades.gestor_bateria import *
from gestores_entidades.gestor_ambiente import *
from gestores_entidades.gestor_climatizador import *
from servicios_aplicacion.presentador import *


class Operador:

    def __init__(self):
        self._gestor_bateria = GestorBateria()
        self._gestor_ambiente = GestorAmbiente()
        self._gestor_climatizador = GestorClimatizador()
        self._presentador = Presentador(self._gestor_bateria,
                                        self._gestor_ambiente,
                                        self._gestor_climatizador)

    def lee_carga_bateria(self):
        while True:
            print("lee_bateria")
            self._gestor_bateria.verificar_nivel_de_carga()
            time.sleep(2)
        return

    def lee_temperatura_ambiente(self):
        while True:
            print("lee temperatura")
            self._gestor_ambiente.leer_temperatura_ambiente()
            self._gestor_ambiente.ambiente.temperatura_deseada = 20
            time.sleep(2)
        return

    def acciona_climatizador(self):
        while True:
            print("acciona climatizador")
            self._gestor_climatizador.accionar_climatizador(self._gestor_ambiente.ambiente)
            time.sleep(5)
        return

    def muestra_parametros(self):
        while True:
            self._presentador.ejecutar()
            time.sleep(5)
        return

    def ejecutar(self):


        print("inicio")

        t1 = threading.Thread(target=self.lee_carga_bateria)

        t2 = threading.Thread(target=self.lee_temperatura_ambiente)

        t3 = threading.Thread(target=self.acciona_climatizador)

        t4 = threading.Thread(target=self.muestra_parametros)

        t1.start()
        t2.start()
        time.sleep(10)
        t3.start()
        time.sleep(1)
        t4.start()

        return

