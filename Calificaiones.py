# Sistema de cálculo de promedio por módulo en RIWI

#Variables

coders = 0
suma_promedios = 0
reprobados = 0
regulares = 0
excelentes = 0
mejor_promedio = -1
mejor_coder = ""


# Registro de coders
def pedir_nota(frente):
    while True:
       try: 
           nota = float(input(f"Ingrese la nota del coder"))
