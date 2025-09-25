from Bus import Bus

plazas_totales = int(input())

buses = [Bus(plazas_totales)]
bus_seleccionado = 0

def menu():
    return "1.- Venta de bitllets"
    + "2.- Devoluci� de bitllets"
    + "3.- Estat de venda"
    + "4.- Afegir Bus"
    + "5.- Seleccionar Bus"
    + "0.- Sortir"

menu()
opcion = int(input())

while opcion != 0:
    
    if opcion == 1:
        billetes_comprar = input("Seleciona el numero de billetes que quieres comprar")
        buses[bus_seleccionado].ventaBilletes(seleccion)
    elif opcion == 2:
        billetes_devolver = input("Seleciona el numero de billetes que quieres devolver")
        buses[bus_seleccionado].devolucionBilletes(seleccion)
    elif opcion == 3:
        buses[bus_seleccionado].estadoVenta()
    elif opcion == 4:
        plazas_totales = int(input())
        buses.append(Bus(plazas_totales))
    elif opcion == 5:
        print("Hay {len(buses)} buses")  
        bus_seleccionado = int(input())
    menu()
    opcion = int(input())
