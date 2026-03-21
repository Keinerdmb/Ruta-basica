inventario = []


def agregar_producto():
    print("\n---Agregar producto---")

# Inventario
# Permite registrar un producto con su nombre, precio y cantidad
# Luego calcula el costo total y muestra el resultado 

# ----------------------------------
# Solicita el nombre del producto.
# ----------------------------------

    nombre = input("Ingresa el nombre del producto: ")

# ----------------------------------
# Solicita el precio del producto.
# ----------------------------------

    while True:
        try:
            precio = float(input("\nIngrese el precio del producto: "))
            break
        except ValueError:
            print("\nError. Debe ingresar un número válido.\n")

# ----------------------------------
# Solicita la cantidad del producto.
# ----------------------------------

    while True:
        try:
            cantidad = int(input("\nIngrese la cantidad del producto: "))
            break
        except ValueError:
            print("\nError. Debe ingresas una cantidad válida.\n")

#-----------------------------------
# Crear producto (Diccionario)
#-----------------------------------

    producto = {
        "Nombre": nombre,
        "Precio": precio,
        "Cantidad": cantidad
    }

#-----------------------------------
# Guardar en la lista
#-----------------------------------    

    inventario.append(producto)

    print("Producto agregado correctamente. \n")

#-----------------------------------
# Funcion (mostrar diccionario).
#-----------------------------------    

def mostrar_inventario():
    print("---Inventario---")

    if len (inventario) == 0:
        print("El inventario esta vacio. \n")

    else:
        for producto in inventario:
            print(f"Producto:{producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        print()
        
#-----------------------------------
# Funcion (calcular estadisticas).
#-----------------------------------

def calcu_estadisticas():
    print("---Estadisticas \n")

    if len(inventario) == 0:
        print("No hay productos registrados \n")
        return
    valor_total = 0
    total_productos = 0

    for producto in inventario:
        valor_total += producto ["precio"] * producto ["cantidad"]
        total_productos += producto ["cantidad"]

    print(f"Valor total del inventario {valor_total}")
    print(f"Productos totales: {total_productos}\n")

#-----------------------------------
# Menú principal
#-----------------------------------    
running = True

while running :
    print("====MENÚ====")
    print("1. Agregar producto.")
    print("2. Mostrar inventario.")
    print("3. Calcular estadisticas.")
    print("4. Salir")

    opcion = input("Seleccione una opción: \n")

    if opcion == "1":
        agregar_producto()

    elif opcion == "2":
        mostrar_inventario()

    elif opcion == "3":
        calcu_estadisticas()

    elif opcion == "4":
        print("Saliendo del sistema...")
        running = False

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



