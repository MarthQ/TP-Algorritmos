##############################################################################

# Trabajo Práctico N°3
# Algoritmos y Estructura de Datos
# Comisión 109 de Ingeniería en Sistemas de la Información

# Integrantes:
# Ochoa, María Sofía - Legajo 50.452
# Piazza, Nair Antonella - Legajo 50.330
# Quagliardi, Martín Nicolás - Legajo 51.657
# Ravera, Camila Denisse -  Legajo 50.468

##############################################################################

import pickle
import os
import datetime

# Estética del programa
# función CLEAR para limpiar pantalla
clear = lambda: os.system('cls')

# variables de COLOR para los print() de consola
VERDE = '\033[92m'
AMARILLO = '\033[93m'
ROJO = '\033[91m'
BLANCO = '\033[0m'

##### ##### REGISTROS ##### ##### 
class csoperacion:
    def __init__(self):
        self.patente = "" # 7 caracteres
        self.codproducto = 0
        self.fechacupo = datetime.datetime(1,1,1) #tipo DATETIME (fecha)
        self.estado = "" # char
        self.bruto = 0
        self.tara = 0

class csproducto:
    def __init__(self):
        self.codproducto = ""
        self.nombreproducto = ""

class csrubro:
    def __init__(self):
        self.codigorubro = 0
        self.nombrerubro = ""

class csrubroxproducto:
    def __init__(self):
        self.codigorubro = 0
        self.codigoproducto = 0
        self.valormax = 0.00 # float, mayor o igual a 0
        self.valormin = 0.00 # float, menor o igual a 100

class cssilo:
    def __init__(self):
        self.codigosilo = 0
        self.nombresilo = ""
        self.codproducto = 0
        self.stock = 0

class csreporte:
    def __init__(self):
        self.codproducto = 0
        self.cantcamiones = 0
        self.pesonetototal = 0
        self.menorpesoneto = 9999999999
        self.patentemenor = ""

##### #####  Apertura de archivos ##### ##### 
AFOPERACIONES = os.getcwd() + "\\OPERACIONES.DAT"
if os.path.exists(AFOPERACIONES) == True:
    ALOPERACIONES = open(AFOPERACIONES, "r+b")
else:
    ALOPERACIONES = open(AFOPERACIONES, "w+b")

RLOPERACIONES = csoperacion()

AFPRODUCTOS = os.getcwd() + "\\PRODUCTOS.DAT"
if os.path.exists(AFPRODUCTOS) == True:
    ALPRODUCTOS = open(AFPRODUCTOS, "r+b")
else:
    ALPRODUCTOS = open(AFPRODUCTOS, "w+b")

RLPRODUCTOS = csproducto()

AFRUBROS = os.getcwd() + "\\RUBROS.DAT"
if os.path.exists(AFRUBROS) == True:
    ALRUBROS = open(AFRUBROS, "r+b")
else:
    ALRUBROS = open(AFRUBROS, "w+b")
RLRUBROS = csrubro()

AFRUBROSXPRODUCTO = os.getcwd() + "\\RUBROS-X-PRODUCTO.DAT"
if os.path.exists(AFRUBROSXPRODUCTO) == True:
    ALRUBROSXPRODUCTO = open(AFRUBROSXPRODUCTO, "r+b")
else:
    ALRUBROSXPRODUCTO = open(AFRUBROSXPRODUCTO, "w+b")
RLRUBROSXPRODUCTO = csrubroxproducto()

AFSILOS = os.getcwd() + "\\SILOS.DAT"
if os.path.exists(AFSILOS) == True:
    ALSILOS = open(AFSILOS, "r+b")
else:
    ALSILOS = open(AFSILOS, "w+b")
RLSILOS = cssilo()

AFREPORTES = os.getcwd() + "\\REPORTES.DAT"
if os.path.exists(AFREPORTES) == True:
    ALREPORTES = open(AFREPORTES, "r+b")
else:
    ALREPORTES = open(AFREPORTES, "w+b")
RLREPORTES = csreporte()

##### ##### FORMATEOS ##### ##### 
def formatearproducto(RL):
    RL.codproducto = str(RL.codproducto)
    RL.codproducto = RL.codproducto.ljust(5, ' ')
    RL.nombreproducto = RL.nombreproducto.ljust(25, ' ')

def formatearrubro(RL):
    RL.codigorubro = str(RL.codigorubro)
    RL.codigorubro = RL.codigorubro.ljust(5, ' ') 
    RL.nombrerubro = RL.nombrerubro.ljust(25, ' ')

def formatearRxP(RL):
    RL.codigorubro = str(RL.codigorubro)
    RL.codigorubro = RL.codigorubro.ljust(5, ' ')
    RL.codigoproducto = str(RL.codigoproducto)
    RL.codigoproducto = RL.codigoproducto.ljust(5, ' ')
    RL.valormax = str(RL.valormax)
    RL.valormax = RL.valormax.ljust(7, ' ')
    RL.valormin = str(RL.valormin)
    RL.valormin = RL.valormin.ljust(7, ' ')

def formatearsilos(RL):
    RL.codigosilo = str(RL.codigosilo)
    RL.codigosilo = RL.codigosilo.ljust(5, ' ')
    RL.nombresilo = RL.nombresilo.ljust(25, ' ')
    RL.codproducto = str(RL.codproducto)
    RL.codproducto = RL.codproducto.ljust(5, ' ')
    RL.stock = str(RL.stock)
    RL.stock = RL.stock.ljust(10, ' ')

def formatearoperaciones(RL):
    RL.patente = str(RL.patente)
    RL.patente = RL.patente.ljust(7, ' ')
    RL.codproducto = str(RL.codproducto)
    RL.codproducto = RL.codproducto.ljust(5, ' ')
    RL.bruto = str(RL.bruto)
    RL.bruto = RL.bruto.ljust(5, ' ')
    RL.tara = str(RL.tara)
    RL.tara = RL.tara.ljust(5, ' ')

def formateareportes(RL):
    RL.codproducto = str(RL.codproducto)
    RL.codproducto = RL.codproducto.ljust(5, ' ')
    RL.cantcamiones = str(RL.cantcamiones)
    RL.cantcamiones = RL.cantcamiones.ljust(3, ' ')
    RL.pesonetototal = str(RL.pesonetototal)
    RL.pesonetototal = RL.pesonetototal.ljust(10, ' ')
    RL.menorpesoneto = str(RL.menorpesoneto)
    RL.menorpesoneto = RL.menorpesoneto.ljust(10, ' ')
    RL.patentemenor = str(RL.patentemenor)
    RL.patentemenor = RL.patentemenor.ljust(7, ' ')

def verificacionFecha(msj):
    os.system("cls")
    f = input(msj)
    listaf = f.split("/", 3)
    while len(listaf) != 3:
        print("El formato de la fecha es incorrecto")
        f = input(msj)
        listaf = f.split("/", 3)
    while not (len(listaf[0]) == 2 and len(listaf[1]) == 2 and len(listaf[2]) == 4) or not (listaf[0].isnumeric() and listaf[1].isnumeric() and listaf[2].isnumeric() or not (int(listaf[0]) in range(1, 32) and int(listaf[1]) in range(1, 13))):
        print("El formato de la fecha es incorrecto")
        f = input(msj)
        listaf = f.split("/", 3)
    return datetime.datetime.strptime(f, "%d/%m/%Y").date()


##### ##### ##### ##### ##### 
# procedimientos en_construccion(), opciones_menu(), opciones_admin(), opciones_terciario()
# Contienen casi todas las impresiones necesarias de los distintos menús.

def en_construccion():
    clear()
    print(ROJO + "Esta funcionalidad está en construcción." + BLANCO)
    os.system("pause")
    
def opciones_menu():
    print(VERDE + "----- MENU PRINCIPAL -----" + BLANCO)
    print("Elija una opción (números enteros del 0 al 8):")
    print("\t1 - ADMINISTRACIONES")
    print("\t2 - ENTREGA DE CUPOS")
    print("\t3 - RECEPCION")
    print("\t4 - REGISTRAR CALIDAD")
    print("\t5 - REGISTRAR PESO BRUTO")
    print("\t6 - REGISTRAR DESCARGA")
    print("\t7 - REGISTRAR TARA")
    print("\t8 - REPORTES")
    print("\t9 - LISTADO DE SILOS Y RECHAZOS")
    print("\t0 - FIN DEL PROGRAMA")

def opciones_admin():
    print(VERDE + "----- MENU ADMINISTRACIÓN -----" + BLANCO)
    print("Opciones de A a G y V únicamente:")
    print("\tA - TITULARES")
    print("\tB - PRODUCTO")
    print("\tC - RUBROS")
    print("\tD - RUBROS POR PRODUCTO")
    print("\tE - SILOS")
    print("\tF - SUCURSALES")
    print("\tG - PRODUCTO POR TITULAR")
    print("\tV - VOLVER AL MENU PRINCIPAL")

def opciones_terciario(titulo):
    print(VERDE + f"----- MENU {titulo} -----" + BLANCO)
    print("\tA. ALTA")
    print("\tB. BAJA")
    print("\tC. CONSULTA")
    print("\tM. MODIFICACION")
    print("\tV. VOLVER AL MENÚ ANTERIOR")

def menu_terciario():

    clear()
    opciones_terciario("TERCIARIO")
    opcion_terciario = "A"
    while opcion_terciario != "V":
        opcion_terciario = input("Opción: ").upper() # Convertir toda cadena ingresada en mayúscula.

        while opcion_terciario == "" or len(opcion_terciario) > 1 or opcion_terciario.isnumeric() == True: # Validación de datos
            opcion_terciario = input("Opción incorrecta. Ingrese nuevamente: ").upper()
        
        if opcion_terciario == "A": # Alta
            en_construccion()
        elif opcion_terciario == "B": # Baja
            en_construccion()
        elif opcion_terciario == "C": # Consulta
            en_construccion()
        elif opcion_terciario == "M": # Modificacion
            en_construccion()
        elif opcion_terciario == "V": # Volver al menú principal
            opcion_terciario = "V"
            administracion()

# Verificación de códigos
def verificacioncod(codigo):
    # isnumeric() devuelve TRUE si lo ingresado es un entero
    # el código es universalmente de 5 dígitos
    while codigo == "" or codigo.isnumeric() == False or int(codigo) not in range(0,100000): 
        codigo = input("Error. Ingrese nuevamente - ")
    return codigo


##### ##### PRODUCTO ##### ##### 
def cargarprod():
    global contp, decisionprod, producto, porlomenosuno
    decisionprod = "SI"

    while decisionprod != "NO":

        porlomenosuno = True
        # Verificación de que el producto no se encuentre repetido o ya haya otro producto allí
        print("Ingresar el nombre del producto: ")
        producto = input("- ").upper()
        
        while producto == "" or producto.isnumeric() == True or len(producto) > 25:
            producto = input("No es un producto válido. Ingrese nuevamente: ").upper()
        
        while tebuscopos(producto) != -1:
            producto = input("Producto ya ingresado. Ingrese nuevamente: ").upper() 
            while producto == "" or producto.isnumeric() == True:
                producto = input("No es un producto válido. Ingrese nuevamente: ").upper()

        RLPRODUCTOS = csproducto()
    
        # RLPRODUCTOS.codproducto devuelve un ENTERO el cual se verifica mediante la 
        # función VERIFICACIONCOD que devuelve un String(por eso lo convierto a ENTERO)
        # anido código para que no esté tan contaminado todo
        RLPRODUCTOS.codproducto = int(verificacioncod(input("Ingrese codigo de producto (hasta 5 dígitos): ")))

        while tebuscodigo(RLPRODUCTOS.codproducto) == True:
            RLPRODUCTOS.codproducto = int(verificacioncod(input("Código no válido. Ingrese nuevamente: ")))


        RLPRODUCTOS.nombreproducto = producto
        formatearproducto(RLPRODUCTOS)
        ALPRODUCTOS.seek(0,2)
        pickle.dump(RLPRODUCTOS, ALPRODUCTOS)
        ALPRODUCTOS.flush()

        decisionprod = input("\n¿Desea ingresar un nuevo producto? Ingrese SI o NO: ").upper()
        while decisionprod != "NO" and decisionprod != "SI": # Validación de datos
            decisionprod = input("\nOpción incorrecta. Ingrese nuevamente: ").upper()
            
        if decisionprod == "NO":
            print("\nProductos ingresados correctamente\n")
            os.system("pause")
            clear()
            opciones_terciario("PRODUCTOS")

def consultaP():
    getsai = os.path.getsize(AFPRODUCTOS)
    RLPRODUCTOS = csproducto()
    if getsai == 0:
        print("No hay nada para mostrar\n")
    
    else:
        ALPRODUCTOS.seek(0,0)
        print("PRODUCTO |     CODIGO DE PRODUCTO")
        print("---------------------------")
    while ALPRODUCTOS.tell() < getsai:
        RLPRODUCTOS = pickle.load(ALPRODUCTOS)
        print(RLPRODUCTOS.nombreproducto, RLPRODUCTOS.codproducto)
    os.system("pause")
    clear()
    opciones_terciario("PRODUCTOS")

# BAJA LÓGICA
def eliminarP(producto):
    if tebuscopos(producto) != -1:
        pos = tebuscopos(producto)
        ALPRODUCTOS.seek(pos,0)
        RLPRODUCTOS = pickle.load(ALPRODUCTOS)
        RLPRODUCTOS.nombreproducto = ""
        RLPRODUCTOS.codproducto = ""
        ALPRODUCTOS.seek(pos,0)
        formatearproducto(RLPRODUCTOS)
        pickle.dump(RLPRODUCTOS, ALPRODUCTOS)
        print(f"\nEl producto {producto} se eliminó correctamente.\n")
        os.system("pause")
        clear()
        opciones_terciario("PRODUCTOS")
    else:
        print("El Producto no se encontró.\n")
        os.system("pause")
        clear()
        opciones_terciario("PRODUCTOS")

def bajaprod():
    getsai = os.path.getsize(AFPRODUCTOS)
    RLPRODUCTOS = csproducto()
    if getsai == 0:
        print("No hay nada para mostrar.\n")
    else:
        ALPRODUCTOS.seek(0,0)
        print("PRODUCTO |       CODIGO PRODUCTO")
        print("---------------------------")
        while ALPRODUCTOS.tell() < getsai:
            RLPRODUCTOS = pickle.load(ALPRODUCTOS)
            print(RLPRODUCTOS.nombreproducto, RLPRODUCTOS.codproducto)
        producto = input("Ingresar el nombre del producto a eliminar: ").upper()
        eliminarP(producto)

def modificarP(producto, nuevoproducto, nuevocod):
    if tebuscopos(producto) != -1:
        pos = tebuscopos(producto)
        ALPRODUCTOS.seek(pos,0)
        RLPRODUCTOS = pickle.load(ALPRODUCTOS)
        RLPRODUCTOS.nombreproducto = nuevoproducto
        RLPRODUCTOS.codproducto = nuevocod

        ALPRODUCTOS.seek(pos,0)
        formatearproducto(RLPRODUCTOS)
        pickle.dump(RLPRODUCTOS, ALPRODUCTOS)

        print(f"El producto {producto} ahora es {nuevoproducto} con código {nuevocod}.\n")
        os.system("pause")
        clear()
        opciones_terciario("PRODUCTOS")
    else:
	    print("El Producto no se encontró.")

def modificacionproducto():

    getsai = os.path.getsize(AFPRODUCTOS)
    RLPRODUCTOS = csproducto()
    if getsai == 0:
        print("No hay nada para mostrar\n")
        
    else:
        ALPRODUCTOS.seek(0,0)
        print("  PRODUCTO    |     CÓDIGO PRODUCTO")
        print("-----------------------------------")
        while ALPRODUCTOS.tell() < getsai:
            RLPRODUCTOS = pickle.load(ALPRODUCTOS)
            print(RLPRODUCTOS.nombreproducto, RLPRODUCTOS.codproducto)
        producto = input("Ingresar el nombre del producto a modificar: ").upper()

        # Verificación de que sea de los ingresados
        while producto == "" or producto.isnumeric() == True or len(producto) > 25:
            producto = input("No es un producto válido. Ingrese nuevamente: ").upper()

        nuevoproducto = input("\nIngresar el nuevo producto: ").upper()
        # Verificación de que sea correcto y no se vaya a repetir
        while nuevoproducto == "" or nuevoproducto.isnumeric() == True or len(nuevoproducto) > 25:
            nuevoproducto = input("No es un producto válido. Ingrese nuevamente: ").upper()

        while tebuscopos(nuevoproducto) != -1:
            nuevoproducto = input("\nProducto ya ingresado. Ingrese nuevamente: ").upper()
            while nuevoproducto == "" or nuevoproducto.isnumeric() == True or len(nuevoproducto) > 25:
                nuevoproducto = input("No es un producto válido. Ingrese nuevamente: ").upper()

        nuevocod = int(verificacioncod(input("\nIngrese el código del producto: ")))
        while tebuscodigo(nuevocod) == True:
            nuevocod = int(verificacioncod(input("Código no válido. Ingrese nuevamente: ")))
        
        modificarP(producto, nuevoproducto, nuevocod)

def menu_productos():

    clear()
    opciones_terciario("PRODUCTOS")
    opcion_terciario = "A"
    while opcion_terciario != "V":
        opcion_terciario = input("Opción: ").upper() # Convertir toda cadena ingresada en mayúscula.
        while opcion_terciario == "" or len(opcion_terciario) > 1: # Validación de datos
            opcion_terciario = input("Opción incorrecta. Ingrese nuevamente: ").upper()
        
        if opcion_terciario == "A": # Alta
            cargarprod()
        elif opcion_terciario == "B": # Baja
            bajaprod()
        elif opcion_terciario == "C": # Consulta
            consultaP()
        elif opcion_terciario == "M": # Modificacion
            modificacionproducto()
        else: # Volver al menú principal
            opcion_terciario = "V"
            administracion()

##### ##### RUBROS ##### ##### 
def menu_rubros():
    clear()
    opciones_terciario("RUBROS")
    opcion_terciario = "A"
    while opcion_terciario != "V":
        opcion_terciario = input("Opción: ").upper() # Convertir toda cadena ingresada en mayúscula.
        while opcion_terciario == "" or len(opcion_terciario) > 1: # Validación de datos
            opcion_terciario = input("Opción incorrecta. Ingrese nuevamente: ").upper()
        
        if opcion_terciario == "A": # Alta
            cargarubro()
        elif opcion_terciario == "B": # Baja
            en_construccion()
            opciones_terciario("RUBROS")
        elif opcion_terciario == "C": # Consulta
            en_construccion()
            opciones_terciario("RUBROS")
        elif opcion_terciario == "M": # Modificacion
            en_construccion()
            opciones_terciario("RUBROS")
        else: # Volver al menú principal
            opcion_terciario = "V"
            administracion()

def cargarubro():
    cargamiento = "SI"
    while cargamiento == "SI":
        nombreR = input("Ingrese el nombre del rubro: ")

        while nombreR == "" or nombreR.isnumeric == True or len(nombreR) > 25 or tebusrubro(nombreR) == True:
            nombreR = input("Nombre del rubro incorrecto. Ingrese nuevamente: ")

        # Verificación de que se ingrese un número
        cod = int(verificacioncod(input("\nIngrese el código del rubro: ")))
        while tebuscodR(cod) == True:
            cod = int(verificacioncod(input("Código no válido. Ingrese nuevamente: ")))


        RLRUBROS = csrubro()

        RLRUBROS.codigorubro = cod
        RLRUBROS.nombrerubro = nombreR
        formatearrubro(RLRUBROS)
        ALRUBROS.seek(0,2)
        pickle.dump(RLRUBROS, ALRUBROS)
        ALRUBROS.flush()
        t = os.path.getsize(AFRUBROS)
        cargamiento = input("\n¿Desea ingresar otro rubro? Ingrese SI o NO: ").upper()
        while cargamiento != "NO" and cargamiento != "SI": # Validación de datos
                cargamiento = input("Opción incorrecta. Ingrese nuevamente: ").upper()
                
        if cargamiento == "NO":
            print("\nRubros ingresados correctamente\n")
            os.system("pause")
            clear()
            opciones_terciario("RUBROS")


##### ##### Rubro por producto ##### ##### 
def menu_rubrosxproducto():
    clear()
    opciones_terciario("RUBROS POR PRODUCTO")
    opcion_terciario = "A"
    while opcion_terciario != "V":
        opcion_terciario = input("Opción: ").upper() # Convertir toda cadena ingresada en mayúscula.
        while opcion_terciario == "" or len(opcion_terciario) > 1: # Validación de datos
            opcion_terciario = input("Opción incorrecta. Ingrese nuevamente: ").upper()
        
        if opcion_terciario == "A": # Alta
            cargaRxP()
        elif opcion_terciario == "B": # Baja
            en_construccion()
            opciones_terciario("RUBROS POR PRODUCTO")
        elif opcion_terciario == "C": # Consulta
            en_construccion()
            opciones_terciario("RUBROS POR PRODUCTO")
        elif opcion_terciario == "M": # Modificacion
            en_construccion()
            opciones_terciario("RUBROS POR PRODUCTO")
        else: # Volver al menú principal
            opcion_terciario = "V"
            administracion()

def cargaRxP():
    cargamiento = "SI"
    while cargamiento == "SI":

#Verificación códigos 
        codrub = int(verificacioncod(input("Ingrese el código del rubro: ")))
        while tebuscodR(codrub) == False:
            codrub = int(verificacioncod(input("Código de rubro no encontrado. Ingrese nuevamente: ")))

        codprod = int(verificacioncod(input("Ingrese el código del producto: ")))
        while tebuscodigo(codprod) == False: 
            codprod = int(verificacioncod(input("Código de producto no encontrado. Ingrese nuevamente: ")))        

# Valores verificación
        valormax = int(verificacioncod(input("Ingrese el valor máximo admitido: ")))

        while valormax > 100:
            valormax = float(verificacioncod(input("Error - el valor máximo no puede ser mayor a 100. Volver a ingresar: ")))

        valormin = input("Ingrese el valor mínimo admitido: ")
        valormin = float(verificacioncod(valormin))

        while valormin < 0 or valormin > 99:
            valormin = float(verificacioncod(input("El valor mínimo no puede ser menor a 0.\nError - Volver a ingresar: ")))

        while valormin > valormax:
            valormin = float(verificacioncod(input("El valor mínimo no puede ser mayor al valor máximo.\nError - Volver a ingresar: ")))
            

        RLRUBROSXPRODUCTO = csrubroxproducto()

        RLRUBROSXPRODUCTO.codigorubro = codrub
        RLRUBROSXPRODUCTO.codigoproducto = codprod
        RLRUBROSXPRODUCTO.valormax = valormax
        RLRUBROSXPRODUCTO.valormin = valormin
        formatearRxP(RLRUBROSXPRODUCTO)
        ALRUBROSXPRODUCTO.seek(0,2)
        pickle.dump(RLRUBROSXPRODUCTO, ALRUBROSXPRODUCTO)
        ALRUBROSXPRODUCTO.flush()

        cargamiento = input("\n¿Desea ingresar otro rubro por producto? Ingrese SI o NO: ").upper()
        while cargamiento != "NO" and cargamiento != "SI": # Validación de datos
                cargamiento = input("Opción incorrecta. Ingrese nuevamente: ").upper()
                
        if cargamiento == "NO":
            print("\nRubros por productos ingresados correctamente\n")
            os.system("pause")
            clear()
            opciones_terciario("RUBROS POR PRODUCTO")



#Ordenamiento secuencial de rubros, esta hecho por codigo del rubro:
def ordenRubro():
    ALRUBROS.seek(0,0)
    aux = pickle.load(ALRUBROS)
    tamReg= ALRUBROS.tell()
    tamArc= os.path.getsize(AFRUBROS)
    cantReg = tamArc//tamReg 
    for i in range (0,cantReg-1):
        for j in range (i+1, cantReg):
            ALRUBROS.seek(i*tamReg, 0)
            auxi = pickle.load(ALRUBROS)
            ALRUBROS.seek(j*tamReg, 0)
            auxj = pickle.load(ALRUBROS)
            if (auxi.codigorubro>auxj.codigorubro):
                ALRUBROS.seek(i*tamReg, 0)
                pickle.dump(auxj,ALRUBROS)
                ALRUBROS.seek(j*tamReg, 0)
                pickle.dump(auxi,ALRUBROS)

##### ##### SILOS ##### ##### 
def cargasilos():
    cargamiento = "SI"
    while cargamiento == "SI":
        codsil = int(verificacioncod(input("\nIngrese el código del silo: ")))
    
        while tebusilo(codsil) == True:
            codsil = int(verificacioncod(input("Código en uso. Ingrese nuevamente: ")))

        codprod = int(verificacioncod(input("\nIngrese el código del producto: ")))

        while tebuscodigo(codprod) == False:
            codprod = int(verificacioncod(input("Código no encontrado. Ingrese nuevamente: ")))

        nombreS = input("Ingrese el nombre del silo: ")
        while nombreS.isnumeric() == True or len(nombreS) > 25:
            nombreS = input("Nombre incorrecto. Ingrese nuevamente: ")

        stockS = int(verificacioncod(input("\nIngrese el stock del silo: ")))

        RLSILOS = cssilo()

        RLSILOS.codigosilo = codsil
        RLSILOS.codproducto = codprod
        RLSILOS.nombresilo = nombreS
        RLSILOS.stock = stockS
        formatearsilos(RLSILOS)
        ALSILOS.seek(0,2)
        pickle.dump(RLSILOS, ALSILOS)
        ALSILOS.flush()

        cargamiento = input("\n¿Desea ingresar otro silo? Ingrese SI o NO: ").upper()
        while cargamiento != "NO" and cargamiento != "SI": # Validación de datos
                cargamiento = input("Opción incorrecta. Ingrese nuevamente: ").upper()
                
        if cargamiento == "NO":
            print("\nSilos ingresados correctamente\n")
            os.system("pause")
            clear()
            opciones_terciario("SILOS")

def menu_silos():
    clear()
    opciones_terciario("SILOS")
    opcion_terciario = "A"
    while opcion_terciario != "V":
        opcion_terciario = input("Opción: ").upper() # Convertir toda cadena ingresada en mayúscula.
        while opcion_terciario == "" or len(opcion_terciario) > 1: # Validación de datos
            opcion_terciario = input("Opción incorrecta. Ingrese nuevamente: ").upper()
        
        if opcion_terciario == "A": # Alta
            cargasilos()
        elif opcion_terciario == "B": # Baja
            en_construccion()
            opciones_terciario("SILOS")
        elif opcion_terciario == "C": # Consulta
            en_construccion()
            opciones_terciario("SILOS")
        elif opcion_terciario == "M": # Modificacion
            en_construccion()
            opciones_terciario("SILOS")
        else: # Volver al menú principal
            opcion_terciario = "V"
            administracion()


##### ##### BÚSQUEDAS ##### #####
#funcion busqueda dicotomica de rubro
def BuscaDico(cod):
    cod = int(cod)
    ALRUBROS.seek(0,0)
    RLRUBROS= pickle.load(ALRUBROS)
    tamReg= ALRUBROS.tell()
    tamArc= os.path.getsize(AFRUBROS)
    cantReg= tamArc//tamReg
    inf= 0
    sup= cantReg-1
    med= (inf+sup)//2
    ALRUBROS.seek(med*tamReg, 0)
    RLRUBROS= pickle.load(ALRUBROS)
    while (inf<sup) and (int(RLRUBROS.codigorubro) != cod):
        if cod<int(RLRUBROS.codigorubro):
            sup=med-1
        else: 
            inf= med+1
        med=(sup+inf)//2
        ALRUBROS.seek(med*tamReg, 0)
        RLRUBROS= pickle.load(ALRUBROS)
    if int(RLRUBROS.codigorubro)==cod:
        return med*tamReg
    else: 
        return -1
# dicotomica de RUBROS
def busconombre(cod):
    pos = BuscaDico(cod)
    ALRUBROS.seek(pos, 0)
    RL = pickle.load(ALRUBROS)
    return RL.nombrerubro

def busconombreprod(cod):
    pos = tebuscopos2(cod)
    ALPRODUCTOS.seek(pos, 0)
    RL = pickle.load(ALPRODUCTOS)
    return RL.nombreproducto

# búsquedas de patente
def tebuscopos(producto):
    producto = producto.ljust(25, ' ')
    getsai = os.path.getsize(AFPRODUCTOS)
    ALPRODUCTOS.seek(0,0)
    RLPRODUCTOS = csproducto()
    pos = -1
    if getsai > 0:
        while ALPRODUCTOS.tell() < getsai and RLPRODUCTOS.nombreproducto != producto:
            pos = ALPRODUCTOS.tell()
            RLPRODUCTOS = pickle.load(ALPRODUCTOS)
        if RLPRODUCTOS.nombreproducto == producto:
            return pos
        else:
            return -1
    else:
        return -1

def tebuscopos2(codigo):
    codigo = codigo.ljust(5, ' ')
    getsai = os.path.getsize(AFPRODUCTOS)
    ALPRODUCTOS.seek(0,0)
    RLPRODUCTOS = csproducto()
    pos = -1
    if getsai > 0:
        while ALPRODUCTOS.tell() < getsai and RLPRODUCTOS.codproducto != codigo:
            pos = ALPRODUCTOS.tell()
            RLPRODUCTOS = pickle.load(ALPRODUCTOS)
        if RLPRODUCTOS.codproducto == codigo:
            return pos
        else:
            return -1
    else:
        return -1

# de AFRUBRO
def tebusrubro(nombreR):
    nombreR = nombreR.ljust(25, ' ')
    getsai = os.path.getsize(AFRUBROS)
    ALRUBROS.seek(0,0) 
    RLRUBROS = csrubro()
    if getsai > 0:
        while ALRUBROS.tell() < getsai and RLRUBROS.nombrerubro != nombreR:
            RLRUBROS = pickle.load(ALRUBROS)
        if RLRUBROS.nombrerubro == nombreR:
            return True
        else:
            return False
    else:
        return False

# de AFOPERACIONES
def buscapatente(npat):
    npat = npat.ljust(7, ' ')
    getsai = os.path.getsize(AFOPERACIONES)
    ALOPERACIONES.seek(0,0) 
    RLOPERACIONES = csoperacion()
    pos = 0
    if getsai > 0:
        while ALOPERACIONES.tell() < getsai and RLOPERACIONES.patente != npat:
            pos = ALOPERACIONES.tell()
            RLOPERACIONES = pickle.load(ALOPERACIONES)
        if RLOPERACIONES.patente == npat:
            return pos
        else:
            return -1
    else:
        return -1

# Búsqueda de código de AFPRODUCTO
def tebuscodigo(codigo):
    codigo = str(codigo)
    codigo = codigo.ljust(5, ' ')
    getsai = os.path.getsize(AFPRODUCTOS)
    ALPRODUCTOS.seek(0,0) 
    RLPRODUCTOS = csproducto()
    if getsai > 0:
        while ALPRODUCTOS.tell() < getsai and RLPRODUCTOS.codproducto != codigo:
            RLPRODUCTOS = pickle.load(ALPRODUCTOS)
        if RLPRODUCTOS.codproducto == codigo:
            return True
        else:
            return False
    else:
        return False

# Búsqueda de código de Reportes
def tereportodigo(codigo):
    codigo = str(codigo)
    codigo = codigo.ljust(5, ' ')
    getsai = os.path.getsize(AFREPORTES)
    pos = 0
    ALREPORTES.seek(0,0) 
    RLREPORTES = csreporte()
    if getsai > 0:
        while ALREPORTES.tell() < getsai and RLREPORTES.codproducto != codigo:
            pos = ALREPORTES.tell()
            RLREPORTES = pickle.load(ALREPORTES)
        if RLREPORTES.codproducto == codigo:
            return pos
        else:
            return -1
    else:
        return -1

# de AFSILOS
def buscosilo(codigo):
    codigo = str(codigo)
    codigo = codigo.ljust(5, ' ')
    getsai = os.path.getsize(AFSILOS)
    ALSILOS.seek(0,0)
    pos = 0 
    RLSILOS = cssilo()
    if getsai > 0:
        while ALSILOS.tell() < getsai and RLSILOS.codproducto != codigo:
            pos = ALSILOS.tell()
            RLSILOS = pickle.load(ALSILOS)
        if RLSILOS.codproducto == codigo:
            return pos
        else:
            return -1
    else:
        return -1

# de AFRUBRO
def tebuscodR(cod):
    cod = str(cod)
    cod = cod.ljust(5, ' ')
    getsai = os.path.getsize(AFRUBROS)
    ALRUBROS.seek(0,0) 
    RLRUBROS = csrubro()
    if getsai > 0:
        while ALRUBROS.tell() < getsai and RLRUBROS.codigorubro != cod:
            RLRUBROS = pickle.load(ALRUBROS)
        if RLRUBROS.codigorubro == cod:
            return True
        else:
            return False
    else:
        return False

# de AFSILOS
def tebusilo(codsil):
    codsil = str(codsil)
    codsil = codsil.ljust(5, ' ')
    getsai = os.path.getsize(AFSILOS)
    ALSILOS.seek(0,0) 
    RLSILOS = cssilo()
    if getsai > 0:
        while ALSILOS.tell() < getsai and RLSILOS.codigosilo != codsil:
            RLSILOS = pickle.load(ALSILOS)
        if RLSILOS.codigosilo == codsil:
            return True
        else:
            return False
    else:
        return False

# de AFOPERACIONES
def ayudaayuda(patente, fecha):
    patente = patente.ljust(7, ' ')
    if buscapatente(patente) != -1:
        pospat = buscapatente(patente)
        ALOPERACIONES.seek(0, pospat)
        RL = pickle.load(ALOPERACIONES)
        if RL.patente == patente and RL.fechacupo == fecha:
            return True
        else:
            return False
        
    else:
        return False

##### ##### CUPOS ##### ##### 
def cupos():
    clear()
    print(AMARILLO + "----- MENÚ DE CUPOS -----" + BLANCO)
    decisioncup = input("\n¿Desea ingresar un cupo? Ingrese SI o NO: ").upper()
    while decisioncup != "SI" and decisioncup != "NO":  # Validación de datos
        decisioncup = input("Ingrese una opción correcta: ").upper()

    while decisioncup == "SI":
        clear()
        nuevapatente = input("\nIngresar la patente del camión: ").upper()
        while len(nuevapatente) < 6 or len(nuevapatente) > 7: # Comprobamos la longitud de la patente
            nuevapatente = input("Error con la longitud de la patente. Por favor ingresar nuevamente: ").upper()
        else:
            RLOPERACIONES = csoperacion()
            fecharep = verificacionFecha("\nIngrese la fecha actual para recepción, formato <dd/mm/yyyy>: ")
            if ayudaayuda(nuevapatente, fecharep) == True:
                print("Cupo ya otorgado en esa fecha.")
            else:
                codigo = int(verificacioncod(input("\nIngrese el código del producto: ")))
                if tebuscodigo(codigo) == False:
                    print("No se encontró el producto con el código dado. Fin de la operación.")
                else:
                    RLOPERACIONES.patente = nuevapatente
                    RLOPERACIONES.fechacupo = fecharep
                    RLOPERACIONES.codproducto = codigo
                    RLOPERACIONES.estado = "P"
                    if tereportodigo(codigo) == -1:
                        ALREPORTES.seek(0, 2)
                        RLREPORTES = csreporte()
                        RLREPORTES.codproducto = codigo
                        formateareportes(RLREPORTES)
                        pickle.dump(RLREPORTES, ALREPORTES)
                        ALREPORTES.flush()
                    formatearoperaciones(RLOPERACIONES)
                    pickle.dump(RLOPERACIONES, ALOPERACIONES)
                    ALOPERACIONES.flush()
                    print(f"Se ingresó el Cupo, código {codigo} con patente {nuevapatente}\n")
            decisioncup = input("\n¿Desea ingresar un nuevo cupo? Ingrese SI o NO: ").upper()
            while decisioncup != "SI" and decisioncup != "NO":  # Validación de datos
                decisioncup = input("Ingrese una opción correcta: ").upper()

    cuposctm = input("\nCupos ingresados correctamente - Presione cualquier tecla para continuar\n")
    clear()


##### ##### ADMINISTRACIÓN ##### ##### 
def administracion():
    
    clear()
    opciones_admin()
    opcion_admin = "A"
    while opcion_admin != "V":
        
        opcion_admin = input("Opción: ").upper() # Convertir toda cadena ingresada en mayúscula.

        # Validación de datos
        while opcion_admin == "" or (opcion_admin > "G" and opcion_admin < "V") or opcion_admin > "V" or opcion_admin.isnumeric() == True or len(opcion_admin) > 1:
            opcion_admin = input("Opción incorrecta. Ingrese nuevamente: ").upper()
 
        if opcion_admin == "A": # Titulares
            opcion_admin = "V"
            en_construccion()
        elif opcion_admin == "B": # Producto
            opcion_admin = "V"
            menu_productos()
        elif opcion_admin == "C": # Rubros
            opcion_admin = "V"
            menu_rubros()
        elif opcion_admin == "D": # Rubros por producto
            opcion_admin = "V"
            menu_rubrosxproducto()
        elif opcion_admin == "E": # Silos
            opcion_admin = "V"
            menu_silos()
        elif opcion_admin == "F": # Sucursales
            opcion_admin = "V"
            en_construccion()
        elif opcion_admin == "G": # Producto por titular
            opcion_admin = "V"
            en_construccion()
        else:
            opcion_admin = "V"
            clear()

##### ##### REGISTRAR CALIDAD ##### ##### 
def regcalidad():
    clear()
    opcall = input("\n¿Desea registrar la calidad? Ingrese SI o NO: ").upper()
    while opcall != "NO" and opcall != "SI":
        opcall = input("Error. Ingresar una respuesta correcta: ").upper()
    while opcall == "SI":
        patentecal = input("\nIngrese la patente a registrar: ").upper()
        while len(patentecal) < 6 or len(patentecal) > 7:
            patentecal = input("La patente no es válida, ingresar nuevamente: ").upper()
        if buscapatente(patentecal) != -1:
            ALOPERACIONES.seek(buscapatente(patentecal), 0)
            RLOPERACIONES = pickle.load(ALOPERACIONES)
            if RLOPERACIONES.estado == "A":
                flaggeado = 0
                ordenRubro()
                elcod = RLOPERACIONES.codproducto
                ALRUBROSXPRODUCTO.seek(0)
                getsai = os.path.getsize(AFRUBROSXPRODUCTO)

                while ALRUBROSXPRODUCTO.tell() < getsai:
                    RLRUBROSXPRODUCTO = pickle.load(ALRUBROSXPRODUCTO)
                    if RLRUBROSXPRODUCTO.codigoproducto == elcod:
                        print("CODIGO RUBRO  | NOMBRE DEL RUBRO")
                        tebuscod = RLRUBROSXPRODUCTO.codigorubro
                        tebuscod = tebuscod.ljust(5, ' ')
                        print(RLRUBROSXPRODUCTO.codigorubro, "           ", busconombre(tebuscod))
                        dichovalor = float(input("Ingrese un valor para este rubro: "))
                        if dichovalor > float(RLRUBROSXPRODUCTO.valormax) or dichovalor < float(RLRUBROSXPRODUCTO.valormin):
                            flaggeado += 1
                
                if flaggeado == 0:
                    print("\nEl camión ha sido aprobado.")
                    RLOPERACIONES.estado = "C"
                    ALOPERACIONES.seek(buscapatente(patentecal), 0)
                    pickle.dump(RLOPERACIONES, ALOPERACIONES)
                    ALOPERACIONES.flush()
                else:
                    print("El camión ha sido rechazado.")
                    RLOPERACIONES.estado = "R"
                    ALOPERACIONES.seek(buscapatente(patentecal), 0)
                    pickle.dump(RLOPERACIONES, ALOPERACIONES)
                    ALOPERACIONES.flush()
            else:
                print("El estado del cupo es incorrecto.")
        else:
            print("La patente no existe")
        opcall = input("\n¿Desea registrar la calidad de otra patente? Ingrese SI o NO: ").upper()
        clear()

##### ##### REGISTRAR PESO BRUTO ##### ##### 
def regpesobruto():
    clear()
    decisionregp = input("\n¿Registrar un nuevo peso bruto? Ingrese SI o NO: ").upper()
    while decisionregp != "NO" and decisionregp != "SI": # Validación del sí
        decisionregp = input("Error. Ingresar una respuesta correcta: ").upper()
    while decisionregp == "SI":
        pato = input("\nIngresar patente a registrar: ").upper()
        while len(pato) < 6 or len(pato) > 7:
            pato = input("La patente no es válida, ingresar nuevamente: ").upper()

        if buscapatente(pato) != -1:
            ALOPERACIONES.seek(buscapatente(pato), 0)
            RLOPERACIONES = pickle.load(ALOPERACIONES)
            if RLOPERACIONES.estado == "C":
                pesobru= input("\nIngrese el peso bruto del camión: ")
                while pesobru.isnumeric() == False or pesobru == "" or int(pesobru) == 0 or int(pesobru) < 0:
                    pesobru = input("Error. Ingrese un peso correcto: ")

                pesobru = int(pesobru)

                ALOPERACIONES.seek(buscapatente(pato), 0)
                RLOPERACIONES = pickle.load(ALOPERACIONES)
                RLOPERACIONES.bruto = pesobru
                RLOPERACIONES.estado = "B"
                formatearoperaciones(RLOPERACIONES)
                ALOPERACIONES.seek(buscapatente(pato), 0)
                pickle.dump(RLOPERACIONES, ALOPERACIONES) 
                ALOPERACIONES.flush()
                print(f"\nSe registró el peso bruto de {pato} con {pesobru} kg con éxito.\n")
            else:
                print("El estado de la patente es incorrecto.")
        else:
            print("No se encontró la patente.")

        decisionregp = input("\n¿Registrar un nuevo peso bruto? Ingrese SI o NO: ").upper()
        while decisionregp != "NO" and decisionregp != "SI": # Validación del sí
            decisionregp = input("Error. Ingresar una respuesta correcta: ").upper()
        clear()

##### ##### REGISTRAR TARA ##### ##### 
def regtara():
    clear()
    decisionregt = input("¿Registrar una nueva tara? Ingrese SI o NO: ").upper()
    while decisionregt != "NO" and decisionregt != "SI": # Validación del sí
        decisionregt = input("Error. Ingresar una respuesta correcta: ").upper()
    while decisionregt == "SI":
        patentereg = input("\nIngresar patente a registrar: ").upper()
        while len(patentereg) < 6 or len(patentereg) > 7:
            patentereg = input("La patente no es válida, ingresar nuevamente: ").upper()
        if buscapatente(patentereg) != -1:
            ALOPERACIONES.seek(buscapatente(patentereg), 0)
            RLOPERACIONES = pickle.load(ALOPERACIONES)
            if RLOPERACIONES.estado == "B":
                tara = input("\nIngrese la tara de esta patente: ")

                while tara.isnumeric() == False or int(tara) < 0 or int(tara) == 0:
                    tara = input("El valor de la tara es incorrecto, ingrese nuevamente: ")
                
                tara = int(tara)

                while int(RLOPERACIONES.bruto) < tara:
                    tara = int(input("El valor de la tara es incorrecto, ingrese nuevamente: "))
                pesoneto = int(RLOPERACIONES.bruto) - tara
                posilo = buscosilo(RLOPERACIONES.codproducto)
                if posilo != -1:
                    posrep = tereportodigo(RLOPERACIONES.codproducto)
                    ALREPORTES.seek(posrep, 0)
                    RLREPORTES = pickle.load(ALREPORTES)
                    RLREPORTES.pesonetototal = int(RLREPORTES.pesonetototal) + pesoneto
                    if int(RLREPORTES.menorpesoneto) > pesoneto:
                        RLREPORTES.menorpesoneto = pesoneto
                        RLREPORTES.patentemenor = RLOPERACIONES.patente
                    ALREPORTES.seek(posrep, 0)
                    ALSILOS.seek(posilo, 0)
                    RLSILOS = pickle.load(ALSILOS)
                    RLSILOS.stock = int(RLSILOS.stock) + pesoneto
                    RLOPERACIONES.estado = "F"
                    ALSILOS.seek(posilo, 0)
                    ALOPERACIONES.seek(buscapatente(patentereg), 0)
                    formatearsilos(RLSILOS)
                    formateareportes(RLREPORTES)
                    pickle.dump(RLREPORTES, ALREPORTES)
                    pickle.dump(RLSILOS, ALSILOS)
                    pickle.dump(RLOPERACIONES, ALOPERACIONES)
                    ALREPORTES.flush()
                    ALSILOS.flush()
                    ALOPERACIONES.flush()
                    print(f"\nSe ingresó el peso neto de {pesoneto} kg con éxito.\n")
                else:
                    print("No hay un silo correspondiente al producto de esta patente.")
            else:
                print("El estado de la patente es incorrecto.")
        else:
            print("No se encontró la patente.")


        decisionregt = input("\n¿Registrar una nueva tara? Ingrese SI o NO: ").upper()
        while decisionregt != "NO" and decisionregt != "SI": # Validación del sí
            decisionregt = input("Error. Ingresar una respuesta correcta: ").upper()
        clear()


##### ##### RECEPCIÓN ##### ##### 
def recepcion():
    clear()
    camiones = input("\n¿Comenzar a ingresar los camiones? Ingrese SI o NO: ").upper()
    while camiones != "NO" and camiones != "SI": # Validación del sí
        camiones = input("Error. Ingresar una respuesta correcta: ").upper()

    while camiones != "NO":
        clear()
        print(ROJO + f"\nDatos del camión" + BLANCO)
        PATENTE = input("Ingresar número de patente ").upper()

        while len(PATENTE) < 6 or len(PATENTE) > 7:
            PATENTE = input("La patente no es válida, ingresar nuevamente: ").upper()

        if buscapatente(PATENTE) != -1:
            pospat = buscapatente(PATENTE)
            ALOPERACIONES.seek(pospat, 0)
            RLOPERACIONES = pickle.load(ALOPERACIONES)

            if RLOPERACIONES.fechacupo == datetime.date.today() and RLOPERACIONES.estado == "P":
                posrep = tereportodigo(RLOPERACIONES.codproducto)
                ALREPORTES.seek(posrep, 0)
                RLREPORTES = pickle.load(ALREPORTES)
                RLREPORTES.cantcamiones = int(RLREPORTES.cantcamiones) + 1
                RLOPERACIONES.estado = "A"
                ALREPORTES.seek(posrep, 0)
                ALOPERACIONES.seek(pospat, 0)
                formateareportes(RLREPORTES)
                pickle.dump(RLOPERACIONES, ALOPERACIONES)
                pickle.dump(RLREPORTES, ALREPORTES)
                ALOPERACIONES.flush()
                ALREPORTES.flush()
                print(f"\nSe actualizó el estado del camión {PATENTE} con éxito.")
            else:
                print("El camión tiene una fecha o estado incorrecto.")
        else: 
            print("No se encontró el camión.")

        camiones = input("\n¿Desea ingresar otro camión? Ingrese SI o NO: ").upper()
        while camiones != "NO" and camiones != "SI": # Validación del sí
            camiones = input("Error. Ingresar una respuesta correcta: ").upper()
    clear()

##### ##### REPORTES ##### ##### 
def buscantcupos():
    cont = 0
    ALOPERACIONES.seek(0)
    RLOPERACIONES = csoperacion()
    t = os.path.getsize(AFOPERACIONES)
    while ALOPERACIONES.tell() < t:
        RLOPERACIONES = pickle.load(ALOPERACIONES)
        cont += 1
    return cont

def buscantcamiones():
    cont = 0
    ALOPERACIONES.seek(0)
    RLOPERACIONES = csoperacion()
    t = os.path.getsize(AFOPERACIONES)
    while ALOPERACIONES.tell() < t:
        RLOPERACIONES = pickle.load(ALOPERACIONES)
        if RLOPERACIONES.estado != "P":
            cont += 1
    return cont    

def reportes():

    clear()
    print(VERDE + "----- REPORTES -----" + BLANCO)
    print("- Cantidad de cupos otorgados: ", buscantcupos())
    print("- Cantidad de camiones recibidos: ", buscantcamiones())
    print(" ")
    print("NOMBRE      | CANTIDAD X CAMION | PESO NETO TOTAL | PROMEDIO PESO NETO | PATENTE MENOR")
    print("--------------------------------------------------------------------------------------")
    t = os.path.getsize(AFREPORTES)
    ALREPORTES.seek(0)
    while t > ALREPORTES.tell():
        RLREPORTES = pickle.load(ALREPORTES)
        promediopeson = 0.0
        if int(RLREPORTES.cantcamiones) != 0:
            promediopeson = float(RLREPORTES.pesonetototal) / float(RLREPORTES.cantcamiones)
        print(busconombreprod(RLREPORTES.codproducto), RLREPORTES.cantcamiones, "              ", RLREPORTES.pesonetototal, "      ", promediopeson, "      ", RLREPORTES.patentemenor)
    print(" ")
    os.system("pause")
    clear()

##### ##### LISTADO SILOS Y RECHAZOS ##### ##### 
def silomayor():
    t = os.path.getsize(AFSILOS)
    posmayor = 0
    ALSILOS.seek(0)
    mayor = 0
    RLSILOS = cssilo()
    while ALSILOS.tell() < t:
        pos = ALSILOS.tell()
        RLSILOS = pickle.load(ALSILOS)
        if int(RLSILOS.stock) > mayor:
            mayor = int(RLSILOS.stock)
            posmayor = pos
    return posmayor

def listadoSilos():
    pos = silomayor()
    ALSILOS.seek(pos, 0)
    RLSILOS = pickle.load(ALSILOS)
    print("Este es el silo con mayor stock:\n")
    print("CÓDIGO DEL SILO | CÓDIGO DEL PRODUCTO | NOMBRE DEL SILO |        STOCK      |")
    print("-----------------------------------------------------------------------------")
    print(RLSILOS.codigosilo, "           ", RLSILOS.codproducto, "               ", RLSILOS.nombresilo, RLSILOS.stock, "\n")
    decision = input("¿Desea buscar camiones rechazados por fecha? Ingrese SI o NO: ").upper()
    while decision != "SI" and decision != "NO":
        decision = input("Opción incorrecta, ingrese nuevamente: ").upper()
    while decision == "SI":
        flag = 0
        fecha = verificacionFecha("Ingrese la fecha a buscar: ")
        ALOPERACIONES.seek(0)
        RLOPERACIONES = csoperacion()
        t = os.path.getsize(AFOPERACIONES)
        print("PATENTE   | ESTADO | FECHA DE RECHAZO")
        print("-------------------------------------")
        while ALOPERACIONES.tell() < t:
            RLOPERACIONES = pickle.load(ALOPERACIONES)
            if RLOPERACIONES.fechacupo == fecha and RLOPERACIONES.estado == "R":
                print(RLOPERACIONES.patente, "    ", RLOPERACIONES.estado, "        ", RLOPERACIONES.fechacupo)
                flag = flag + 1
        if flag == 0:
            print("\nNo hay nada para mostrar.")
        decision = input("\n¿Desea buscar otra fecha? Ingrese SI o NO: ").upper()

##### ##### MAIN ##### ##### 
def cerrarArchivos():
    ALOPERACIONES.close()
    ALPRODUCTOS.close()
    ALRUBROS.close()
    ALRUBROSXPRODUCTO.close()
    ALSILOS.close()
    ALREPORTES.close()

def main():

    clear()
    opcion = "1"

    while opcion != "0":
        opciones_menu()
        opcion = input("Opción: ")

    # Validación de datos
        while opcion == "" or len(opcion) > 1 or opcion.isnumeric() == False:
            opcion = input("Opción incorrecta. Ingresar nuevamente: ")
        while int(opcion) < 0 or int(opcion) > 9:
            opcion = input("Opción incorrecta. Ingresar nuevamente: ")

    # Menú de opciones
        if opcion == "1": # Administración
            administracion() # Se ejecuta el módulo administración.
            
        elif opcion == "2": # Entrega de cupos
            cupos()

        elif opcion == "3": # Recepción
            recepcion() 

        elif opcion == "4": # Registrar calidad
            regcalidad()

        elif opcion == "5": # Registrar peso bruto
            regpesobruto() 

        elif opcion == "6": # Registrar descarga
            en_construccion() 

        elif opcion == "7": # Registrar tara
            regtara() 

        elif opcion == "8": # Reportes
            reportes()
        
        elif opcion == "9": # Listado de Silos y Rechazos
            listadoSilos()

        else: # Fin del programa
            cerrarArchivos()
            print("Fin del programa.")
    clear()

        
# Ejecución del programa principal.
main()