"""

"""

from entidades.climatizador import *
from gestores_entidades.gestor_ambiente import *


class GestorClimatizador:

    def __init__(self):
        self._climatizador = Climatizador()
        return

    def definir_accion(self, gestor_ambiente):
        accion = "Nada"
        #leer temperatura ambiente
        #leer temperatura desaeda
        #Que hago?
        return accion

    def accionar_climatizador(self, accion):
        #mandar al proxy
        self._climatizador.proximo_estado(accion)
        return

    def obtener_estado_climatizador(self):
        return

    def mostrar_estado_climatizador(self):
        return
