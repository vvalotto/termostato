"""
Clase que llamaria a la lectura de la interfaz de lectura
del sensor de temperatura
"""


class ProxySensorTemperatura():

    def leer_temperatura(self):
        '''
        Aqui lee desde la GPIO el valor que indica la bateria
        :return:
        '''
        error = True
        temperatura = 25
        if error is True:
            raise Exception("Error de Lectura de Sensor")
        return temperatura