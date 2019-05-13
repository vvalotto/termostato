"""

"""

class ActuadorClimatizador:

    @staticmethod
    def accionar_climatizador(accion):

        # Simula Actuador
        archivo_climatizador = open("climatizador", "w")
        archivo_climatizador.write(accion)
        archivo_climatizador.close()
        return
