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

def ejecutar_consigna_3_matematica():
    print("\n--- CONSIGNA 3: PARTE B (Análisis de Matrices) ---")
    
    # --- Parte 3: Tiempos Promedio ---
    promedios_funciones = []
    for i in range(filas):
        suma_fila = 0
        for j in range(columnas):
            suma_fila += M[i][j]
        promedio = suma_fila / columnas
        promedios_funciones.append(promedio)
        print(f"Tiempo promedio de la Función {i+1}: {promedio:.2f} ms")

    print("-" * 40)

    promedios_servidores = []
    for j in range(columnas):
        suma_columna = 0
        for i in range(filas):
            suma_columna += M[i][j]
        promedio = suma_columna / filas
        promedios_servidores.append(promedio)
        print(f"Tiempo promedio en el Servidor {j+1}: {promedio:.2f} ms")

    # --- Parte 4: Matriz Transpuesta ---
    print("\n=== Matriz Transpuesta M^T ===")
    M_transpuesta = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(filas):
        for j in range(columnas):
            M_transpuesta[j][i] = M[i][j]
    for fila in M_transpuesta:
        print(fila)

    # --- Parte C (5): Productos Matriciales ---
    print("\n=== Producto Elemento a Elemento (Hadamard) ===")
    T_elemento_a_elemento = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(filas):
        for j in range(columnas):
            T_elemento_a_elemento[i][j] = M[i][j] * C[i][j]
    for fila in T_elemento_a_elemento:
        print(fila)
    
    
    print("\n=== Producto Matricial Estándar (M . C) ===")
    T_producto_puro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(filas):
        for j in range(columnas):
            suma_producto = 0
            for k in range(columnas):
                suma_producto += M[i][k] * C[k][j]
            T_producto_puro[i][j] = suma_producto
    for fila in T_producto_puro:
        print(fila)

    # --- Parte E (8): Simetría ---
    es_simetrica = True
    for i in range(filas):
        for j in range(columnas):
            if M[i][j] != M_transpuesta[i][j]:
                es_simetrica = False
    print(f"\n¿La matriz M es simétrica?: {es_simetrica}")

    # --- Parte E (9): Determinante por Sarrus ---
    a, b, c = M[0][0], M[0][1], M[0][2]
    d, e, f = M[1][0], M[1][1], M[1][2]
    g, h, i = M[2][0], M[2][1], M[2][2]
    determinante = (a*e*i + b*f*g + c*d*h) - (c*e*g + a*f*h + b*d*i)
    print(f"Determinante de M (Sarrus): {determinante:.2f}")
    print(f"¿Es invertible?: {determinante != 0}")

    # --- Parte F (11): Análisis de Extremos ---
    max_promedio = promedios_funciones[0]
    peor_funcion = 1
    for idx in range(1, len(promedios_funciones)):
        if promedios_funciones[idx] > max_promedio:
            max_promedio = promedios_funciones[idx]
            peor_funcion = idx + 1

    min_promedio = promedios_servidores[0]
    mejor_servidor = 1
    for idx in range(1, len(promedios_servidores)):
        if promedios_servidores[idx] < min_promedio:
            min_promedio = promedios_servidores[idx]
            mejor_servidor = idx + 1

    print(f"\nFunción con MAYOR costo promedio: Función {peor_funcion}")
    print(f"Servidor MÁS EFICIENTE: Servidor {mejor_servidor}")

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