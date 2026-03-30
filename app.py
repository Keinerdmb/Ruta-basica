from modulo_servicios import*
from servicio_csv import*

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
    print("7. Guardar en CSV.")
    print("8. Cargar desde CSV.")
    print("9. Salir.")

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

        agregar_producto(nombre, inventario, precio, cantidad)
        print("\nProducto agregado exitosamente. \n")

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        calcu_estadisticas(inventario)

    elif opcion == "9":
        print("Saliendo del sistema...")
        running = False

    elif opcion == "4":
        nombre = input("Nombre del producto: \n").lower()
        producto = buscar_producto(inventario, nombre)

        if producto:
            print("\nProducto encontrado.\n")
            print(f"\nNombre: {producto['nombre'].capitalize()} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}\n")

        else:
            print("\nProducto no registrado.\n")          

    elif opcion == "5":
        
        nombre = input("Nombre del producto: ").lower()
        producto = buscar_producto(inventario, nombre)
        
        if not producto:
            print("\nProducto no registrado. \n")
            continue

        while True:
            cambio = input("ingrese el nuevo precio del producto o presione ENTER si no quiere hacer cambios: ")
            if cambio == "":
                n_precio = None
                break
            try:
                n_precio = float(cambio)
                break
            except ValueError:
                print("Deberia ser un número.")
                
        while True:
            cambio = input("Ingrese la nueva cantidad del producto o presione Enter si no quiere hacer cambios: ").lower()
        
            if cambio == "":
                n_cantidad = None
                break
            try:
                n_cantidad = int(cambio)
                break
            except ValueError:    
                print("Deberia ser un número.")

        actualizar_producto(inventario, nombre, n_precio, n_cantidad)
        print(f"\nProducto '{nombre.capitalize()}' actualizado correctamente.\n")

    elif opcion == "6":
        nombre = input("Nombre del producto a eliminar: ").lower()
        eliminar_producto(inventario, nombre)

     # GUARDAR CSV
    elif opcion == "7":
        ruta = input("nombre del archivo (ej: inventario.csv): ")
        guardar_csv(inventario, ruta)

    # CARGAR CSV
    elif opcion == "8":
        ruta = input("Archivo a cargar: ")
        inventario = cargar_csv(ruta)

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



