from modulo_servicios import *

inventario = []

#-----------------------------------
# Menú principal
#-----------------------------------    
running = True

while running :
    print("=======MENÚ=======")
    print("1. Agregar producto.")
    print("2. Mostrar inventario.")
    print("3. Calcular estadisticas.")
    print("4. Buscar producto.")
    print("5. Actualizar producto.")
    print("6. Eliminar producto.")
    print("7. Salir")

    opcion = input("Seleccione una opción: \n")

    if opcion == "1":
        nombre = input("Ingrese nombre del producto: ")

        while True:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                break
            except ValueError:
                print("Ingrese un precio valido.")

        while True:
            try:
                cantidad = int(input("Ingrese la cantidad del producto: "))   
                break
            except ValueError:
                print("Deberia ser un número.")     

        agregar_producto(inventario, nombre, precio, cantidad)
        print("\nProducto agregado exitosamente. \n")

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        calcu_estadisticas(inventario)


    elif opcion == "7":
        print("Saliendo del sistema...")
        running = False

    elif opcion == "4":
        nombre = input("Nombre del producto: \n").lower()
        producto = buscar_producto(inventario, nombre)

        if producto:
            print("\nProducto encontrado.\n")
            print(f"\nNombre: {producto['nombre'].capitalize()} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}\n")
        else:
            print("Producto no registrado.\n")

    elif opcion == "5":
        
        nombre = input("Nombre del producto: ").lower()            
        while True:
            cambio = input("ingrese el nuevo precio del producto o presione ENTER si no quiere hacer cambios: ")
            if cambio == "":
                n_precio = None
                break
            try:
                n_precio = float(cambio)
            except ValueError:
                print("Deberia ser un número.")
                
        while True:
            cambio = input("Ingrese la nueva cantidad del producto o presione Enter si no quiere hacer cambios: ")
            if cambio == "":
                n_cantidad = None
                break
            try:
                n_cantidad = int(cambio)
            except ValueError:    
                print("Deberia ser un número.")
                
        actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None)
    else:
        print("Ingrese una opción valida. intente nuevamente. \n")


# ----------------------------------------------------------------
# Este programa permite gestionar multiples productos en un inven
# tario.
# Se utiliza el menú interactvio con un bucle while para repetir
# opciones.
# Los productos se almacenan en una lista de diccionarios.
# Se aplican estructuras como:
# - Condicionales  (if, elif, else)
# - Bucles (While y for)
# - Funciones para  organizar el codigo
# Ademas, se pueden calcular estadisticas como el valor total y
# la cantidad total del productos. 
# ----------------------------------------------------------------



