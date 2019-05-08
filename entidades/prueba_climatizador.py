from entidades.climatizador import *

if __name__ == "__main__":

    c = Climatizador()
    print(c.maquina_estado)
    print(c.proximo_estado("calentar"))
    print(c.proximo_estado("apagar"))
    print(c.proximo_estado("enfriar"))
    print(c.proximo_estado("apagar"))
