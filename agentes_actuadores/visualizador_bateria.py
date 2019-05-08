""""
Muestra los valores de carga de la Bateria
"""


class VisualizadorBateria:

    def mostrar_tension(self, tension_bateria):

        archivo = open("bateria", "a")
        archivo.write("la carga de la bateria es:")
        archivo.write(str(tension_bateria))
        archivo.write("\n")
        archivo.close()
        return

    def mostrar_indicador(self, indicador_bateria):
        print(indicador_bateria)
        return