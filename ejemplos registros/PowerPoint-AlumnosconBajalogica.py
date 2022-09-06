# ejemplo presentación en Power Alumnos

import os
import pickle
import os.path


class Alumno:
    def __init__(self):  # constructor dentro de la clase Alumno
        self.legajo = 0
        self.comision= 0
        self.nombre = ""
        self.carrera = ""
        self.notas = [0]*3
        self.promedio = 0.0


def validarChar(l1,l2,l3,l4):
    letra = input("Ingrese Carrera:  S- Sistemas   Q- Quimica  M-Mecanica   C-Civil: : ").upper()
    while (letra !=l1) and (letra !=l2) and (letra !=l3) and (letra !=l4):
        letra = input("Ingrese Carrera:  S- Sistemas   Q- Quimica  M-Mecanica   C-Civil: : ").upper()
    return letra
 
 
def validaRangoEntero(nro, min, max):
    try:              
        nro = int(nro)      
        if nro >= min and nro <= max:
            return False 
        else:
            return True  
    except:
        return True  


def formatearAlumno(vrAlu): # vrAlu parámetro formal
    vrAlu.legajo= str(vrAlu.legajo)
    vrAlu.legajo= vrAlu.legajo.ljust(5, ' ')     
    vrAlu.nombre = vrAlu.nombre.ljust(25, ' ')
    vrAlu.comision= str(vrAlu.comision)
    vrAlu.comision = vrAlu.comision.ljust(2, ' ') 
    vrAlu.carrera = str(vrAlu.carrera)
    vrAlu.carrera = vrAlu.carrera.ljust(1) 
    for i in range(0, 2):
        vrAlu.notas[i] = str(vrAlu.notas[i])
        vrAlu.notas[i] = vrAlu.notas[i].ljust(2, ' ')
    vrAlu.promedio = str(vrAlu.promedio)
    vrAlu.promedio = vrAlu.promedio.ljust(5, ' ') 


def ordenaAlumnosxProme():  #ordena por campo promedio 
    global ArcFisiAlu, ArcLogAlu 
    ArcLogAlu.seek (0, 0)
    aux = pickle.load(ArcLogAlu)
    tamReg = ArcLogAlu.tell() 
    tamArch = os.path.getsize(ArcFisiAlu)
    cantReg = int(tamArch / tamReg)  
    for i in range(0, cantReg-1):
        for j in range (i+1, cantReg):
            ArcLogAlu.seek (i*tamReg, 0)
            auxi = pickle.load(ArcLogAlu)
            ArcLogAlu.seek (j*tamReg, 0)
            auxj = pickle.load(ArcLogAlu)
            if (float(auxi.promedio) < float(auxj.promedio)):
                ArcLogAlu.seek (i*tamReg, 0)
                pickle.dump(auxj, ArcLogAlu)
                ArcLogAlu.seek (j*tamReg, 0)
                pickle.dump(auxi, ArcLogAlu)
                ArcLogAlu.flush()


def ordenaAlumnosxLeg():  #ordena por campo legajo 
    global ArcFisiAlu, ArcLogAlu 
    ArcLogAlu.seek (0, 0)
    aux = pickle.load(ArcLogAlu)
    tamReg = ArcLogAlu.tell() 
    tamArch = os.path.getsize(ArcFisiAlu)
    cantReg = int(tamArch / tamReg)  
    for i in range(0, cantReg-1):
        for j in range (i+1, cantReg):
            ArcLogAlu.seek (i*tamReg, 0)
            auxi = pickle.load(ArcLogAlu)
            ArcLogAlu.seek (j*tamReg, 0)
            auxj = pickle.load(ArcLogAlu)
            if int(auxi.legajo) > int(auxj.legajo):
                ArcLogAlu.seek (i*tamReg, 0)
                pickle.dump(auxj, ArcLogAlu)
                ArcLogAlu.seek (j*tamReg, 0)
                pickle.dump(auxi, ArcLogAlu)
                ArcLogAlu.flush()


def BuscaSec(Leg):
    global ArcFisiAlu, ArcLogAlu
    t = os.path.getsize(ArcFisiAlu)
    pos=0
    ArcLogAlu.seek(0, 0) 
    vrAlu = Alumno() 
    if t>0:
        vrAlu = pickle.load(ArcLogAlu)
        while (ArcLogAlu.tell()<t) and (int(Leg) != int(vrAlu.legajo)):
            pos = ArcLogAlu.tell()
            vrAlu = pickle.load(ArcLogAlu)
        if int(vrAlu.legajo) == int(Leg):        
            return pos
        else:
            return -1
    else:
        print('-----------------')
        print("Archivo sin datos")
        print('-----------------')
        input()
        return -1


def BusquedaDico (Leg):   # método de búsqueda dicotómica
        global ArcFisiAlu, ArcLogAlu 
        ArcLogAlu.seek (0, 0)
        aux = pickle.load(ArcLogAlu)
        tamReg = ArcLogAlu.tell() 
        cantReg = int(os.path.getsize(ArcFisiAlu) / tamReg)
        inferior = 0
        superior = cantReg-1
        medio = (inferior + superior) // 2 					
        ArcLogAlu.seek(medio*tamReg, 0)
        RegAlu= pickle.load(ArcLogAlu) 					
        while int(RegAlu.legajo)!= Leg and (inferior < superior):
            if Leg < int(RegAlu.legajo):
                superior = medio - 1
            else:
                inferior = medio + 1
            medio = (inferior + superior) // 2 
            ArcLogAlu.seek(medio*tamReg, 0)
            RegAlu= pickle.load(ArcLogAlu)
        if int(RegAlu.legajo) == Leg:						
            return medio*tamReg							
        else:
            return -1


def ModificaCampo():
    global ArcLogAlu
    RegAlu = Alumno()
    os.system("cls")
    print("ACTUALIZACIÓN campo COMISIÓN o CARRERA")
    print("--------------------------------------")
    t = os.path.getsize(ArcFisiAlu)
    if t==0:
        print ("No hay Alumnos registrados")
    else:
        leg = input("Ingrese el legajo del Alumno a modificar entre 1 y 9999 [0 para Volver]: ")
        while validaRangoEntero(leg, 0, 9999):
            leg = input("Incorrecto - Entre 0 y 9999 [0 para Volver]: ")
        if leg != 0:
            pos = BuscaSec(leg)    #invoca la función buscar para obtener la posición
                                           #donde comienza el registro
            if pos == -1:   #si no se encontró el Alumno
                print("El Alumno no existe")
            else:
                ArcLogAlu.seek(pos, 0)        #Ubico el punto en la posición donde comienza el registro
                RegAlu = pickle.load(ArcLogAlu)    #Cargo el registro en memoria
                print ("Alumno a actualizar:")
                print ("Nombre: ", RegAlu.nombre)
                print ("Comisión: ", RegAlu.comision)
                print ("Carrera: ", RegAlu.carrera)
                print ("Nota 1: ", RegAlu.notas[0])
                print ("Nota 2: ", RegAlu.notas[1])
                print ("Nota 3: ", RegAlu.notas[2])
                print ("Promedio de Notas:", RegAlu.promedio)
                print("\n Solo se podrán modificar la comisión y la carrera \n")
                rta = input("Deseas Modificar la comisión (S/N): ").upper()
                while rta != "S" and rta != "N":
                    rta = input("Por favor, solo contesta con S para Si o N para No").upper()
                if rta == "S":
                    RegAlu.comision = input("Nueva comisión: ")
                    while validaRangoEntero(RegAlu.comision, 1, 5):
                        RegAlu.comision = int(input("Incorrecto - numero de comision entre 1 y 5: "))

                rtac = input("Deseas Modificar la carrera (S/N): ").upper()
                while rtac != "S" and rtac != "N":
                    rtac = input("Por favor, solo contesta con S para Si o N para No: ").upper()
                if rtac == "S":
                    RegAlu.carrera=validarChar('S','M','Q','C')
                
                rpta = input("Confirma? (S o N): ")
                while rpta.upper() != "S" and rpta.upper() != "N":
                    rpta = input("Incorrecto - Confirma? (S o N): ")
                if rpta.upper() == "S":
                    ArcLogAlu.seek(pos, 0)
                    formatearAlumno(RegAlu)
                    pickle.dump(RegAlu, ArcLogAlu)
                    ArcLogAlu.flush()  #fuerza el envío del objeto/registro al archivo físico sin necesidad de cerrar el mismo
                    print('--------------------')
                    print("Modificación exitosa")
                    print('--------------------')
                    print("Los datos actualizados del Alumno son:")
                    print ("Nombre: ", RegAlu.nombre)
                    print ("Comisión: ", RegAlu.comision)
                    print ("Carrera: ", RegAlu.carrera)
                    print ("Nota 1: ", RegAlu.notas[0])
                    print ("Nota 2: ", RegAlu.notas[1])
                    print ("Nota 3: ", RegAlu.notas[2])
                    print ("Promedio de Notas:", RegAlu.promedio)
    os.system("pause")


def BajaLogicaBlanqueoCampos():
    global ArcLogAlu
    RegAlu = Alumno()
    os.system("cls")
    print("Baja lógica de todos los campos menos el legajo")
    print("-----------------------------------------------")
    t = os.path.getsize(ArcFisiAlu)
    if t==0:
        print ("No hay Alumnos registrados")
    else:
        leg = input("Ingrese el legajo del Alumno a dar de baja entre 1 y 9999 [0 para Volver]: ")
        while validaRangoEntero(leg, 0, 9999):
            leg = input("Incorrecto - Entre 0 y 9999 [0 para Volver]: ")
        if leg != 0:
            pos = BuscaSec(leg)    #invoca la función buscar para obtener la posición
                                          #donde comienza el registro
            if pos == -1:              #si no se encontró el Alumno
                print("El Alumno no existe")
            else:
                ArcLogAlu.seek(pos, 0)        #Ubico el punto en la posición donde comienza el registro
                RegAlu = pickle.load(ArcLogAlu)    #Cargo el registro en memoria
                print("Alumno a dar de baja lógica:")
                print ("Nombre: ",RegAlu.nombre)
                print ("Comisión: ", RegAlu.comision)
                print ("Carrera: ", RegAlu.carrera)
                print ("Nota 1: ", RegAlu.notas[0])
                print ("Nota 2: ", RegAlu.notas[1])
                print ("Nota 3: ", RegAlu.notas[2])
                print ("Promedio de Notas:", RegAlu.promedio)
                
                rta = input("seguro Deseas dar de baja (S/N): ").upper()
                while rta != "S" and rta != "N":
                    rta = input("Por favor, solo contesta con S para Si o N para No").upper()
                if rta == "S":
                    #RegAlu.legajo= leg
                    RegAlu.comision= 0
                    RegAlu.nombre= ""
                    RegAlu.carrera= ""
                    for i in range(0, 3):
                        RegAlu.notas[i] = 0
                    RegAlu.promedio = 0.0
                    ArcLogAlu.seek(pos, 0)
                    formatearAlumno(RegAlu)
                    pickle.dump(RegAlu, ArcLogAlu)
                    ArcLogAlu.flush()  #Fuerza el envío del objeto/registro al archivo físico sin necesidad de cerrar el mismo
                    print('--------------------')
                    print("   Baja exitosa")
                    print('--------------------')
                else: 
                    print('tranquilo...los datos no fueron borrados')
    os.system("pause")


def ListaAlumnosPromeMayor8():
        global ArcFisiAlu, ArcLogAlu 
        os.system("cls")
        print("OPCION 4 - Lista de Alumnos con promedio mayor a 8")
        print("--------------------------------------------------------\n")
        t = os.path.getsize(ArcFisiAlu)
        if t==0:
            print ("No hay Alumnos registrados")
        else:
            print('legajo  Nombre                     comisión   Carrera  nota1  nota2  nota3   Promedio')
            print("-------------------------------------------------------------------------------------------")
            RegAlu = Alumno()
            ArcLogAlu.seek(0, 0)
            while ArcLogAlu.tell()<t:
                RegAlu = pickle.load(ArcLogAlu)
                if float(RegAlu.promedio) >= 8:
                    print(RegAlu.legajo,"  ",RegAlu.nombre, "  ", RegAlu.comision,"       ",RegAlu.carrera, "    ", RegAlu.notas[0], "   ",RegAlu.notas[1], "  ",RegAlu.notas[2],"      ",RegAlu.promedio)
                print()
        os.system("pause")


def ListaxPromeDescendente():
    global ArcFisiAlu, ArcLogAlu 
    os.system("cls")
    print("-                  Listado de alumnos ordenado por promedio")
    print("--------------------------------------------------------------------------------\n")
    t = os.path.getsize(ArcFisiAlu)
    if t==0:
        print ("No hay Alumnos registrados a listar")
    else:
        ordenaAlumnosxProme()
        print('legajo  Nombre                     comisión   Carrera  nota1  nota2  nota3   Promedio')
        print('--------------------------------------------------------------------------------------')
        ArcLogAlu.seek(0, 0)
        RegAlu = Alumno()
        while ArcLogAlu.tell()<t:
            RegAlu = pickle.load(ArcLogAlu)
            print(RegAlu.legajo,"  ",RegAlu.nombre, "  ", RegAlu.comision,"       ",RegAlu.carrera, "    ", RegAlu.notas[0], "   ",RegAlu.notas[1], "  ",RegAlu.notas[2],"   ",RegAlu.promedio)
    os.system ("pause")
	
	
def ListaAlumnos():
    global ArcFisiAlu, ArcLogAlu 
    os.system("cls")
    print("Listado de alumnos")
    print("--------------------------------------------------------------------------------\n")
    t = os.path.getsize(ArcFisiAlu)
    if t==0:
        print ("No hay Alumnos registrados a listar")
    else:
        print("muestra Desordenado")
        print("-------------------")
        print('legajo  Nombre                     comisión   Carrera  nota1  nota2  nota3   Promedio')
        print('--------------------------------------------------------------------------------------')
        ArcLogAlu.seek(0, 0)
        RegAlu = Alumno()
        while ArcLogAlu.tell()<t:
            RegAlu = pickle.load(ArcLogAlu)
            print(RegAlu.legajo,"  ",RegAlu.nombre, "  ", RegAlu.comision,"       ",RegAlu.carrera, "    ", RegAlu.notas[0], "   ",RegAlu.notas[1], "  ",RegAlu.notas[2],"     ",RegAlu.promedio)
        print()    
        print("muestra Ordenado por Legajo")
        print("--------------------------")
        print('legajo  Nombre                     comisión   Carrera  nota1  nota2  nota3   Promedio')
        print('-------------------------------------------------------------------------------------')
        ordenaAlumnosxLeg()  #ORDENA POR LEGAJO
        ArcLogAlu.seek(0, 0)
        RegAlu = Alumno()
        while ArcLogAlu.tell()<t:
            RegAlu = pickle.load(ArcLogAlu)
            print(RegAlu.legajo,"  ",RegAlu.nombre, "  ", RegAlu.comision,"       ",RegAlu.carrera, "    ", RegAlu.notas[0], "   ",RegAlu.notas[1], "  ",RegAlu.notas[2],"     ",RegAlu.promedio)
    os.system ("pause")    


def ConsultaAlumno():
    global ArcFisiAlu, ArcLogAlu
    os.system("cls")
    print("OPCION 2 - Cosulta de un alumno")
    print("-------------------------------\n")
    t = os.path.getsize(ArcFisiAlu)
    RegAlu = Alumno()
    if t==0:
        print ("No hay Ningún Alumno Cargado")
    else:
        Leg= input("Ingrese legajo a buscar: ")
        pos = BuscaSec(Leg) # el ordenamiento es por el campo promedio, por eso acá llamo a busca secuencial x legajo
        if (pos == -1):
            print ("Legajo no Encontrado")
        else:
            print ("Legajo Encontrado") # mostrar los campos de ESE solo alumno 
            ArcLogAlu.seek(pos,0)
            RegAlu= pickle.load(ArcLogAlu)
            print ("Nombre: ",RegAlu.nombre)
            print ("Comisión: ", RegAlu.comision)
            print ("Carrera: ", RegAlu.carrera)
            print ("Nota 1: ", RegAlu.notas[0])
            print ("Nota 2: ", RegAlu.notas[1])
            print ("Nota 3: ", RegAlu.notas[2])
            print ("Promedio de Notas:", RegAlu.promedio)
    os.system("pause")
                        
 
def Altas():
    global ArcFisiAlu, ArcLogAlu
    os.system("cls")
    print("OPCION 1 - Alta de Alumnos")
    print("----------------------------\n")
    leg = input("Ingrese el legajo del Alumno a dar de alta, entre 1 y 9999 [0- para Volver]: ")
    while validaRangoEntero(leg, 0, 9999):
        leg = int(input("Incorrecto - Entre 1 y 9999 [0 para Volver]: "))
    RegAlu = Alumno()
    while int(leg) != 0:
        if BuscaSec(leg) == -1:
            RegAlu.legajo = int(leg)
            RegAlu.nombre = input("Nombre y Apellido <hasta 25 caracteres>: ")
            while len(RegAlu.nombre)<1 or len(RegAlu.nombre)>25:
                RegAlu.nombre = input("Incorrecto - Nombre y Apellido <hasta 25 caracteres>: ")
            RegAlu.comision = input("comision entre 1 y 5: ")
            while validaRangoEntero(RegAlu.comision, 1, 5):
                RegAlu.comision = int(input("Incorrecto - numero de comision entre 1 y 5: "))
            carr = validarChar('S','M','Q','C')
            RegAlu.carrera = carr
            n1 = input("Ingrese nota 1er parcial entre 1 y 10: ")
            while validaRangoEntero(n1, 1, 10):
                n1 = input("Incorrecto entre 1 y 10: ")
            n1 = int(n1)
            n2 = input("Ingrese nota 2do parcial entre 1 y 10: ")
            while validaRangoEntero(n2, 1, 10):
                n2 = input("Incorrecto entre 1 y 10: ")
            n2 = int(n2)
            n3 = input("Ingrese nota 3er parcial entre 1 y 10: ")
            while validaRangoEntero(n3, 1, 10):
                n3 = input("Incorrecto entre 1 y 10: ")  
            n3 = int(n3)
            RegAlu.notas[0] = n1
            RegAlu.notas[1] = n2
            RegAlu.notas[2] = n3
            RegAlu.promedio= round((n1+n2+n3)/3, 2) # redondeo el decimal y guarda solo 2 decimales despues de la coma
            formatearAlumno(RegAlu)
            pickle.dump(RegAlu, ArcLogAlu)
            ArcLogAlu.flush()
            print ("-----------------------")
            print("Alta de Alumno exitosa")
            print ("-----------------------")
        else:
            print("Ya existe el Alumno con ese legajo, ingrese nuevamente..")
            os.system("pause")
        leg = input("Ingrese el legajo del Alumno a dar de alta, entre 1 y 9999 [0 para Volver]: ")
        while validaRangoEntero(leg, 0, 9999):
          leg = int(input("Incorrecto - Entre 1 y 9999 [0 para Volver]: "))
        

def pantalla():
    print('Menu de opciones');
    print('-----------------');
    print()
    print('1-Alta de Alumnos')
    print('2-Consulta de UN Alumno')
    print('3-Modificación campo comisión y/o Carrera')
    print('4-Listado completo del archivo')
    print('5-Listado de alumnos con Promedio mayor a 8')
    print('6-Baja lógica')
    print('7-Listado de alumnos ordenado por promedio descendente')
    print('8-salir')
    print()


### Programa Principal ###
ArcFisiAlu = "C:\\fuck ultad\\TP Algorritmos\\ejemplos registros\\alumnos.dat"   
if not os.path.exists(ArcFisiAlu):   
    ArcLogAlu = open(ArcFisiAlu, "w+b")   
else:
    ArcLogAlu = open(ArcFisiAlu, "r+b")   
opc = -1
while (opc != 8):
    os.system("cls")
    pantalla()
    opc = input("Ingrese opcion <1 a 8>: ")
    while (validaRangoEntero(opc, 1, 8)):
        opc = input("Incorrecto. Ingrese opcion <1 a 8>: ")
    opc = int(opc)
    if (opc == 1):
        Altas()
    elif (opc == 2):
        ConsultaAlumno()
    elif (opc == 3):
        ModificaCampo()
    elif (opc == 4):
        ListaAlumnos()
    elif (opc == 5):
        ListaAlumnosPromeMayor8()
    elif (opc == 6):
        BajaLogicaBlanqueoCampos()
    elif (opc==7):
        ListaxPromeDescendente()
    elif (opc == 8):    
        ArcLogAlu.close()    
        print("\n\n archivo cerrado ..Fin del programa!!")
print("\n\n CHAU!!!!")
input()