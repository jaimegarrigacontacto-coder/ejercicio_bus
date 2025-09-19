from Billete import Billete

class Bus():
    def __init__(self, asientosLibres, asientosOcupados, identificador, billete):
        setAsientosLibres(asientosLibres)
        setAsientosOcupados(asientosOcupados)
        setIdentificador(identificador)
        setBillete(billete)

    def getAsientosLibres(self):
        return self.__asientosLibres

    def setAsientosLibres(self, asientos):
        self.__asientosLibres = asientos

    def getAsientosOcupados(self):
        return self.__asientosOcupados

    def setAsientosOcupados(self, asientos):
        self.__asientosOcupados = asientos

    def getIdentificador(self):
        return self.__identificador

    def setIdentificador(self, identificador):
        self.__identificador = identificador

    def getBillete(self):
        return self.__billete

    def setBillete(self, billete):
        self.__billete = billete

