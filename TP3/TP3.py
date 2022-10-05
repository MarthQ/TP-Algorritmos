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
from turtle import pos

# Estética del programa
# función CLEAR para limpiar pantalla
clear = lambda: os.system('cls')

# variables de COLOR para los print() de consola
VERDE = '\033[92m'
AMARILLO = '\033[93m'
ROJO = '\033[91m'
BLANCO = '\033[0m'

# Registros
class csoperacion:
    def __init__(self):
        self.patente = "" # 7 caracteres
        self.codproducto = 0
# ver uso de datetime para esto (tal vez es una paja y usamos el string tradicional, es un datazo este comentario)
        self.fechacupo = datetime.datetime(1,1,1) # es una FECHA AAAAAAAAAA
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


# Apertura de archivos 
AFOPERACIONES = os.getcwd() + "\\TP3\\OPERACIONES.DAT"
if os.path.exists(AFOPERACIONES) == True:
    ALOPERACIONES = open(AFOPERACIONES, "r+b")
else:
    ALOPERACIONES = open(AFOPERACIONES, "w+b")

RLOPERACIONES = csoperacion()

AFPRODUCTOS = os.getcwd() + "\\TP3\\PRODUCTOS.DAT"
if os.path.exists(AFPRODUCTOS) == True:
    ALPRODUCTOS = open(AFPRODUCTOS, "r+b")
else:
    ALPRODUCTOS = open(AFPRODUCTOS, "w+b")

RLPRODUCTOS = csproducto()

AFRUBROS = os.getcwd() + "\\TP3\\RUBROS.DAT"
if os.path.exists(AFRUBROS) == True:
    ALRUBROS = open(AFRUBROS, "r+b")
else:
    ALRUBROS = open(AFRUBROS, "w+b")
RLRUBROS = csrubro()

AFRUBROSXPRODUCTO = os.getcwd() + "\\TP3\\RUBROS-X-PRODUCTO.DAT"
if os.path.exists(AFRUBROSXPRODUCTO) == True:
    ALRUBROSXPRODUCTO = open(AFRUBROSXPRODUCTO, "r+b")
else:
    ALRUBROSXPRODUCTO = open(AFRUBROSXPRODUCTO, "w+b")
RLRUBROSXPRODUCTO = csrubroxproducto()

AFSILOS = os.getcwd() + "\\TP3\\SILOS.DAT"
if os.path.exists(AFSILOS) == True:
    ALSILOS = open(AFSILOS, "r+b")
else:
    ALSILOS = open(AFSILOS, "w+b")
RLSILOS = cssilo()

# Formateos
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
#       self.patente = "" # 7 caracteres
#         self.codproducto = 0
# # ver uso de datetime para esto (tal vez es una paja y usamos el string tradicional, es un datazo este comentario)
#         self.fechacupo = datetime.datetime(1,1,1) # es una FECHA AAAAAAAAAA
#         self.estado = "" # char
#         self.bruto = 0
#         self.tara = 0
    RL.patente = str(RL.patente)
    RL.patente = RL.patente.ljust(7, ' ')
    RL.codproducto = str(RL.codproducto)
    RL.codproducto = RL.codproducto.ljust(5, ' ')
    RL.bruto = str(RL.bruto)
    RL.bruto = RL.bruto.ljust(5, ' ')
    RL.tara = str(RL.tara)
    RL.tara = RL.tara.ljust(5, ' ')


# probando Date para la fecha:
# def date():
#     global fecha
#     flag=True
#     while flag:
#         try:
#             fecha=input("Ingrese fecha(DD,MM,AAAA):")
#             datetime.datetime.strptime(fecha, '%d/%m/%Y')
#             print("Fecha valida")
#             flag = False
#         except ValueError:
#             print("Fecha invalida.")
# lo copio como en el video, dsp vemos si lo dejamos o lo sacamos al carajo. pone automaticamente las barras /
# dia,mes,anio= fecha.split('/')


# eta e' la de jp casañas ft. sofi eeeeeeeeeeeeeeeeeeeeeee

def validarFecha(mensaje):

    os.system("cls")
    fecha = input(mensaje)
    o = fecha.split("/", 3)
    while(len(o[0]) > 2 or len(o[1]) > 2 or len(o[2]) > 4 or len(o[2]) < 4) or not (o[0].isnumeric() and o[1].isnumeric() and o[2].isnumeric() or not (int(o[0]) in range(1, 32) and int(o[1]) in range(1, 13))):
        print("El formato de la fecha es incorrecto")
        fecha = input(mensaje)
        o = fecha.split("/", 3)
    return datetime.datetime.strptime(fecha, "%d/%m/%Y").date()


# procedimiento inicializadodatoscam()
# VAR:
# total_camiones, total_camiones_maiz, total_camiones_soja, total_camiones_cebada, total_camiones_girasol, total_camiones_trigo,camion: Integer
# PATENTEMAYOR, PATENTEMENOR: String
# total_neto_maiz, total_neto_soja: Float
# promedio_neto_soja, promedio_neto_maiz: Float
def inicializodatoscam():
    global total_camiones, total_camiones_maiz, total_camiones_soja, total_camiones_cebada, total_camiones_girasol, total_camiones_trigo, total_neto_maiz, total_neto_soja, total_neto_trigo, total_neto_girasol, total_neto_cebada, menor_maiz, mayor_soja, promedio_neto_soja, promedio_neto_maiz, recepcionhecha, camion, decisionprod, producto, porlomenosuno
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
    decisionprod = ""
    producto = ""
    porlomenosuno = False

# procedimientos en_construccion(), opciones_menu(), opciones_admin(), opciones_terciario()
# Contienen casi todas las impresiones necesarias de los distintos menús.

def en_construccion():
    clear()
    print(ROJO + "Esta funcionalidad está en construcción." + BLANCO)
    

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

#procedimiento opciones_terciario(titulo: String)
def opciones_terciario(titulo):
    print(VERDE + f"----- MENU {titulo} -----" + BLANCO)
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

# Verificación de códigos
def verificacioncod(codigo):
    # isnumeric() devuelve TRUE si lo ingresado es un entero
    # el código es universalmente de 5 dígitos
    while codigo == "" or codigo.isnumeric() == False or codigo not in range(0,100000): 
        codigo = input("Error. Ingrese nuevamente - ")
    return codigo

def cargarprod():
    global contp, decisionprod, producto, porlomenosuno
    decisionprod = "SI"
    if ncupos == 0:
        while decisionprod != "NO":

            porlomenosuno = True
            # Verificación de que el producto no se encuentre repetido o ya haya otro producto allí
            print("Ingresar el nombre del producto: ")
            producto = input("- ").upper()
            
            while producto == "" or producto.isnumeric() == True or len(producto) > 25:
                producto = input("No es un producto válido. Ingrese nuevamente: ").upper()
            
            while tebuscoalla(producto) == True:
                producto = input("Producto ya ingresado. Ingrese nuevamente: ").upper() 
                while producto == "" or producto.isnumeric() == True:
                    producto = input("No es un producto válido. Ingrese nuevamente: ").upper()

           # while tebuscopos(producto) == -1:
           #     producto = input("Producto ya ingresado. Ingrese nuevamente: ").upper() 
           #     while producto == "" or producto.isnumeric() == -1:
            #        producto = input("No es un producto válido. Ingrese nuevamente: ").upper()

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

            decisionprod = input("¿Desea ingresar otro producto? Ingrese SI o NO: ").upper()
            while decisionprod != "NO" and decisionprod != "SI": # Validación de datos
                decisionprod = input("Opción incorrecta. Ingrese nuevamente: ").upper()
                
            if decisionprod == "NO":
                print("Productos ingresados correctamente")
                os.system("pause")
                clear()
                opciones_terciario("PRODUCTOS")
    else:
        print("Cupos ya otorgados.")

# Búsqueda de productos
def tebuscoalla(producto):
    producto = producto.ljust(25, ' ')
    getsai = os.path.getsize(AFPRODUCTOS)
    ALPRODUCTOS.seek(0,0) 
    RLPRODUCTOS = csproducto()
    if getsai > 0:
        while ALPRODUCTOS.tell() < getsai and RLPRODUCTOS.nombreproducto != producto:
            RLPRODUCTOS = pickle.load(ALPRODUCTOS)
        if RLPRODUCTOS.nombreproducto == producto:
            return True
        else:
            return False
    else:
        return False

# Búsqueda de código
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

# otra búsqueda igual pero que retorna 1 y -1???????????????
###########################################################
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

def consultaP():
    getsai = os.path.getsize(AFPRODUCTOS)
    RLPRODUCTOS = csproducto()
    if getsai == 0:
        print("No hay nada para mostrar")
    
    else:
        ALPRODUCTOS.seek(0,0)
        print("producto |       codigo producto")
        print("---------------------------")
    while ALPRODUCTOS.tell() < getsai:
        RLPRODUCTOS = pickle.load(ALPRODUCTOS)
        print(RLPRODUCTOS.nombreproducto, RLPRODUCTOS.codproducto)
    os.system("pause")
    clear()
    opciones_terciario("PRODUCTOS")

# procedimiento eliminarP(var P: P; producto: String)
# VAR
# j, i: Integer
# producto: String
def eliminarP(producto):
    if tebuscopos(producto) != -1:
        pos = tebuscopos(producto)
        ALPRODUCTOS.seek(pos,0)
        RLPRODUCTOS = pickle.load(ALPRODUCTOS)
        RLPRODUCTOS.nombreproducto = ""
        RLPRODUCTOS.codproducto = 0
        ALPRODUCTOS.seek(pos,0)
        formatearproducto(RLPRODUCTOS)
        pickle.dump(RLPRODUCTOS, ALPRODUCTOS)
        print(f"El producto {producto} se eliminó correctamente.")
        os.system("pause")
        clear()
        opciones_terciario("PRODUCTOS")
    else:
        print("El Producto no se encontró.")
        os.system("pause")
        clear()
        opciones_terciario("PRODUCTOS")

# procedimiento bajaprod(var P: P)
# VAR
# producto: String
# ncupos: Integer
def bajaprod():
    # Si hay cupos otorgados, no se deben cambiar/eliminar los productos (para evitar que haya camiones sin productos dados de alta)
    if ncupos == 0: 
        getsai = os.path.getsize(AFPRODUCTOS)
        RLPRODUCTOS = csproducto()
        if getsai == 0:
            print("No hay nada para mostrar.")
            
        else:
            ALPRODUCTOS.seek(0,0)
            print("producto |       codigo producto")
            print("---------------------------")
            while ALPRODUCTOS.tell() < getsai:
                RLPRODUCTOS = pickle.load(ALPRODUCTOS)
                print(RLPRODUCTOS.nombreproducto, RLPRODUCTOS.codproducto)
            producto = input("Ingresar el nombre del producto a eliminar: ").upper() # BUCLE INFINITO PA
            eliminarP(producto)
    else:
        print("Cupos ya otorgados. No se pueden eliminar productos.")

def modificarP(producto, nuevoproducto, nuevocod):
    if tebuscopos(producto) != -1:
        pos = tebuscopos(producto)
        print("este es el pos ", pos)
        ALPRODUCTOS.seek(pos,0)
        RLPRODUCTOS = pickle.load(ALPRODUCTOS)
        RLPRODUCTOS.nombreproducto = nuevoproducto
        RLPRODUCTOS.codproducto = nuevocod

        ALPRODUCTOS.seek(pos,0)
        formatearproducto(RLPRODUCTOS)
        pickle.dump(RLPRODUCTOS, ALPRODUCTOS)

        print(f"El producto {producto} ahora es {nuevoproducto} con código {nuevocod}.")
        os.system("pause")
        clear()
        opciones_terciario("PRODUCTOS")
    else:
	    print("El Producto no se encontró.")

def modificacionproducto():

    if ncupos == 0:
        getsai = os.path.getsize(AFPRODUCTOS)
        RLPRODUCTOS = csproducto()
        if getsai == 0:
            print("No hay nada para mostrar")
            
        else:
            ALPRODUCTOS.seek(0,0)
            print("producto |       codigo producto")
            print("---------------------------")
            while ALPRODUCTOS.tell() < getsai:
                RLPRODUCTOS = pickle.load(ALPRODUCTOS)
                print(RLPRODUCTOS.nombreproducto, RLPRODUCTOS.codproducto)
            producto = input("Ingresar el nombre del producto a modificar: ").upper()

            # Verificación de que sea de los ingresados
            while producto == "" or producto.isnumeric() == True or len(producto) > 25:
                producto = input("No es un producto válido. Ingrese nuevamente: ").upper()

            nuevoproducto = input("Ingresar el nuevo producto: ").upper()
            # Verificación de que sea correcto y no se vaya a repetir
            while nuevoproducto == "" or nuevoproducto.isnumeric() == True or len(nuevoproducto) > 25:
                nuevoproducto = input("No es un producto válido. Ingrese nuevamente: ").upper()

            while tebuscoalla(nuevoproducto) == True:
                nuevoproducto = input("Producto ya ingresado. Ingrese nuevamente: ").upper()
                while nuevoproducto == "" or nuevoproducto.isnumeric() == True or len(nuevoproducto) > 25:
                    nuevoproducto = input("No es un producto válido. Ingrese nuevamente: ").upper()

            nuevocod = int(verificacioncod(input("Ingrese el código del producto: ")))
            while tebuscodigo(nuevocod) == True:
                nuevocod = int(verificacioncod(input("Código no válido. Ingrese nuevamente: ")))
            
            modificarP(producto, nuevoproducto, nuevocod)
    else:
        print("Cupos ya otorgados. No se pueden modificar los productos.")

# procedimiento menu_productos():
# VAR
# P: productos
# opcion_terciario: Char (un caracter)
def menu_productos():

    clear()
    opciones_terciario("PRODUCTOS")
    opcion_terciario = "A"
    while opcion_terciario != "V":
        opcion_terciario = input("Opción: ").upper() # Convertir toda cadena ingresada en mayúscula.
        while opcion_terciario == "" or len(opcion_terciario) > 1: # Validación de datos
            opcion_terciario = input("Opción incorrecta. Ingrese nuevamente: ")
        
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

def menu_rubros():
    clear()
    opciones_terciario("RUBROS")
    opcion_terciario = "A"
    while opcion_terciario != "V":
        opcion_terciario = input("Opción: ").upper() # Convertir toda cadena ingresada en mayúscula.
        while opcion_terciario == "" or len(opcion_terciario) > 1: # Validación de datos
            opcion_terciario = input("Opción incorrecta. Ingrese nuevamente: ")
        
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

def cargarubro():
    cargamiento = "S"
    while cargamiento == "S":
        nombreR = input("Ingrese el nombre del rubro: ")

        while nombreR == "" or nombreR.isnumeric == True or len(nombreR) > 25 or tebusrubro(nombreR) == True:
            nombreR = input("Nombre del rubro incorrecto. Ingrese nuevamente: ")

        # Verificación de que se ingrese un número
        cod = int(verificacioncod(input("Ingrese el código del rubro: ")))
        while tebuscodR(cod) == True:
            cod = int(verificacioncod(input("Código no válido. Ingrese nuevamente: ")))


        RLRUBROS = csrubro()

        RLRUBROS.codigorubro = cod
        RLRUBROS.nombrerubro = nombreR
        formatearrubro(RLRUBROS)
        ALRUBROS.seek(0,2)
        pickle.dump(RLRUBROS, ALRUBROS)
        ALRUBROS.flush()

        cargamiento = input("¿Desea ingresar otro rubro? Ingrese SI o NO: ").upper()
        while cargamiento != "NO" and cargamiento != "SI": # Validación de datos
                cargamiento = input("Opción incorrecta. Ingrese nuevamente: ").upper()
                
        if cargamiento == "NO":
            print("Rubros ingresados correctamente")
            os.system("pause")
            clear()
            opciones_terciario("RUBROS")

def menu_rubrosxproducto():
    clear()
    opciones_terciario("RUBROS POR PRODUCTO")
    opcion_terciario = "A"
    while opcion_terciario != "V":
        opcion_terciario = input("Opción: ").upper() # Convertir toda cadena ingresada en mayúscula.
        while opcion_terciario == "" or len(opcion_terciario) > 1: # Validación de datos
            opcion_terciario = input("Opción incorrecta. Ingrese nuevamente: ")
        
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
    cargamiento = "S"
    while cargamiento == "S":

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

        cargamiento = input("¿Desea ingresar otro rubro por producto? Ingrese SI o NO: ").upper()
        while cargamiento != "NO" and cargamiento != "SI": # Validación de datos
                cargamiento = input("Opción incorrecta. Ingrese nuevamente: ").upper()
                
        if cargamiento == "NO":
            print("Rubros por productos ingresados correctamente")
            os.system("pause")
            clear()
            opciones_terciario("RUBROS POR PRODUCTO")

#funcion busqueda dicotomica de producto, entre parentesis va la variable del codigo que se ingrese, cambienla como sea que se llame :3
def BuscaDico(cod):
    ALPRODUCTOS.seek(0,0)
    RLPRODUCTOS= pickle.load(ALPRODUCTOS)
    tamReg= ALPRODUCTOS.tell()
    tamArc= os.path.getsize(AFPRODUCTOS)
    cantReg= tamArc//tamReg
    inf= 0
    sup= cantReg-1
    med= (inf+sup)//2
    ALPRODUCTOS.seek(med*cantReg, 0)
    RLPRODUCTOS= pickle.load(ALPRODUCTOS)
    while (inf<sup) and (RLPRODUCTOS.codproducto != cod):
        if cod<RLPRODUCTOS.codproducto:
            sup=med-1
        else: 
            inf= med+1
        med=(sup+inf)//2
        ALPRODUCTOS.seek(med*cantReg, 0)
        RLPRODUCTOS= pickle.load(ALPRODUCTOS)
    if RLPRODUCTOS.codproducto==cod:
        return med*cantReg
    else: 
        return -1

#Ordenamiento secuencial de producto, esta hecho por codigo del producto:
def ordenProdu():
    ALPRODUCTOS.seek(0,0)
    aux= pickle.load(ALPRODUCTOS)
    tamReg= ALPRODUCTOS.tell()
    tamArc= os.path.getsize(AFOPERACIONES)
    cantReg = tamArc//tamReg #tambien se puede hacer cantReg= int(tamArc/tamReg)
    for i in range (0,cantReg-1):
        for j in range (i+1, cantReg):
            ALPRODUCTOS.seek(i*tamReg, 0)
            auxi = pickle.load(ALPRODUCTOS)
            ALPRODUCTOS.seex(j*tamReg, 0)
            auxj = pickle.load(ALPRODUCTOS)
            if (auxi.codproducto>auxj.codproducto):
                ALPRODUCTOS.seek(i*tamReg, 0)
                pickle.dump(auxj,ALPRODUCTOS)
                ALPRODUCTOS.seek(j*tamReg, 0)
                pickle.dump(auxi,ALPRODUCTOS)




def menu_silos():
    clear()
    opciones_terciario("SILOS")
    opcion_terciario = "A"
    while opcion_terciario != "V":
        opcion_terciario = input("Opción: ").upper() # Convertir toda cadena ingresada en mayúscula.
        while opcion_terciario == "" or len(opcion_terciario) > 1: # Validación de datos
            opcion_terciario = input("Opción incorrecta. Ingrese nuevamente: ")
        
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

def cargasilos():
    cargamiento = "S"
    while cargamiento == "S":
        codsil = int(verificacioncod(input("Ingrese el código del silo: ")))
    
        while tebusilo(codsil) == True:
            codsil = int(verificacioncod(input("Código en uso. Ingrese nuevamente: ")))

        codprod = int(verificacioncod(input("Ingrese el código del producto: ")))

        while tebuscodigo(codprod) == False:
            codprod = int(verificacioncod(input("Código no encontrado. Ingrese nuevamente: ")))

        nombreS = input("Ingrese el nombre del silo: ")
        while nombreS.isnumeric() == True or len(nombreS) > 25:
            nombreS = input("Nombre incorrecto. Ingrese nuevamente: ")

        stockS = int(verificacioncod(input("Ingrese el stock del silo: ")))

        RLSILOS = cssilo()

        RLSILOS.codigosilo = codsil
        RLSILOS.codproducto = codprod
        RLSILOS.nombresilo = nombreS
        RLSILOS.stock = stockS
        formatearsilos(RLSILOS)
        ALSILOS.seek(0,2)
        pickle.dump(RLSILOS, ALSILOS)
        ALSILOS.flush()

        cargamiento = input("¿Desea ingresar otro silo? Ingrese SI o NO: ").upper()
        while cargamiento != "NO" and cargamiento != "SI": # Validación de datos
                cargamiento = input("Opción incorrecta. Ingrese nuevamente: ").upper()
                
        if cargamiento == "NO":
            print("Silos ingresados correctamente")
            os.system("pause")
            clear()
            opciones_terciario("SILOS")




m = 0
pospat = 0
vrtemp = " "

# function bucapatente(patente): char
# Intento de funcion buscar- Nair

def buscapatente(npat):
    npat = npat.ljust(7, ' ')
    m = os.path.getsize(AFOPERACIONES)
    ALOPERACIONES.seek(0)
    while ALOPERACIONES.tell() < m:
        pospat = ALOPERACIONES.tell()
        vrtemp = pickle.load(ALOPERACIONES)
        if vrtemp.patente == npat:
            return pospat
    return -1

def ayudaayuda(patente, fecha):
    patente = patente.ljust(7, ' ')
    if buscapatente(patente) != -1:
        pospat = buscapatente(patente)
        ALOPERACIONES.seek(0, pospat)
        RL = pickle.load(ALOPERACIONES)
        if RL.patente == patente and RL.fecharep == fecha:
            return True
        else:
            return False
        
    else:
        return False
# procedimiento cupos()
# VAR
# decisioncup, nuevapatente, cuposctm: String
# arrpatentes: arrpatentes (Type Array declarado al inicio del programa)
# arrcupos: arrcupos (Type Array declarado al inicio del programa)
# ncupos: Integer
# nuevoestado: Char
ncupos = 0
def cupos():

    clear()
    print(AMARILLO + "----- MENÚ DE CUPOS -----" + BLANCO)
    decisioncup = input("¿Desea ingresar un cupo? Ingrese SI o NO: ").upper()
    while decisioncup != "SI" and decisioncup != "NO":  # Validación de datos
        decisioncup = input("Ingrese una opción correcta: ").upper()

    while decisioncup == "SI":
        clear()
        nuevapatente = input("Ingresar la patente del camión: ").upper()
        while len(nuevapatente) < 6 or len(nuevapatente) > 7: # Comprobamos la longitud de la patente
            nuevapatente = input("Error con la longitud de la patente. Por favor ingresar de vuelta: ").upper()
        else:
            RLOPERACIONES = csoperacion()
            fecharep = validarFecha("Ingrese la fecha de recepción: ")
            if ayudaayuda(nuevapatente, fecharep) == True:
                print("Cupo ya otorgado en esa fecha.")
            else:
                codigo = int(verificacioncod(input("Ingrese el código del producto: ")))
                if tebuscodigo(codigo) == False:
                    print("No se encontró el producto con el código dado. Fin de la operación.")
                else:
                    RLOPERACIONES.patente = nuevapatente
                    RLOPERACIONES.fechacupo = fecharep
                    RLOPERACIONES.codproducto = codigo
                    RLOPERACIONES.estado = "P"

                    formatearoperaciones(RLOPERACIONES)
                    pickle.dump(RLOPERACIONES, ALOPERACIONES)
                    ALOPERACIONES.flush()
                    print(f"Se ingresó el Cupo, código {codigo} con patente {nuevapatente}")
            decisioncup = input("¿Desea ingresar un nuevo cupo? Ingrese SI o NO: ").upper()
            while decisioncup != "SI" and decisioncup != "NO":  # Validación de datos
                decisioncup = input("Ingrese una opción correcta: ").upper()

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
        respuestarep = input("¿Desea limpiar los datos de la recepción? Ingrese SI o NO: ").upper()
    
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
        print(ROJO + f"\nDatos del camión" + BLANCO)
        PATENTE = input("Ingresar número de patente ").upper()

        while len(PATENTE) < 6 or len(PATENTE) > 7:
            PATENTE = input("La patente no es válida, ingresar de vuelta: ").upper()

        if buscapatente(PATENTE) != -1:
            pospat = buscapatente(PATENTE)
            ALOPERACIONES.seek(pospat, 0)
            RLOPERACIONES = pickle.load(ALOPERACIONES)

            if RLOPERACIONES.fechacupo == datetime.date.today() and RLOPERACIONES.estado == "P":
                RLOPERACIONES.estado = "A"
                ALOPERACIONES.seek(pospat, 0)
                pickle.dump(RLOPERACIONES, ALOPERACIONES)
                ALOPERACIONES.flush()
                print(f"Se actualizó el estado del camión {PATENTE} con éxito.")

            else:
                print("El camión tiene una fecha o estado incorrecto.")

        else: print("ta mal unu")
        # else:
        #     if arrcupos[lugar] == "P":

        #         print("Ingresar tipo de producto (Maíz, Soja, Trigo, Girasol, Cebada)")
        #         PRODUCTO = input("- ").upper()
        #         while tebuscoaca(P, PRODUCTO) != True and PRODUCTO != "S":
        #             PRODUCTO = input("No es un producto válido o no está dado de alta, ingresar de vuelta (S\salir): ").upper()

        #         if PRODUCTO != "S":
        #             arrcupos[lugar] = "E"
        #             print(f'Se actualizó el cupo de la patente {PATENTE} a "En proceso"')

        #         if PRODUCTO == "MAIZ":
        #             print(f"Cargado camión con patente {PATENTE} de {PRODUCTO}")
        #             total_camiones_maiz += 1
        #             productosxp[lugar] = PRODUCTO
        #         elif PRODUCTO == "SOJA":
        #             print(f"Cargado camión con patente {PATENTE} de {PRODUCTO}")
        #             total_camiones_soja += 1
        #             productosxp[lugar] = PRODUCTO
        #         elif PRODUCTO == "TRIGO":
        #             print(f"Cargado camión con patente {PATENTE} de {PRODUCTO}")
        #             total_camiones_trigo += 1
        #             productosxp[lugar] = PRODUCTO
        #         elif PRODUCTO == "GIRASOL":
        #             print(f"Cargado camión con patente {PATENTE} de {PRODUCTO}")
        #             total_camiones_girasol += 1
        #             productosxp[lugar] = PRODUCTO
        #         elif PRODUCTO == "CEBADA":
        #             print(f"Cargado camión con patente {PATENTE} de {PRODUCTO}")
        #             total_camiones_cebada += 1
        #             productosxp[lugar] = PRODUCTO
        #         total_camiones += 1
        #     else:
        #         print("Este camión ya fue procesado.")

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

def cerrarArchivos():
    ALOPERACIONES.close()
    ALPRODUCTOS.close()
    ALRUBROS.close()
    ALRUBROSXPRODUCTO.close()
    ALSILOS.close()

# main() -> Programa principal
# Variables:
# opcion: Char (un caracter)
def main():

    clear()
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
        
        elif opcion == "9":
            print("esto es el listado de silos y rechazos")

        else: # Fin del programa
            cerrarArchivos()
            print("Fin del programa.")

        
# Ejecución del programa principal.
main()

# -------- FUNCION PARA CHEQUEAR COSITAS DE OPERACIONESSSSSS -----------------

# getsai = os.path.getsize(AFOPERACIONES)
# ALOPERACIONES.seek(0,0)
# while ALOPERACIONES.tell() < getsai:
#     RLPRODUCTOS = pickle.load(ALOPERACIONES)
#     print(RLPRODUCTOS.fechacupo, RLPRODUCTOS.patente, RLPRODUCTOS.codproducto, RLPRODUCTOS.estado)
# os.system("pause")