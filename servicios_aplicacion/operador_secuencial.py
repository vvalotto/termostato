import time
from gestores_entidades.gestor_bateria import *
from gestores_entidades.gestor_ambiente import *
from gestores_entidades.gestor_climatizador import *
from servicios_aplicacion.selector_entrada import *
from servicios_aplicacion.presentador import *

class Operador:

    def __init__(self):
        self._gestor_bateria = GestorBateria()
        self._gestor_ambiente = GestorAmbiente()
        self._gestor_climatizador = GestorClimatizador()
        self._selector = SelectorEntradaTemperatura(self._gestor_ambiente)
        self._presentador = Presentador(self._gestor_bateria,
                                        self._gestor_ambiente,
                                        self._gestor_climatizador)

    def ejecutar(self):

        print("inicio")

        self._gestor_ambiente.ambiente.temperatura_deseada = 23

        while True:
            print("lee_bateria")
            self._gestor_bateria.verificar_nivel_de_carga()
            time.sleep(1)

            print("lee temperatura")
            self._gestor_ambiente.leer_temperatura_ambiente()
            time.sleep(1)

            print("revisa selector de temperatura")
            self._selector.ejecutar()
            time.sleep(1)

            print("acciona climatizador")
            self._gestor_climatizador.accionar_climatizador(self._gestor_ambiente.ambiente)
            time.sleep(1)

            print("Muestra estado")
            self._presentador.ejecutar()
            time.sleep(5)

        return