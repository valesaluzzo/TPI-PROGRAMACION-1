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