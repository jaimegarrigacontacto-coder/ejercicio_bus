from Billete import Billete

class Bus():
    def __init__(self, asientosLibres, asientosOcupados = 0, billetes = []):
        self.setAsientosLibres(asientosLibres)
        self.setAsientosOcupados(asientosOcupados)
        self.setBilletes(billetes)

    def getAsientosLibres(self):
        return self.__asientosLibres

    def setAsientosLibres(self, asientos):
        self.__asientosLibres = asientos

    def getAsientosOcupados(self):
        return self.__asientosOcupados

    def setAsientosOcupados(self, asientos):
        self.__asientosOcupados = asientos

    def getBilletes(self):
        return self.__billetes

    def setBilletes(self, billetes):
        self.__billetes = billetes

    def ventaBilletes(self, numeroBilletes):
        if numeroBilletes > self.getAsientosLibres():
            return "No hay asientos suficientes"
        else:
            self.setAsientosOcupados(self.getAsientosOcupados() + numeroBilletes)
            self.setAsientosLibres(self.getAsientosLibres() - numeroBilletes)

    def devolucionBilletes(self, numeroBilletes):
        if numeroBilletes > self.getAsientosOcupados():
            return "No se pueden devolver tantos billetes"
        else:
            self.setAsientosOcupados(self.getAsientosOcupados() - numeroBilletes)
            self.setAsientosLibres(self.getAsientosLibres() + numeroBilletes)

    def estadoVenta(self):
        return f"Plazas totales: {self.getAsientosLibres() + self.getAsientosOcupados()}, Plazas vendidas: {self.getAsientosOcupados()}, Plazas libres: {self.getAsientosLibres()} "