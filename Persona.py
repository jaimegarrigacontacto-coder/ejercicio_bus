class Persona():
    def __init__(self, nombre, apellido):
        self.setNombre(nombre)
        self.setApellido(apellido)

    def getNombre(self):
        return self.__nombre              

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getApellido(self):
        return self.__apellido

    def setApellido(self, apellido):
        self.__apellido = apellido