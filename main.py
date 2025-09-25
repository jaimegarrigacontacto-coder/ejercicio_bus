from Bus import Bus

plazas_totales = ""
while plazas_totales.isnumeric() == False:
            plazas_totales = input("Introduce las plazas totales del bus: ")
            if plazas_totales.isnumeric():
                if int(plazas_totales) > 200 or int(plazas_totales) < 30:
                    plazas_totales = ""
            else:
                plazas_totales = ""
plazas_totales = int(plazas_totales)

buses = [Bus(plazas_totales)]
bus_seleccionado = 0

def menu():
    return f'''1.- Venta de billetes 
     2.- Devolucion de billetes
     3.- Estado de venta
     4.- Anadir bus
     5.- Seleccionar bus 
     0.- Salir'''

print(menu())

opcion = input("Selecciona la opcion deseada: ")

while opcion != "0":
    if opcion == "1":
        billetes_comprar = input("Seleciona el numero de billetes que quieres comprar: ")
        while billetes_comprar.isnumeric() == False:
            billetes_comprar = input()
        billetes_comprar = int(billetes_comprar)
        print(buses[bus_seleccionado].ventaBilletes(billetes_comprar))
    elif opcion == "2":
        billetes_devolver = input("Seleciona el numero de billetes que quieres devolver: ")
        while billetes_devolver.isnumeric() == False:
            billetes_devolver = input()
        billetes_devolver = int(billetes_devolver)
        print(buses[bus_seleccionado].devolucionBilletes(billetes_devolver))
    elif opcion == "3":
        print(buses[bus_seleccionado].estadoVenta())
    elif opcion == "4":
        plazas_totales = ""
        while plazas_totales.isnumeric() == False:
            plazas_totales = input("Introduce las plazas totales del bus: ")
            if plazas_totales.isnumeric():
                if int(plazas_totales) > 200 or int(plazas_totales) < 30:
                    plazas_totales = ""
            else:
                plazas_totales = ""
        plazas_totales = int(plazas_totales)
        buses.append(Bus(plazas_totales))
    elif opcion == "5":
        print(f"Hay {len(buses)} buses")
        for i in range(len(buses)):
            print(f"Bus: {i}")
        bus_seleccionado = ""
        while bus_seleccionado.isnumeric() == False:
            bus_seleccionado = input()
            if bus_seleccionado.isnumeric():
                if int(bus_seleccionado) < 0 or int(bus_seleccionado) > len(buses) -1:
                    bus_seleccionado = ""
            else:
                bus_seleccionado = "" 
        bus_seleccionado = int(bus_seleccionado)

    print(menu())
    opcion = input("Selecciona la opcion deseada: ")
