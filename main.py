from Persona import Persona
from Bus import Bus
from Billete import Billete

plazas_totales = int(input())

buses = [Bus(plazas_totales)]

def menu():
    return "1.- Venta de bitllets"
    + "2.- Devolució de bitllets"
    + "3.- Estat de venda"
    + "4.- Afegir Bus"
    + "0.- Sortir"