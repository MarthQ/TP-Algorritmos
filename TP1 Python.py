##############################################################################
# Trabajo Práctico N°1 
# Algoritmos y Estructura de Datos
# Comisión 109 de Ingeniería en Sistemas de la Información

# Integrantes:
# Ochoa, María Sofía - Legajo 50.452
# Piazza, Nair Antonella - Legajo 50.330
# Quagliardi, Martín Nicolás - DNI 45.341.323
# Ravera, Camila Denisse -  Legajo 50.468

##############################################################################


# en_construccion(), opciones_menu(), opciones_admin(), opciones_terciario()
# Contienen casi todas las impresiones necesarias de los distintos menús.
def en_construccion():
    print( "Esta funcionalidad está en construcción.")

def opciones_menu():
    print("\n\n----- MENU PRINCIPAL -----")
    print("Elija una opción (números enteros del 1 al 9):")
    print("\t1 - ADMINISTRACIONES")
    print("\t2 - ENTREGA DE CUPOS")
    print("\t3 - RECEPCION")
    print("\t4 - REGISTRAR CALIDAD")
    print("\t5 - REGISTRAR PESO BRUTO")
    print("\t6 - REGISTRAR DESCARGA")
    print("\t7 - REGISTRAR TARA")
    print("\t8 - REPORTES")
    print("\t9 - FIN DEL PROGRAMA")

def opciones_admin():
    print("\n\n----- MENU ADMINISTRACIÓN -----")
    print("Opciones de A a G y V únicamente:")
    print("\tA - TITULARES")
    print("\tB - PRODUCTO")
    print("\tC - RUBROS")
    print("\tD - RUBROS POR PRODUCTO")
    print("\tE - SILOS")
    print("\tF - SUCURSALES")
    print("\tG - PRODUCTO POR TITULAR")
    print("\tV - VOLVER AL MENU PRINCIPAL")

def opciones_terciario():
    print("\n\n----- MENU TITULARES -----")
    print("\tA. ALTA")
    print("\tB. BAJA")
    print("\tC. CONSULTA")
    print("\tM. MODIFICACION")
    print("\tV. VOLVER AL MENÚ ANTERIOR")


# menu_terciario():
# opcion_terciario: Char (un caracter)
def menu_terciario():

    opciones_terciario()
    opcion_terciario = "A"
    while opcion_terciario != "V":
        opcion_terciario = input("Opción: ").upper() # Convertir toda cadena ingresada en mayúscula.
        while opcion_terciario == "" or len(opcion_terciario) > 1: # Validación de datos
            opcion_terciario = input("Opción incorrecta. Ingrese nuevamente: ")
        
        if opcion_terciario == "A": # Alta
            en_construccion()
        elif opcion_terciario == "B": # Baja
            en_construccion()
        elif opcion_terciario == "C": # Consulta
            en_construccion()
        elif opcion_terciario == "M": # Modificacion
            en_construccion()
        else: # Volver al menú principal
            opcion_terciario = "V"
            administracion()

# administracion()
# Variables:
# opcion_admin: Char
def administracion():
    
    opciones_admin()
    opcion_admin = "A"
    while opcion_admin != "V":
        
        opcion_admin = input("Opción: ").upper() # Convertir toda cadena ingresada en mayúscula.

        # Validación de datos
        while opcion_admin == "" or (opcion_admin > "G" and opcion_admin < "V") or opcion_admin > "V":
            opcion_admin = input("Opción incorrecta. Ingrese nuevamente: ")
 
        if opcion_admin == "A": # Titulares
            opcion_admin = "V"
            menu_terciario()
        elif opcion_admin == "B": # Producto
            opcion_admin = "V"
            menu_terciario()
        elif opcion_admin == "C": # Rubros
            opcion_admin = "V"
            menu_terciario()
        elif opcion_admin == "D": # Rubros por producto
            opcion_admin = "V"
            menu_terciario()
        elif opcion_admin == "E": # Silos
            opcion_admin = "V"
            menu_terciario()
        elif opcion_admin == "F": # Sucursales
            opcion_admin = "V"
            menu_terciario()
        elif opcion_admin == "G": # Producto por titular
            opcion_admin = "V"
            menu_terciario()
        else:
            opcion_admin = "V"
            main()

# Verificación de si se hizo la recepción de los datos de los N camiones. 
# La variable recepcionhecha (Booleano) funciona como verificación. En caso de que esté en False, significa que 
# los camiones no fueron ingresados, y por tanto hacer una planilla de reportes sería imposible.
recepcionhecha = False

# procedimiento recepcion()
# Variables:
# total_camiones, total_camiones_soja, total_camiones_maiz, camiones: Enteros (Integer)
# total_neto_soja, total_neto_maiz, promedio_neto_maiz, promedio_neto_soja, PESO_BRUTO, TARA, PESO_NETO: Real (Float)
# PATENTEMAYOR, PATENTEMENOR, decision: String (Cadena de caracteres)
# PRODUCTO: Char (un caracter)
def recepcion():
    global total_camiones, total_camiones_maiz, total_camiones_soja, total_neto_maiz, total_neto_soja, menor_maiz, mayor_soja, promedio_neto_soja, promedio_neto_maiz, PATENTEMAYOR, PATENTEMENOR, recepcionhecha

    # Inicialización de variables.
    total_camiones = 0
    total_camiones_soja = 1
    total_camiones_maiz = 1
    total_neto_soja = 0
    total_neto_maiz = 0
    promedio_neto_maiz = 0
    promedio_neto_soja = 0
    menor_maiz = 1000000000
    mayor_soja = 0
    PATENTEMAYOR = ""
    PATENTEMENOR = ""

    camiones = int(input("\nIngresar cantidad de camiones: "))

    while camiones < 1: # Validación de datos
        camiones = int(input("Error. Ingresar un camión o más: "))

    for camion in range(1, camiones+1):

        print(f"\nDatos del camión N{camion}")

        # Ingreso de datos, cálculo de peso neto y contador de camiones
        PATENTE = input("Ingresar número de patente ")
        PRODUCTO = input("Ingresar tipo de producto (M para maíz y S para soja.): ").upper()
        while PRODUCTO!="S" and PRODUCTO!="M":
            PRODUCTO=input("Ingrese una opcion valida:").upper()
        PESO_BRUTO = float(input("Ingresar peso bruto "))
        TARA = float(input("Ingresar tara "))
        PESO_NETO = PESO_BRUTO - TARA
        print("\nEl peso neto es ", PESO_NETO)
        total_camiones += 1

        # Cálculos por tipo de producto (Maíz o Soja)
        if PRODUCTO == "S":
            total_camiones_soja += 1
            total_neto_soja = total_neto_soja + PESO_NETO
            if PESO_NETO > mayor_soja:
                mayor_soja = PESO_NETO
                PATENTEMAYOR = PATENTE
        elif PRODUCTO == "M":
            total_camiones_maiz += 1
            total_neto_maiz = total_neto_maiz + PESO_NETO
            if PESO_NETO < menor_maiz:
                menor_maiz = PESO_NETO
                PATENTEMENOR = PATENTE

    # Cálculo de promedios
    promedio_neto_maiz = total_neto_maiz / total_camiones_maiz 
    promedio_neto_soja = total_neto_soja / total_camiones_soja

    recepcionhecha = True # Se valida la verificación

    # Opción de mostrar los reportes directamente
    decision = input("\n¿Desea mostrar los reportes? Ingrese SI o NO: \n").upper()
    while decision != "SI" and decision != "NO":  # Validación de datos
        decision = input("Ingrese una opción correcta. ") 
    if decision == "SI":
        reportes()
    elif decision == "NO":
        main()

# procedimiento reportes()
# Variables:
# total_camiones, total_camiones_maiz, total_camiones_soja: Enteros (Integer)
# promedio_neto_soja, promedio_neto_maiz, total_neto_maiz, total_neto_soja, menor_maiz, mayor_soja: Float (Real) 
# PATENTEMAYOR, PATENTEMENOR, decisionrep: String
def reportes():
    global total_camiones, total_camiones_maiz, total_camiones_soja, total_neto_maiz, total_neto_soja, menor_maiz, mayor_soja, promedio_neto_soja, promedio_neto_maiz, PATENTEMAYOR, PATENTEMENOR
    print("\nCantidad total de camiones que llegaron: ",  total_camiones)				
    print("Cantidad total de camiones de soja: ",  total_camiones_soja)			
    print("Cantidad total de camiones de maíz: ",  total_camiones_maiz)			
    print("Peso neto total de soja: ",  total_neto_soja)					
    print("Peso neto total de maíz: ",  total_neto_maiz)					
    print("Promedio del peso neto de soja por camión: ",  promedio_neto_soja)		
    print("Promedio del peso neto de maíz por camión: ", promedio_neto_maiz)		
    print("Patente del camión de soja que mayor cantidad de soja descargó: ", PATENTEMAYOR)		
    print("Patente del camión de maíz que menor cantidad de maíz descargó: ", PATENTEMENOR)

    # Opción de regreso al menú principal (main())
    decisionrep = input("\n¿Desea volver al menú principal? Ingrese SI o NO: ").upper()
    while decisionrep != "SI" and decisionrep != "NO":  
        decisionrep = input("Ingrese una opción correcta. ") 
    if decisionrep == "SI":
        main()
    elif decisionrep == "NO":
        print("Fin del programa.")

# main() -> Programa principal
# Variables:
# opcion: Char (un caracter)
def main():

    global recepcionhecha

    opcion = "1"

    while opcion != "9":
        opciones_menu()
        opcion = input("Opción: ")

    # Validación de datos
        while opcion == "" or len(opcion) > 1:
            opcion = input("Opción incorrecta. Ingresar nuevamente: ")
        while int(opcion) < 0 or int(opcion) > 9:
            opcion = input("Opción incorrecta. Ingresar nuevamente: ")

    # Menú de opciones
        if opcion == "1": # Administración
            opcion = "9"
            administracion() # Se ejecuta el módulo administración.
            
        elif opcion == "2": # Entrega de cupos
            en_construccion() # No desarrollado aún.

        elif opcion == "3": # Recepción
            opcion = "9"
            recepcion() 

        elif opcion == "4": # Registrar calidad
            en_construccion()

        elif opcion == "5": # Registrar peso bruto
            en_construccion() # No desarrollado aún.

        elif opcion == "6": # Registrar descarga
            en_construccion() # No desarrollado aún.

        elif opcion == "7": # Registrar tara
            en_construccion() # No desarrollado aún.

        elif opcion == "8": # Reportes
            if recepcionhecha != True: # Verificación
                print("Para realizar los reportes se necesita la recepción de los camiones, por favor seleccione la opción 3: ")
            else:
                opcion = "9"
                reportes() 

        else: # Fin del programa
            print("Fin del programa.")
        
# Ejecución del programa principal.
main()