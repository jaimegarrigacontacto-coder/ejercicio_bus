from Persona import Persona

class Billete:
    def __init__(self, plaza, persona):
        self.setPlaza(plaza)
        self.setPersona(persona)

    def getPlaza(self):
        return self.__plaza

    def setPlaza(self, plaza):
        self.__plaza = plaza

    def getPersona(self):
        return self.__persona

    def setPersona(self, persona):
        self.__persona = persona