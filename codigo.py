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
    # Usuarios que utilizan la plataforma pero no presentan errores
    for i in range(len(vec5)):
        tiene_error = False
        for x in vec3:
            if x == vec5[i]:
                tiene_error = True
                break
        if not tiene_error:
            vec6.append(vec5[i])
    print(f"A-1.3 Activos sin errores: {vec6}")

    # Usuarios que utilizan exclusivamente una sola plataforma
    for i in range(len(vec1)):
        encontrado_en_2 = False
        for x in vec2:
            if x == vec1[i]:
                encontrado_en_2 = True
                break
        if not encontrado_en_2:
            vec7.append(vec1[i])
            
    for i in range(len(vec2)):
        encontrado_en_1 = False
        for x in vec1:
            if x == vec2[i]:
                encontrado_en_1 = True
                break
        if not encontrado_en_1:
            vec7.append(vec2[i])
    print(f"A-1.4 Exclusivos de una sola: {vec7}")

    # Usuarios que aparecen en C pero no en A u B
    for i in range(len(vec3)):
        encontrado_en_1 = False
        for x in vec1:
            if x == vec3[i]:
                encontrado_en_1 = True
                break
        
        encontrado_en_2 = False
        for x in vec2:
            if x == vec3[i]:
                encontrado_en_2 = True
                break
                
        if not encontrado_en_1 and not encontrado_en_2:
            vec8.append(vec3[i])
    print(f"Errores externos (En C, pero no en A ni B): {vec8}")


def ejecutar_consigna_1_parte_b():
    print("\n--- CONSIGNA 1: PARTE B (Lógica Proposicional) ---")
    
    print("\nTabla de valores de verdad para (p v q) ^ r:")
    print("p\tq\tr\t(p or q) and r")
    valores = [True, False]
    for p_val in valores:
        for q_val in valores:
            for r_val in valores:
                resultado = (p_val or q_val) and r_val
                print(f"{p_val}\t{q_val}\t{r_val}\t{resultado}")

    # Crear el dataset unificado manualmente sin duplicados
    dataset = []
    for x in vec1:
        encontrado = False
        for d in dataset:
            if d == x: encontrado = True; break
        if not encontrado: dataset.append(x)
        
    for x in vec2:
        encontrado = False
        for d in dataset:
            if d == x: encontrado = True; break
        if not encontrado: dataset.append(x)
        
    for x in vec3:
        encontrado = False
        for d in dataset:
            if d == x: encontrado = True; break
        if not encontrado: dataset.append(x)

    criticos = []
    no_criticos = []

    for usuario in dataset:
        # Evaluar pertenencia a P (vec1)
        pertenece_p = False
        for x in vec1:
            if x == usuario: pertenece_p = True; break
            
        # Evaluar pertenencia a Q (vec2)
        pertenece_q = False
        for x in vec2:
            if x == usuario: pertenece_q = True; break
            
        # Evaluar pertenencia a R (vec3)
        pertenece_r = False
        for x in vec3:
            if x == usuario: pertenece_r = True; break

        # Condición lógica: (p v q) ^ r
        if (pertenece_p or pertenece_q) and pertenece_r:
            criticos.append(usuario)
        else:
            no_criticos.append(usuario)

    print("\nClasificacion final del Dataset:")
    print(f"Usuarios Criticos: {criticos}")
    print(f"Usuarios No Criticos: {no_criticos}")



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