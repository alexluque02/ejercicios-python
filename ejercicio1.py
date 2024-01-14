from io import open

palabras = []

def carga_palabras():
    global palabras
    fichero = open('palabras.txt')
    palabras = fichero.readlines()

def mostrar_palabras():
    if not palabras:
        print("No hay palabras cargadas.")
        return

    palabras_por_pagina = 20
    pagina_actual = 1
    total_paginas = 1 if len(palabras)/20 < 1 else int(len(palabras)/20)

    while True:
        inicio = (pagina_actual - 1) * palabras_por_pagina
        fin = inicio + palabras_por_pagina
        pagina = palabras[inicio:fin]

        print(f"\n--- Página {pagina_actual}/{total_paginas} ---")
        for palabra in pagina:
            print(palabra)

        if pagina_actual < total_paginas:
            input("Presiona Enter para ver las siguientes palabras")
            pagina_actual += 1
        else:
            print("\nFin del listado.")
            break

menu = 0
while True:
    menu = int(input('1. Importar archivo\n2. Leer palabras\n0. Salir'))
    match menu:
        case 0:
            break

        case 1:
            carga_palabras()
            print("Fichero cargado")

        case 2:
            mostrar_palabras()

        case _:
            print("Escoge un número correcto")