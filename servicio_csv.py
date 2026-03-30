# -------------------------------
# Guardar CSV
# -------------------------------
def guardar_csv(inventario, ruta):
    if len(inventario) == 0:
        print("No hay productos para guardar.\n")
        return

    try:
        with open(ruta, "w") as archivo:
            archivo.write("nombre,precio,cantidad\n")

            for producto in inventario:
                archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")

        print(f"Inventario guardado en: {ruta}\n")

    except Exception as e:
        print("Error al guardar:", e)


# -------------------------------
# Cargar CSV
# -------------------------------
def cargar_csv(ruta):
    inventario = []

    try:
        with open(ruta, "r") as archivo:
            lineas = archivo.readlines()

            for linea in lineas[1:]:
                nombre, precio, cantidad = linea.strip().split(",")

                producto = {
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                }

                inventario.append(producto)

        print("Inventario cargado correctamente.\n")
        return inventario

    except FileNotFoundError:
        print("Archivo no encontrado.\n")
        return []

    except Exception as e:
        print("Error al cargar:", e)
        return []