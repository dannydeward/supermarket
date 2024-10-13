""" crear la caja de ventas de un super mercado, donde se registren los articulo para vender y su precio, las 
 ventas, nos de el total de la venta y el cambio """

inventario = {}
ventas = []
total_ventas = 0
Pago = 0
cambio = 0

def carga_inventario():
    opcion = input('Vamos al módulo de carga de inventario, ¿desea continuar? responda Y o N: ')
    if opcion == "Y" or opcion == "y":
        while True:
            articulo = input('Ingrese el nombre de un artículo al inventario o ingrese S para salir: ')
            if articulo == "S" or articulo == "s":
                print("\nInventario actualizado:")
                for item, precio in inventario.items():
                    print(f"{item}: ${precio}")
                return inventario
            else:
                try:
                    precio = int(input('Ingrese el precio del artículo: '))
                    inventario[articulo] = precio
                except ValueError:
                    print("Por favor, ingrese un número válido para el precio.")
                
def carga_ventas():
    global total_ventas
    opcion = input('Vamos al módulo de carga de ventas, ¿desea continuar? responda Y o N: ')
    if opcion == "Y" or opcion == "y":
        while True:
            venta = input('Ingrese el artículo a vender o presione S para salir: ')
            if venta == "S" or venta == "s":
                print(f'El total de la venta de {ventas} es: ', total_ventas)
                return
            if venta in inventario:
                try:
                    cantidad = int(input('Ingrese la cantidad que desea llevar: '))
                    precio = inventario[venta]
                    saldo = cantidad * precio
                    ventas.append(venta)
                    total_ventas += saldo
                except ValueError:
                    print("Por favor, ingrese una cantidad válida.")
            else:
                print(f"El artículo {venta} no está en el inventario.")
            

def cobrar():
    global total_ventas, cambio
    try:
        Pago = int(input('Ingrese la cantidad con la que va a pagar: '))
        if Pago > total_ventas:
            cambio = Pago - total_ventas
            print('Su cambio es', cambio)
        elif Pago < total_ventas:
            faltante = total_ventas - Pago
            print('Su pago es menor, faltan', faltante)
            diferencia = int(input('Ingrese la diferencia: '))
            if diferencia == faltante:
                print('El pago ha sido correcto')
        else:
            print('Su pago es correcto, gracias por la compra')
    except ValueError:
        print("Por favor, ingrese una cantidad válida.")

def resumen():
    print('Las ventas totales del día son:', total_ventas)

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Cargar Inventario")
        print("2. Registrar Ventas")
        print("3. Registar pago")
        print("4. Ver resumen")
        print("5. Salir")
              
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            carga_inventario()
        elif opcion == '2':           
            carga_ventas()
        elif opcion == '3':
            cobrar()
        elif opcion == '4':
            resumen()
        elif opcion == '5':
            print('Gracias por usar el sistema')
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

menu()