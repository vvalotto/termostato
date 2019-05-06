""""

"""
from gestores_entidades.gestor_bateria import *
from agentes_actuadores.visualizador_bateria import *

if __name__ == "__main__":
    gestor = GestorBateria()
    gestor.verificar_nivel_de_carga()
    gestor.mostrar_nivel_de_carga()
    gestor.mostrar_indicador_de_carga()