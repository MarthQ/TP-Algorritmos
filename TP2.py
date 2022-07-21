##############################################################################
# Trabajo Práctico N°1 
# Algoritmos y Estructura de Datos
# Comisión 109 de Ingeniería en Sistemas de la Información

# Integrantes:
# Ochoa, María Sofía - Legajo 50.452
# Piazza, Nair Antonella - Legajo 50.330
# Quagliardi, Martín Nicolás - Legajo 51.657
# Ravera, Camila Denisse -  Legajo 50.468

##############################################################################

# función CLEAR para limpiar pantalla

import os
clear = lambda: os.system('cls')

# en_construccion(), opciones_menu(), opciones_admin(), opciones_terciario()
# Contienen casi todas las impresiones necesarias de los distintos menús.

def en_construccion():
    print( "Esta funcionalidad está en construcción.")

def inicializoarrays():
    global P, arrcupos, arrpatentes, arrpesobru, arrtara
    P = [""] * 3
    arrcupos = [""] * 8
    arrpatentes = [""] * 8

def inicializodatoscam():
    global total_camiones, total_camiones_maiz, total_camiones_soja, total_neto_maiz, total_neto_soja, menor_maiz, mayor_soja, promedio_neto_soja, promedio_neto_maiz, PATENTEMAYOR, PATENTEMENOR, recepcionhecha, camion
    total_camiones = 0
    total_camiones_soja = 0
    total_camiones_maiz = 0
    total_neto_soja = 0
    total_neto_maiz = 0
    promedio_neto_maiz = 0
    promedio_neto_soja = 0
    menor_maiz = 1000000000
    mayor_soja = 0
    PATENTEMAYOR = ""
    PATENTEMENOR = ""
    camion = 0

def opciones_menu():
    print("----- MENU PRINCIPAL -----")
    print("Elija una opción (números enteros del 0 al 8):")
    print("\t1 - ADMINISTRACIONES")
    print("\t2 - ENTREGA DE CUPOS")
    print("\t3 - RECEPCION")
    print("\t4 - REGISTRAR CALIDAD")
    print("\t5 - REGISTRAR PESO BRUTO")
    print("\t6 - REGISTRAR DESCARGA")
    print("\t7 - REGISTRAR TARA")
    print("\t8 - REPORTES")
    print("\t0 - FIN DEL PROGRAMA")

def opciones_admin():
    print("----- MENU ADMINISTRACIÓN -----")
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
    print("----- MENU TITULARES -----")
    print("\tA. ALTA")
    print("\tB. BAJA")
    print("\tC. CONSULTA")
    print("\tM. MODIFICACION")
    print("\tV. VOLVER AL MENÚ ANTERIOR")

# menu_terciario():
# opcion_terciario: Char (un caracter)
def menu_terciario():

    clear()
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

def cargarprod(P):
    Pprimero = ""
    Pmedio = ""
    for i in range(0,3):

        # Verificación de que el producto no se encuentre repetido o ya haya otro producto allí

        P[i]= input(f"Ingresar el producto número {i+1}. (Maíz, Soja, Trigo, Girasol o Cebada): ").upper()
        
        while P[i] != "TRIGO" and P[i] != "SOJA" and P[i] != "MAIZ" and P[i] != "GIRASOL" and P[i] != "CEBADA":
            P[i] = input("No es un producto válido. Ingrese nuevamente: ").upper()
        
        while P[i] == Pprimero or P[i] == Pmedio:
            P[i] = input("Producto ya ingresado. Ingrese nuevamente: ").upper()

        Pprimero = P[0]
        Pmedio = P[1] # guardo los valores en las variables a lo gitanazo y pregunto si ya están ahí
        
def eliminarP(P, producto):
    j = 0
    while (P[j] != producto and j <3):
        j += 1
    if P[j]==producto:
        P[j] = " "
        print(f"El producto {producto} se eliminó correctamente.")
    else:
	    print("El Producto no se encontró.")  

def bajaprod(P):
    print(f"Producto 1: {P[0]}\nProducto 2: {P[1]}\nProducto 3: {P[2]}")
    producto = input("Ingresar el nombre del producto a eliminar: ").upper()
    eliminarP(P, producto)

def modificarP(P, producto, nuevoproducto):
    j = 0
    while (P[j] != producto and j <2):
        j += 1
    if P[j]==producto:
        P[j] = nuevoproducto
        print(f"El producto {producto} ahora es {nuevoproducto}.")
    else:
	    print("El Producto no se encontró.")

def modificacionproducto(P):
    print(f"Producto 1: {P[0]}\nProducto 2: {P[1]}\nProducto 3: {P[2]}")

    producto = input("Ingresar el nombre del producto a modificar: ").upper()
    while producto != "TRIGO" and producto != "SOJA" and producto != "MAIZ" and producto != "GIRASOL" and producto != "CEBADA":
        producto = input(f"No es un producto válido. Ingrese nuevamente: ").upper()

    nuevoproducto = input("Ingresar el nuevo producto: ").upper()
    while nuevoproducto != "TRIGO" and nuevoproducto != "SOJA" and nuevoproducto != "MAIZ" and nuevoproducto != "GIRASOL" and nuevoproducto != "CEBADA":
           nuevoproducto = input(f"No es un producto válido. Ingrese nuevamente: ").upper()

    while nuevoproducto == P[0] or nuevoproducto == P[1] or nuevoproducto == P[2]:
        nuevoproducto = input("Producto ya ingresado. Ingrese nuevamente: ").upper()

    modificarP(P, producto, nuevoproducto)

# menu_productos():
# TYPE
# productos = array [1..3] de string
# VAR
# P: productos
# opcion_terciario: Char (un caracter)

def menu_productos():

    global P
    clear()
    opciones_terciario()
    opcion_terciario = "A"
    while opcion_terciario != "V":
        opcion_terciario = input("Opción: ").upper() # Convertir toda cadena ingresada en mayúscula.
        while opcion_terciario == "" or len(opcion_terciario) > 1: # Validación de datos
            opcion_terciario = input("Opción incorrecta. Ingrese nuevamente: ")
        
        if opcion_terciario == "A": # Alta
            cargarprod(P)
        elif opcion_terciario == "B": # Baja
            bajaprod(P)
        elif opcion_terciario == "C": # Consulta
            print(f"Producto 1: {P[0]}\nProducto 2: {P[1]}\nProducto 3: {P[2]}")
        elif opcion_terciario == "M": # Modificacion
            modificacionproducto(P)
        else: # Volver al menú principal
            opcion_terciario = "V"
            administracion()


def repeticionpat(array, patente):

    for i in range(0,8):
        if array[i] == patente:
            return True

def buscocupo(array, patente):
    
    for i in range(0,8):
        if array[i] == patente:
            return i

# cupos()
# TYPE
#
# VAR
#

ncupos = 0

def cupos():

    global ncupos
    clear()
    print("----- MENÚ DE CUPOS -----")
    decisioncup = input("¿Desea ingresar un cupo? Ingrese SI o NO: ").upper()
    while decisioncup != "SI" and decisioncup != "NO":  # Validación de datos
        decisioncup = input("Ingrese una opción correcta: ").upper()

    while decisioncup == "SI" and ncupos < 8:
        clear()
        nuevapatente = input("Ingresar la patente del camión: ")
        while len(nuevapatente) < 6 or len(nuevapatente) > 7: # Comprobamos la longitud de la patente
            nuevapatente = input("Error con la longitud de la patente. Por favor ingresar de vuelta: ").upper()
        while repeticionpat(arrpatentes, nuevapatente): # Buscamos si la patente existe en el array
            nuevapatente = input("La patente ya tiene un cupo asignado, especificar otra: ").upper()
        arrpatentes[ncupos] = nuevapatente # Finalmente se asigna

        print("Posibles estados: P - Pendiente, E - En proceso, C - Cumplido")
        nuevoestado = input("Ingresar el estado de la patente: ").upper()
        while nuevoestado != "P" and nuevoestado != "E" and nuevoestado != "C": # Lo mismo acá...
            nuevoestado = input("Estado erróneo. Ingresar un estado correcto: ").upper()
        arrcupos[ncupos] = nuevoestado # Asignación del estado

        ncupos += 1
        print(f"Se ingresó Cupo Nº {ncupos} con patente {nuevapatente}")
        decisioncup = input("¿Desea ingresar un nuevo cupo? Ingrese SI o NO: ").upper()
        while decisioncup != "SI" and decisioncup != "NO":  # Validación de datos
            decisioncup = input("Ingrese una opción correcta: ").upper()
    
    if ncupos >= 8:
        print("Se ha alcanzado el límite de cupos.")

    print(arrcupos)
    cuposctm = input("Cupos ingresados correctamente - Presione cualquier tecla para continuar")
    clear()

# administracion()
# Variables:
# opcion_admin: Char
def administracion():
    
    clear()
    opciones_admin()
    opcion_admin = "A"
    while opcion_admin != "V":
        
        opcion_admin = input("Opción: ").upper() # Convertir toda cadena ingresada en mayúscula.

        # Validación de datos
        while opcion_admin == "" or (opcion_admin > "G" and opcion_admin < "V") or opcion_admin > "V":
            opcion_admin = input("Opción incorrecta. Ingrese nuevamente: ").upper()
 
        if opcion_admin == "A": # Titulares
            opcion_admin = "V"
            menu_terciario()
        elif opcion_admin == "B": # Producto
            opcion_admin = "V"
            menu_productos()
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


# regpesobruto()
# TYPE
#
# VAR
#
def regpesobruto():
    clear()
    patentereg = input("Ingresar patente a registrar: ")




def tebuscoaca(P, producto):
    for i in range(0, 3):
        if P[i] == producto:
            return True

# procedimiento recepcion()
# Variables:
# total_camiones, total_camiones_soja, total_camiones_maiz, camiones: Enteros (Integer)
# total_neto_soja, total_neto_maiz, promedio_neto_maiz, promedio_neto_soja, PESO_BRUTO, TARA, PESO_NETO: Real (Float)
# PATENTEMAYOR, PATENTEMENOR, decision: String (Cadena de caracteres)
# PRODUCTO: Char (un caracter)

# Verificación de si se hizo la recepción de los datos de los N camiones. 
# La variable recepcionhecha (Booleano) funciona como verificación. En caso de que esté en False, significa que 
# los camiones no fueron ingresados, y por tanto hacer una planilla de reportes sería imposible.
recepcionhecha = False

def recepcion():
    clear()
    global total_camiones, total_camiones_maiz, total_camiones_soja, total_neto_maiz, total_neto_soja, menor_maiz, mayor_soja, promedio_neto_soja, promedio_neto_maiz, PATENTEMAYOR, PATENTEMENOR, recepcionhecha, camion

    if recepcionhecha == True:
        print("Ya se ha realizado una recepción de camiones.")
        respuestarep = input("¿Desea ingresar una nueva recepción? Ingrese SI o NO: ").upper()
    
        while respuestarep != "NO" and respuestarep != "SI": # Validación del sí
            respuestarep = input("Error. Ingresar una respuesta correcta: ").upper()

        if respuestarep == "SI":

        # Inicialización de variables.
            inicializodatoscam()

    camiones = input("\n¿Comenzar a ingresar los camiones? Ingrese SI o NO: ").upper()

    while camiones != "NO" and camiones != "SI": # Validación del sí
        camiones = input("Error. Ingresar una respuesta correcta: ").upper()

    while camiones != "NO":
        
        print(f"\nDatos del camión")

        # Ingreso de datos, cálculo de peso neto y contador de camiones
        PATENTE = input("Ingresar número de patente ").upper()

        while len(PATENTE) < 6 or len(PATENTE) > 7:
            PATENTE = input("La patente no es válida, ingresar de vuelta: ").upper()

        lugar = 0
        while lugar < 8 and arrpatentes[lugar] != PATENTE:
            lugar += 1

        if lugar == 8:
            print("La patente no se encuentra registrada.")

        else:
            if arrcupos[lugar] == "P":
                arrcupos[lugar] = "E"
                print(f'Se actualizó el cupo de la patente {PATENTE} a "En proceso"')
                print("Ingresar tipo de producto (Maíz, Soja, Trigo, Girasol, Cebada)")
                PRODUCTO = input("- ").upper()
                while tebuscoaca(P, PRODUCTO) != True:
                    PRODUCTO = input("No es un producto válido o no está dado de alta, ingresar de vuelta: ").upper()

                if PRODUCTO == "MAIZ":
                    print("encontradoo")

                elif PRODUCTO == "SOJA":
                    print("encontradoo")
                
                elif PRODUCTO == "TRIGO":
                    print("encontradoo")

                elif PRODUCTO == "GIRASOL":
                    print("encontradoo")

                elif PRODUCTO == "CEBADA":
                    print("encontradoo")

            else:
                print("El cupo no es válido.")


        # PRODUCTO = input("Ingresar tipo de producto (M para maíz y S para soja.): ").upper()
        # while PRODUCTO!="S" and PRODUCTO!="M":
        #     PRODUCTO=input("Ingrese una opcion valida:").upper()                
        # PESO_BRUTO = float(input("Ingresar peso bruto "))
        # TARA = float(input("Ingresar tara "))
        # while TARA > PESO_BRUTO:
        #     TARA = float(input("La tara no puede ser mayor al Peso Bruto. Ingresar de vuelta: "))
        # PESO_NETO = PESO_BRUTO - TARA
        # print("\nEl peso neto es ", PESO_NETO)
        # total_camiones += 1

        # Cálculos por tipo de producto (Maíz o Soja)
        # if PRODUCTO == "S":
        #     total_camiones_soja += 1
        #     total_neto_soja = total_neto_soja + PESO_NETO
        #     if PESO_NETO > mayor_soja:
        #         mayor_soja = PESO_NETO
        #         PATENTEMAYOR = PATENTE
        # elif PRODUCTO == "M":
        #     total_camiones_maiz += 1
        #     total_neto_maiz = total_neto_maiz + PESO_NETO
        #     if PESO_NETO < menor_maiz:
        #         menor_maiz = PESO_NETO
        #         PATENTEMENOR = PATENTE

        camiones = input("\n¿Desea ingresar otro camión? Ingrese SI o NO: ").upper()

        while camiones != "NO" and camiones != "SI": # Validación del sí
            camiones = input("Error. Ingresar una respuesta correcta: ").upper()
    clear()

    # Cálculo de promedios
    # if total_camiones_maiz == 0:
    #     promedio_neto_maiz = 0
    # else:
    #     promedio_neto_maiz = total_neto_maiz / total_camiones_maiz 

    # if total_camiones_soja == 0:
    #     promedio_neto_maiz = 0
    # else:
    #     promedio_neto_soja = total_neto_soja / total_camiones_soja

    recepcionhecha = True # Se valida la verificación

    # Opción de mostrar los reportes directamente
    decision = input("\n¿Desea mostrar los reportes? Ingrese SI o NO: \n").upper()
    while decision != "SI" and decision != "NO":  # Validación de datos
        decision = input("Ingrese una opción correcta: ").upper() 
    if decision == "SI":
        reportes()
    else:
        clear()

# procedimiento reportes()
# Variables:
# total_camiones, total_camiones_maiz, total_camiones_soja: Enteros (Integer)
# promedio_neto_soja, promedio_neto_maiz, total_neto_maiz, total_neto_soja, menor_maiz, mayor_soja: Float (Real) 
# PATENTEMAYOR, PATENTEMENOR, decisionrep: String
def reportes():
    clear()
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
    reportesctm = input("\nPresione cualquier tecla para volver al menú principal: ")
    clear()

# main() -> Programa principal
# Variables:
# opcion: Char (un caracter)
def main():

    clear()
    inicializoarrays()
    inicializodatoscam()
    global recepcionhecha
    global ncupos
    opcion = "1"

    while opcion != "0":
        opciones_menu()
        opcion = input("Opción: ")

    # Validación de datos
        while opcion == "" or len(opcion) > 1:
            opcion = input("Opción incorrecta. Ingresar nuevamente: ")
        while int(opcion) < 0 or int(opcion) > 8:
            opcion = input("Opción incorrecta. Ingresar nuevamente: ")

    # Menú de opciones
        if opcion == "1": # Administración
            administracion() # Se ejecuta el módulo administración.
            
        elif opcion == "2": # Entrega de cupos
            cupos()

        elif opcion == "3": # Recepción
            recepcion() 

        elif opcion == "4": # Registrar calidad
            en_construccion()

        elif opcion == "5": # Registrar peso bruto
            regpesobruto() # No desarrollado aún.

        elif opcion == "6": # Registrar descarga
            en_construccion() 

        elif opcion == "7": # Registrar tara
            en_construccion() 

        elif opcion == "8": # Reportes
            if recepcionhecha != True: # Verificación
                clear()
                print("Para realizar los reportes se necesita la recepción de los camiones, por favor seleccione la opción 3: ")
            else:
                reportes() 

        else: # Fin del programa
            print("Fin del programa.")
        
# Ejecución del programa principal.
main()