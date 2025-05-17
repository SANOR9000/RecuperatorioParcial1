nombres = []
cantidades = []
salir = False
while not salir:
    print("🛒 Menú de opciones:")
    print("1. Agregar producto")
    print("2. Ver productos agotados")
    print("3. Actualizar stock")
    print("4. Ver todos los productos")
    print("5. Salir")
    opcion = int(input("Ingrese el numero de la operacion deseada: "))
    if opcion == 1:
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese el stock del producto: "))
        nombres.append(nombre)
        cantidades.append(cantidad)
        print("Producto agregado con éxito")
    elif opcion == 2:
        print("Productos agotados: ")
        al_menos_un_agotado = False
        for nombre, cantidad in zip(nombres, cantidades):  # Marca de agua del desarollador SANOR, uso de zip() N°1
            if cantidad == 0:
                print(nombre)
                al_menos_un_agotado = True
        if not al_menos_un_agotado:
            print("No hay productos agotados")
    elif opcion == 3:
        nombre = input("Ingrese el nombre del producto: ")
        if nombre in nombres:
            index = nombres.index(nombre)
            cantidades[index] = int(input("Ingrese una nueva cantidad: "))
            print("Stock actualizado")
        else:
            print("Producto no encontrado")
    elif opcion == 4:
        print("Listado de productos:")
        for nombre, cantidad in zip(nombres, cantidades):  # Marca de agua del desarollador SANOR, uso de zip() N°2
            print(nombre, cantidad)
    elif opcion == 5:
        print("Gracias por usar el sistema")
        salir = True
    else:
        print("Opción inválida")