##############################################################################
# Trabajo Práctico N°2 
# Algoritmos y Estructura de Datos
# Comisión 109 de Ingeniería en Sistemas de la Información

# Integrantes:
# Ochoa, María Sofía - Legajo 50.452
# Piazza, Nair Antonella - Legajo 50.330
# Quagliardi, Martín Nicolás - Legajo 51.657
# Ravera, Camila Denisse -  Legajo 50.468

##############################################################################

# Estética del programa
# función CLEAR para limpiar pantalla
import os
clear = lambda: os.system('cls')

# procedimiento inicializoarrays()
# TYPE:
# P = array [0..2] of String
# arrcupos = array [0..7] of String
# arrpatentes = array [0..7] of String
# arrpesobru = array [0..7] of Integer
# arrtara = array [0..7] of Integer
# productosxp = array [0..7] of String
# pesosnetos = array [0..7] of Integer
# mayores = array [0..5] of Integer
# menores = array [0..5] of Integer
# patentemay = array [0..5] of String
# patentemin = array [0..5] String
def inicializoarrays():
    global P, arrcupos, arrpatentes, arrpesobru, arrtara, productosxp, pesosnetos, mayores, menores, patentemay, patentemin
    P = [""] * 3
    arrcupos = [""] * 8
    arrpatentes = [""] * 8
    arrpesobru = [0] * 8
    arrtara = [0] * 8
    productosxp = [""] * 8
    pesosnetos = [0] * 8
    mayores = [0] * 5
    menores = [99999999999] * 5
    patentemay = [""] * 5
    patentemin = [""] * 5

# procedimiento inicializadodatoscam()
# VAR:
# total_camiones, total_camiones_maiz, total_camiones_soja, total_camiones_cebada, total_camiones_girasol, total_camiones_trigo,camion: Integer
# PATENTEMAYOR, PATENTEMENOR: String
# total_neto_maiz, total_neto_soja: Float
# promedio_neto_soja, promedio_neto_maiz: Float
def inicializodatoscam():
    global total_camiones, total_camiones_maiz, total_camiones_soja, total_camiones_cebada, total_camiones_girasol, total_camiones_trigo, total_neto_maiz, total_neto_soja, total_neto_trigo, total_neto_girasol, total_neto_cebada, menor_maiz, mayor_soja, promedio_neto_soja, promedio_neto_maiz, recepcionhecha, camion, Pprimero, Pmedio, contp, decisionprod, producto, porlomenosuno
    total_camiones = 0
    total_camiones_soja = 0
    total_camiones_maiz = 0
    total_camiones_trigo = 0
    total_camiones_girasol = 0
    total_camiones_cebada = 0
    total_neto_soja = 0
    total_neto_maiz = 0
    total_neto_trigo = 0
    total_neto_girasol = 0
    total_neto_cebada = 0
    promedio_neto_maiz = 0
    promedio_neto_soja = 0
    camion = 0
    Pprimero = ""
    Pmedio = ""
    contp = 0
    decisionprod = ""
    producto = ""
    porlomenosuno = False

# procedimientos en_construccion(), opciones_menu(), opciones_admin(), opciones_terciario()
# Contienen casi todas las impresiones necesarias de los distintos menús.

def en_construccion():
    print( "Esta funcionalidad está en construcción.")

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

#procedimiento opciones_terciario(titulo: String)
def opciones_terciario(titulo):
    print(f"----- MENU {titulo} -----")
    print("\tA. ALTA")
    print("\tB. BAJA")
    print("\tC. CONSULTA")
    print("\tM. MODIFICACION")
    print("\tV. VOLVER AL MENÚ ANTERIOR")

# procedimiento menu_terciario()
# opcion_terciario: Char (un caracter)
def menu_terciario():

    clear()
    opciones_terciario("TERCIARIO")
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

# procedimiento cargarprod(var P: P)
# VAR:
# Pprimero, Pmedio, producto, decisionprod: String
# i, contp, ncupos: Integer
def cargarprod(P):
    global contp, Pmedio, Pprimero, decisionprod, producto, porlomenosuno
    decisionprod = "SI"
    if ncupos == 0:
        while contp < 3 and decisionprod != "NO":

            porlomenosuno = True
            # Verificación de que el producto no se encuentre repetido o ya haya otro producto allí
            print(f"Ingresar el producto número {contp+1}. (Maíz, Soja, Trigo, Girasol o Cebada).")
            producto = input("- ").upper()
            
            while producto != "TRIGO" and producto != "SOJA" and producto != "MAIZ" and producto != "GIRASOL" and producto != "CEBADA":
                producto = input("No es un producto válido. Ingrese nuevamente: ").upper()
            
            while producto == Pprimero or producto == Pmedio:
                producto = input("Producto ya ingresado. Ingrese nuevamente: ").upper() 
                while producto != "TRIGO" and producto != "SOJA" and producto != "MAIZ" and producto != "GIRASOL" and producto != "CEBADA":
                    producto = input("No es un producto válido. Ingrese nuevamente: ").upper()

            P[contp] = producto
            contp += 1

            Pprimero = P[0]
            Pmedio = P[1] # guardo los valores en las variables a la fuerza y pregunto si ya están ahí

            if contp < 3:
                decisionprod = input("¿Desea ingresar otro producto? Ingrese SI o NO: ").upper()
                while decisionprod == "" or len(decisionprod) > 2: # Validación de datos
                    decisionprod = input("Opción incorrecta. Ingrese nuevamente: ")
                    
            if contp == 3 or decisionprod == "NO":
                print(f"Producto 1: {P[0]}\nProducto 2: {P[1]}\nProducto 3: {P[2]}")
                productosctm = input("Productos ingresados correctamente - Presione cualquier tecla para continuar ")
                clear()
                opciones_terciario("PRODUCTOS")

    else:
        print("Cupos ya otorgados.")

# procedimiento eliminarP(var P: P; producto: String)
# VAR
# j, i: Integer
# producto: String
def eliminarP(P, producto):
    j = 0
    while (P[j] != producto and j <3):
        j += 1
    if P[j]==producto:
        P[j] = " "
        print(f"El producto {producto} se eliminó correctamente.")
    else:
	    print("El Producto no se encontró.")  

# procedimiento bajaprod(var P: P)
# VAR
# producto: String
# ncupos: Integer
def bajaprod(P):
    # Si hay cupos otorgados, no se deben cambiar/eliminar los productos (para evitar que haya camiones sin productos dados de alta)
    if ncupos == 0: 
        print(f"Producto 1: {P[0]}\nProducto 2: {P[1]}\nProducto 3: {P[2]}")
        producto = input("Ingresar el nombre del producto a eliminar: ").upper() # BUCLE INFINITO PA
        eliminarP(P, producto)
    else:
        print("Cupos ya otorgados. No se pueden eliminar productos.")

# procedimiento modificarP(var P: P; producto: String, nuevoproducto: String)
# VAR
# j: Integer
# producto, nuevoproducto: String
# P: P
def modificarP(P, producto, nuevoproducto):
    j = 0
    while (P[j] != producto and j <2):
        j += 1
    if P[j]==producto:
        P[j] = nuevoproducto
        print(f"El producto {producto} ahora es {nuevoproducto}.")
    else:
	    print("El Producto no se encontró.")

# procedimiento modificacionproducto(var P: P)
# VAR
# producto, nuevoproducto: String
# ncupos: Integer
def modificacionproducto(P):

    if ncupos == 0:
        print(f"Producto 1: {P[0]}\nProducto 2: {P[1]}\nProducto 3: {P[2]}")

        producto = input("Ingresar el nombre del producto a modificar: ").upper()
        # Verificación de que sea de los ingresados
        while producto != "TRIGO" and producto != "SOJA" and producto != "MAIZ" and producto != "GIRASOL" and producto != "CEBADA":
            producto = input(f"No es un producto válido. Ingrese nuevamente: ").upper()

        nuevoproducto = input("Ingresar el nuevo producto: ").upper()
        # Verificación de que sea correcto y no se vaya a repetir
        while nuevoproducto != "TRIGO" and nuevoproducto != "SOJA" and nuevoproducto != "MAIZ" and nuevoproducto != "GIRASOL" and nuevoproducto != "CEBADA":
            nuevoproducto = input(f"No es un producto válido. Ingrese nuevamente: ").upper()
        while nuevoproducto == P[0] or nuevoproducto == P[1] or nuevoproducto == P[2]:
            nuevoproducto = input("Producto ya ingresado. Ingrese nuevamente: ").upper()

        modificarP(P, producto, nuevoproducto)
    else:
        print("Cupos ya otorgados. No se pueden modificar los productos.")

# procedimiento menu_productos():
# TYPE
# productos = array [0..2] de string
# VAR
# P: productos
# opcion_terciario: Char (un caracter)
def menu_productos():

    global P
    clear()
    opciones_terciario("PRODUCTOS")
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

# function repeticionpat(array, valor): Boolean
# array y valor pueden ser de cualquier tipo de dato a buscar en X type de array
# Cumple la función de ser globalizadora, de búsqueda secuencial en un arreglo.
# Por lo tanto no se puede definir un type específico para las variables usadas.
def repeticionpat(array, valor):
    for i in range(0,8):
        if array[i] == valor:
            return True

# procedimiento cupos()
# VAR
# decisioncup, nuevapatente, cuposctm: String
# arrpatentes: arrpatentes (Type Array declarado al inicio del programa)
# arrcupos: arrcupos (Type Array declarado al inicio del programa)
# ncupos: Integer
# nuevoestado: Char
ncupos = 0
def cupos():
    global ncupos, porlomenosuno
    if porlomenosuno != True:
        bah = input("Se requiere dar de alta productos antes de ingresar cupos - Presione cualquier tecla para volver ")
        clear()

    else:
        clear()
        print("----- MENÚ DE CUPOS -----")
        decisioncup = input("¿Desea ingresar un cupo? Ingrese SI o NO: ").upper()
        while decisioncup != "SI" and decisioncup != "NO":  # Validación de datos
            decisioncup = input("Ingrese una opción correcta: ").upper()

        while decisioncup == "SI" and ncupos < 8:
            clear()
            nuevapatente = input("Ingresar la patente del camión: ").upper()
            while len(nuevapatente) < 6 or len(nuevapatente) > 7: # Comprobamos la longitud de la patente
                nuevapatente = input("Error con la longitud de la patente. Por favor ingresar de vuelta: ").upper()
            if repeticionpat(arrpatentes, nuevapatente): # Buscamos si la patente existe en el array
                print("La patente ya tiene un cupo asignado.")
            else:
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

        cuposctm = input("Cupos ingresados correctamente - Presione cualquier tecla para continuar")
        clear()

# procedimiento administracion()
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
            clear()

# procedimiento regpesobruto()
# VAR
# x, pesobruto, totalbrutomaiz, totalbrutosoja, totalbrutotrigo, totalbrutogirasol, totalbrutocebada: Integer
# patentereg, decisionregp: String
# arrpatentes: arrpatentes
# arrcupos: arrcupos
# arrpesobru: arrpesobru
def regpesobruto():
    global totalbrutomaiz, totalbrutosoja, totalbrutotrigo, totalbrutogirasol, totalbrutocebada
    clear()
    decisionregp = input("¿Registrar un nuevo peso bruto? Ingrese SI o NO: ").upper()
    while decisionregp != "NO" and decisionregp != "SI": # Validación del sí
        decisionregp = input("Error. Ingresar una respuesta correcta: ").upper()
    while decisionregp == "SI":
        patentereg = input("Ingresar patente a registrar: ").upper()
        while len(patentereg) < 6 or len(patentereg) > 7:
            patentereg = input("La patente no es válida, ingresar de vuelta: ").upper()
        
        x = 0
        while x < 8 and arrpatentes[x] != patentereg:
            x += 1

        if x == 8:
            print("La patente no se encuentra en el sistema.")

        else:
            if arrcupos[x] == "E":
                if arrpesobru[x] == 0:
                        pesobruto = int(input("Ingresar peso bruto: "))
                        while pesobruto < 1:
                            pesobruto = int(input("El peso no es válido, ingresar un valor mayor a 0."))
                        arrpesobru[x] = pesobruto
                        print(f"Asignado el peso bruto de {pesobruto} kg del camión {patentereg}, con producto {productosxp[x]}.")
                else:
                    print("Esta patente ya tiene asignado un peso bruto.")
                    
            else:
                print("El cupo de esta patente no es válido para ingresar el peso bruto.")
    
        decisionregp = input("¿Registrar un nuevo peso bruto? Ingrese SI o NO: ").upper()
        while decisionregp != "NO" and decisionregp != "SI": # Validación del sí
            decisionregp = input("Error. Ingresar una respuesta correcta: ").upper()
        clear()

# procedimiento regtara
# VAR
# decisionregt, patentereg: String
# x, j, tara, total_neto_maiz, total_neto_soja, total_neto_trigo, total_neto_girasol, total_neto_cebada: Integer
# arrtara: arrtara, arrcupos: arrcupos, arrpesobru: arrpesobru
# productosxp: productos xp, pesosneto: pesosneto, menores: menores, patentemin: patentemin, mayores:mayores, patentemay: patentemay
def regtara():
    global total_neto_maiz, total_neto_soja, total_neto_trigo, total_neto_girasol, total_neto_cebada
    clear()
    decisionregt = input("¿Registrar una nueva tara? Ingrese SI o NO: ").upper()
    while decisionregt != "NO" and decisionregt != "SI": # Validación del sí
        decisionregt = input("Error. Ingresar una respuesta correcta: ").upper()
    while decisionregt == "SI":
        patentereg = input("Ingresar patente a registrar: ").upper()
        while len(patentereg) < 6 or len(patentereg) > 7:
            patentereg = input("La patente no es válida, ingresar de vuelta: ").upper()
        
        x = 0
        while x < 8 and arrpatentes[x] != patentereg:
            x += 1

        if x == 8:
            print("La patente no se encuentra en el sistema.")

        else:
            if arrcupos[x] == "E":
                if arrpesobru[x] != 0:
                        if arrtara[x] != 0:
                            print("Esta patente ya tiene una tara ingresada.")
                        else:
                            tara = int(input("Ingresar tara: "))
                            while tara < 1 or tara > arrpesobru[x]:
                                tara = int(input("La tara no es válida, volver a ingresar: "))
                            arrtara[x] = tara
                            pesoneto = arrpesobru[x] - tara
                            pesosnetos[x] = pesoneto
                            if productosxp[x] == "MAIZ":
                                total_neto_maiz += pesoneto
                                if pesoneto > mayores[0]:
                                    mayores[0] = pesoneto
                                    patentemay[0] = arrpatentes[x]
                                if pesoneto < menores[0]:
                                    menores[0] = pesoneto
                                    patentemin[0] = arrpatentes[x]
                            elif productosxp[x] == "SOJA":
                                total_neto_soja += pesoneto
                                if pesoneto > mayores[1]:
                                    mayores[1] = pesoneto
                                    patentemay[1] = arrpatentes[x]
                                if pesoneto < menores[1]:
                                    menores[1] = pesoneto
                                    patentemin[1] = arrpatentes[x]
                            elif productosxp[x] == "TRIGO":
                                total_neto_trigo += pesoneto
                                if pesoneto > mayores[2]:
                                    mayores[2] = pesoneto
                                    patentemay[2] = arrpatentes[x]
                                if pesoneto < menores[2]:
                                    menores[2] = pesoneto
                                    patentemin[2] = arrpatentes[x]
                            elif productosxp[x] == "GIRASOL":
                                total_neto_girasol += pesoneto
                                if pesoneto > mayores[3]:
                                    mayores[3] = pesoneto
                                    patentemay[3] = arrpatentes[x]
                                if pesoneto < menores[3]:
                                    menores[3] = pesoneto
                                    patentemin[3] = arrpatentes[x]
                            elif productosxp[x] == "CEBADA":
                                total_neto_cebada += pesoneto
                                if pesoneto > mayores[4]:
                                    mayores[4] = pesoneto
                                    patentemay[4] = arrpatentes[x]
                                if pesoneto < menores[4]:
                                    menores[4] = pesoneto
                                    patentemin[4] = arrpatentes[x]
                        print(f"Asignada la tara de {tara} kg del camión {patentereg}, con producto {productosxp[x]}.")
                else:
                    print("Error - Para asignar la tara se requiere tener asignado un peso bruto.")
                    
            else:
                print("El cupo de esta patente no es válido para ingresar la tara.")
    
        decisionregt = input("¿Registrar una nueva tara? Ingrese SI o NO: ").upper()
        while decisionregt != "NO" and decisionregt != "SI": # Validación del sí
            decisionregt = input("Error. Ingresar una respuesta correcta: ").upper()
        clear()

# function tebuscoaca(P: arrproducto, producto): Boolean
# VAR
# i: Integer
def tebuscoaca(P, producto):
    for i in range(0, 3):
        if P[i] == producto:
            return True

# procedimiento recepcion()
# Variables:
# total_camiones, total_camiones_soja, total_camiones_maiz,total_camiones_cebada, total_camiones_trigo, total_camiones_girasol, lugar: Enteros (Integer)
# total_neto_soja, total_neto_maiz, promedio_neto_maiz, promedio_neto_soja, PESO_BRUTO, TARA, PESO_NETO: Real (Float)
# PATENTEMAYOR, PATENTEMENOR, decision, camiones, PATENTE, respuestarep, PRODUCTO: String (Cadena de caracteres)
# PRODUCTO: Char (un caracter)
# arrcupos: arrcupos
# arrpatentes: arrpatentes

# Verificación de si se hizo la recepción de los datos de los N camiones. 
# La variable recepcionhecha (Booleano) funciona como verificación. En caso de que esté en False, significa que 
# los camiones no fueron ingresados, y por tanto hacer una planilla de reportes sería imposible.
recepcionhecha = False

def recepcion():
    clear()
    global total_camiones, total_camiones_maiz, total_camiones_soja, total_camiones_cebada, total_camiones_girasol, total_camiones_trigo, total_neto_maiz, total_neto_soja, menor_maiz, mayor_soja, promedio_neto_soja, promedio_neto_maiz, PATENTEMAYOR, PATENTEMENOR, recepcionhecha, camion

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
        clear()
        print(f"\nDatos del camión")
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

                print("Ingresar tipo de producto (Maíz, Soja, Trigo, Girasol, Cebada)")
                PRODUCTO = input("- ").upper()
                while tebuscoaca(P, PRODUCTO) != True and PRODUCTO != "S":
                    PRODUCTO = input("No es un producto válido o no está dado de alta, ingresar de vuelta (S\salir): ").upper()

                if PRODUCTO != "S":
                    arrcupos[lugar] = "E"
                    print(f'Se actualizó el cupo de la patente {PATENTE} a "En proceso"')

                if PRODUCTO == "MAIZ":
                    print(f"Cargado camión con patente {PATENTE} de {PRODUCTO}")
                    total_camiones_maiz += 1
                    productosxp[lugar] = PRODUCTO
                elif PRODUCTO == "SOJA":
                    print(f"Cargado camión con patente {PATENTE} de {PRODUCTO}")
                    total_camiones_soja += 1
                    productosxp[lugar] = PRODUCTO
                elif PRODUCTO == "TRIGO":
                    print(f"Cargado camión con patente {PATENTE} de {PRODUCTO}")
                    total_camiones_trigo += 1
                    productosxp[lugar] = PRODUCTO
                elif PRODUCTO == "GIRASOL":
                    print(f"Cargado camión con patente {PATENTE} de {PRODUCTO}")
                    total_camiones_girasol += 1
                    productosxp[lugar] = PRODUCTO
                elif PRODUCTO == "CEBADA":
                    print(f"Cargado camión con patente {PATENTE} de {PRODUCTO}")
                    total_camiones_cebada += 1
                    productosxp[lugar] = PRODUCTO
                total_camiones += 1
            else:
                print("Este camión ya fue procesado.")

        camiones = input("\n¿Desea ingresar otro camión? Ingrese SI o NO: ").upper()
        

        while camiones != "NO" and camiones != "SI": # Validación del sí
            camiones = input("Error. Ingresar una respuesta correcta: ").upper()
    clear()

    recepcionhecha = True # Se valida la verificación

# procedimiento reportes()
# Variables:
# total_camiones, total_camiones_maiz, total_camiones_soja, total_camiones_trigo, total_camiones_cebada, total_camiones_girasol: Enteros (Integer)
# promedio_neto_soja, promedio_neto_maiz, total_neto_maiz, total_neto_soja, total_neto_cebada, total_neto_girasol, total_neto_trigo, menor_maiz, mayor_soja, aux, aux2, aux3: Float (Real) 
# decisionrep: String
# t, v, j: Integer
# pesosnetos: pesosnetos, productosxp: productosxp, patentemay: patentemay, patentemin: patentemin
def reportes():

    clear()
    global total_camiones, total_camiones_maiz, total_camiones_soja, total_neto_maiz, total_neto_soja, menor_maiz, mayor_soja, promedio_neto_soja, promedio_neto_maiz, PATENTEMAYOR, PATENTEMENOR
    print("\nCantidad de cupos otorgados: ",  ncupos)
    print("Cantidad total de camiones que llegaron: ",  total_camiones, "\n")
   # print("") COMO VAS A HACER ESTO???? USA \N NO SEAS TROLO MAN
    print("Cantidad total de camiones de maíz: ",  total_camiones_maiz)				
    print("Cantidad total de camiones de soja: ",  total_camiones_soja)
    print("Cantidad total de camiones de trigo: ",  total_camiones_trigo)
    print("Cantidad total de camiones de girasol: ",  total_camiones_girasol)
    print("Cantidad total de camiones de cebada: ",  total_camiones_cebada, "\n"), 	
    #print("")				
    print("Peso neto total de maíz: ",  total_neto_maiz)
    print("Peso neto total de soja: ",  total_neto_soja)					
    print("Peso neto total de trigo: ",  total_neto_trigo)
    print("Peso neto total de girasol: ",  total_neto_girasol)
    print("Peso neto total de cebada: ",  total_neto_cebada, "\n")
    #print("")					
    if total_camiones_maiz != 0:
        print("Promedio del peso neto de maíz por camión: ",  total_neto_maiz / total_camiones_maiz)
    else:
        print("No hay un promedio de maíz para mostrar.")   		
    if total_camiones_soja != 0:
        print("Promedio del peso neto de soja por camión: ",  total_neto_soja / total_camiones_soja)
    else:
        print("No hay un promedio de soja para mostrar.")   
    if total_camiones_trigo != 0:
        print("Promedio del peso neto de trigo por camión: ",  total_neto_trigo / total_camiones_trigo)
    else:
        print("No hay un promedio de trigo para mostrar.")   
    if total_camiones_girasol != 0:
        print("Promedio del peso neto de girasol por camión: ",  total_neto_girasol / total_camiones_girasol)
    else:
        print("No hay un promedio de girasol para mostrar.")   
    if total_camiones_cebada != 0:
        print("Promedio del peso neto de cebada por camión: ",  total_neto_cebada / total_camiones_cebada)
    else:
        print("No hay un promedio de cebada para mostrar.")
    print("")
    print("Patente del camión de maíz que mayor cantidad de maiz descargó: ", patentemay[0])
    print("Patente del camión de maíz que menor cantidad de maíz descargó: ", patentemin[0], "\n")
    #print("")
    print("Patente del camión de soja que mayor cantidad de soja descargó: ", patentemay[1])
    print("Patente del camión de soja que menor cantidad de soja descargó: ", patentemin[1], "\n")
    #print("")
    print("Patente del camión de trigo que mayor cantidad de trigo descargó: ", patentemay[2])
    print("Patente del camión de trigo que menor cantidad de trigo descargó: ", patentemin[2], "\n")
    #print("")
    print("Patente del camión de girasol que mayor cantidad de girasol descargó: ", patentemay[3])
    print("Patente del camión de girasol que menor cantidad de girasol descargó: ", patentemin[3], "\n")
    #print("")
    print("Patente del camión de cebada que mayor cantidad de cebada descargó: ", patentemay[4])
    print("Patente del camión de cebada que menor cantidad de cebada descargó: ", patentemin[4], "\n")

    for t in range (0,8):
                for v in range (t+1,8):
                    if pesosnetos[t]<pesosnetos[v]:
                        aux=pesosnetos[t]
                        pesosnetos[t]=pesosnetos[v]
                        pesosnetos[v]=aux
                        aux2=arrpatentes[t]
                        arrpatentes[t]=arrpatentes[v]
                        arrpatentes[v]=aux2
                        aux3=productosxp[t]
                        productosxp[t]=productosxp[v]
                        productosxp[v]=aux3
    print("Listado de camiones ordenados por peso neto descendente:\n")
    print("PATENTE\tPRODUCTO PESO NETO")
    for j in range (0,8):
        print(arrpatentes[j], "\t", productosxp[j], "\t", pesosnetos[j])

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
            regpesobruto() 

        elif opcion == "6": # Registrar descarga
            en_construccion() 

        elif opcion == "7": # Registrar tara
            regtara() 

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