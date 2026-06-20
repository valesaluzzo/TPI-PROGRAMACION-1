def menu_principal():
    print("          MENÚ PRINCIPAL - TRABAJO PRÁCTICO")
    print("\nOpciones: 1. Ejecutar Consigna 1 - Parte A (Conjuntos de Usuarios), 2. Ejecutar Consigna 1 - Parte B (Tabla de Verdad y Críticos), 3. Ejecutar Consigna 3 - Parte B (Cálculos de Matrices), 4. Salir del programa")
    opcion = int(input("Ingrese una opcion: "))
    match opcion:
        case 1:
            ejecutar_consigna_1_parte_a()
        case 2:
            ejecutar_consigna_1_parte_b()
        case 3:
            ejecutar_consigna_3_matematica()
        case 4:
            print("\n¡Gracias por utilizar el sistema! Saliendo...")


def ejecutar_consigna_1_parte_a():
    print("\n--- CONSIGNA 1: PARTE A (Conjuntos de Usuarios) ---")
    vec4 = []
    vec5 = []
    vec6 = []
    vec7 = []
    vec8 = []

    # Usuarios que utilizan ambas plataformas
    for i in range(len(vec1)):
        encontrado = False
        for x in vec2:
            if x == vec1[i]:
                encontrado = True
                break
        if encontrado:
            vec4.append(vec1[i])
    print(f"A-1.1 Ambas plataformas: {vec4}")

    # Usuarios que utilizan al menos una plataforma
    for i in range(len(vec1)):
        vec5.append(vec1[i])
    for i in range(len(vec2)):
        encontrado = False
        for x in vec5:
            if x == vec2[i]:
                encontrado = True
                break
        if not encontrado:
            vec5.append(vec2[i])
    print(f"A-1.2 Al menos una plataforma: {vec5}")






# DATOS INICIALES
vec1 = [101, 102, 103, 104, 105, 106]  # Plataforma A
vec2 = [104, 105, 106, 107, 108]       # Plataforma B
vec3 = [102, 105, 109]                 # Errores C
M = [
    [120, 150, 100],
    [200, 180, 220],
    [90,  110, 95]
]
C = [
    [30, 20, 10],
    [15, 25, 20],
    [40, 10, 30]
]
filas = 3
columnas = 3

menu_principal()