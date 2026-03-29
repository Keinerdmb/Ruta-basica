def agregar_producto( nombre, inventario, precio, cantidad):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)

def mostrar_inventario(inventario):

#-----------------------------------
# Funcion (mostrar diccionario).
#-----------------------------------

    print("---Inventario---")

    if len (inventario) == 0:
        print("El inventario esta vacio. \n")

    else:
        for producto in inventario:
            print(f"Producto: {producto['nombre'].capitalize()} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        print()

def calcu_estadisticas(inventario):

#-----------------------------------
# Funcion (calcular estadisticas).
#-----------------------------------

    print("---Estadisticas \n")

    if len(inventario) == 0:
        print("No hay productos registrados \n")
        return
    valor_total = 0
    total_productos = 0

    for producto in inventario:
        valor_total += producto ["precio"] * producto ["cantidad"]
        total_productos += producto ["cantidad"]

    print(f"Valor total del inventario: {valor_total}")
    print(f"Productos totales: {total_productos}\n")

def buscar_producto(inventario, nombre):

    for producto in inventario:
        if producto['nombre'] == nombre:
            return producto
    return None    

def actualizar_producto(inventario, nombre, n_precio=None, n_cantidad=None):
   
    producto = buscar_producto(inventario, nombre)
    if producto:
        if n_precio is not None:
           producto['precio'] = n_precio
        if n_cantidad is not None:
            producto['cantidad'] = n_cantidad
        
    else:
       print(f"Producto '{nombre}' no esta registrado.")        

def eliminar_producto(inventario, nombre):
    producto = buscar_producto(inventario, nombre)

    if producto:
        inventario.remove(producto)
        print(f"Producto: '{nombre.capitalize()}' eliminado correctamente.")
    else:
        print(f"Producto: '{nombre.capitalize()}' no se encontro en el inventario.")                   


   