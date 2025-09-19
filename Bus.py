from Billete import Billete

class Bus():
    def __init__(self, asientosLibres, asientosOcupados = 0, identificador, billetes = []):
        setAsientosLibres(asientosLibres)
        setAsientosOcupados(asientosOcupados)
        setIdentificador(identificador)
        setBilletes(billetes)

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

    def getBilletes(self):
        return self.__billetes

    def setBilletes(self, billetes):
        self.__billetes = billetes

    def ventaBilletes():
        

    def devolucionBilletes():
        

    def estadoVenta():


