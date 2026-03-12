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

# ----------------------------------
# Calcula el costo total.
# ----------------------------------

costo_total = precio * cantidad

# ----------------------------------
# Muestra los resultados en consola.
# ----------------------------------

print("\n ---- Resúmen del producto ----")
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")

# ----------------------------------------------------------------
# Este programa solicita al usuario el nombre, precio y cantidad
# de un producto. Luego calcula el costo total multiplicando el
# precio por la cantidad y muestra el resultado en la consola.
# ----------------------------------------------------------------



