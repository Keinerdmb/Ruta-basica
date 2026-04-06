# Sistema de Inventario en Python

## Descripción

Este proyecto es un sistema de inventario desarrollado en Python que permite gestionar productos mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar), así como almacenar y recuperar la información utilizando archivos CSV.

El sistema fue diseñado para reforzar conceptos fundamentales y prácticos de programación, evolucionando desde un programa básico hasta una aplicación modular y persistente.

---
## Diagrama de flujo

![Diagrama_de_flujo](<Diagrama de flujo.png>)

---

## Funcionalidades

El sistema permite:

* Agregar productos al inventario
* Mostrar todos los productos registrados
* Buscar productos por nombre
* Actualizar precio y/o cantidad de un producto
* Eliminar productos del inventario
* Calcular estadísticas del inventario:

  * Valor total
  * Cantidad total de productos
  * Producto más caro
  * Producto con mayor stock
* Guardar el inventario en un archivo CSV
* Cargar el inventario desde un archivo CSV

---

## Estructura del proyecto

El proyecto está organizado en múltiples archivos para mejorar la modularidad:

```
📁 proyecto/
│
├── app.py            # Archivo principal (menú e interacción)
├── servicios.py      # Lógica del inventario (CRUD y estadísticas)
├── archivos.py       # Manejo de archivos CSV
└── inventario.csv    # Archivo generado (persistencia de datos)
```

---

## Tecnologías y conceptos aplicados

Durante el desarrollo se aplicaron los siguientes conceptos:

* Listas y diccionarios
* Funciones y modularización
* Manejo de errores con try/except
* Bucles (while, for)
* Condicionales (if, elif, else)
* Lectura y escritura de archivos (CSV)
* Separación de responsabilidades en módulos

---

## Cómo funciona

1. El usuario interactúa con un menú en consola.
2. Puede seleccionar diferentes opciones (1–9).
3. El sistema ejecuta funciones según la opción elegida.
4. Los datos se almacenan en memoria (lista de diccionarios).
5. Opcionalmente, se pueden guardar o cargar desde un archivo CSV.

---

## Menú del sistema

```
1. Agregar producto
2. Mostrar inventario
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Estadísticas
7. Guardar CSV
8. Cargar CSV
9. Salir
```

---

## Ejemplo de uso

```
==== MENÚ ====
1. Agregar producto
2. Mostrar inventario
...

Seleccione una opción: 1

Nombre: Laptop
Precio: 800
Cantidad: 2

Producto agregado correctamente.
```

---

## Persistencia de datos

El sistema permite guardar y cargar el inventario mediante archivos CSV con el siguiente formato:

```
nombre,precio,cantidad
laptop,800,2
mouse,50,5
```

Además:

* Se validan errores de lectura/escritura
* Se manejan archivos inexistentes
* Se evita que el programa se cierre ante errores

---

## Cómo ejecutar el proyecto

### 1. Requisitos

* Python 3
* Git

Verificar instalación:

```bash
python --version
git --version
```

---

### 2. Clonar el repositorio

```bash
git clone https://github.com/Keinerdmb/Proyecto_inventario_pyhton.git
```

---

### 3. Acceder al proyecto

```bash
cd "Nombre de la carpeta donde se guardo"
```

---

### 4. Ejecutar el programa

```bash
python app.py
```

---

## Estado del proyecto

El sistema se encuentra funcional y cumple con:

* Operaciones CRUD completas
* Persistencia en archivos CSV
* Manejo de errores
* Estructura modular

---

## Autor

Keiner Martinez.
El programa actualmente funciona correctamente y calcula el costo total de los productos.
