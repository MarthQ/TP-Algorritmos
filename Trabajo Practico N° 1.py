
#INTEGRANTES: ALESANDRONI VALENTINO, RUIZ MILTON FRANCO, RADINS NICOLAS ARIEL, RODRÍGUEZ MARTINIANO.

#------------------------------------------> Limpiar Consola <----------------------------------------------

clearconsole = lambda: print('\n' * 150)

#---------------------------------------> MODULO DE ADMINISTRACIONES <--------------------------------------

# variables: op2: string

def MODULOADMINISTRACIONES():
    clearconsole()
    print(">>> BIENVENIDO AL MENU ADMINISTRACIONES <<<\n")
    print("A - TITULARES")
    print("B - PRODUCTOS")
    print("C - RUBROS")
    print("D - RUBROS x PRODUCTOS")
    print("E - SILOS")
    print("F - SUCURSALES")
    print("G - PRODUCTOS x TITULAR")
    print("V - VOLVER AL MENÚ PRINCIPAL\n")
    op2 = input('INGRESE UNA OPCIÓN: ')
    op2=op2.upper()
    print()
    while (op2!="V"):
        op2=op2.upper()
        if(op2=="A"):
            clearconsole()
            print(">>> TITULARES <<<")
            print()
            OPMENU()
        elif(op2=="B"):
            clearconsole()
            print(">>> PRODUCTOS <<<")
            print()
            OPMENU()
        elif(op2=="C"):
            clearconsole()
            print(">>> RUBROS <<<")
            print()
            OPMENU()
        elif(op2=="D"):
            clearconsole()
            print(">>> RUBROS x PRODUCTOS <<<")
            print()
            OPMENU()
        elif(op2=="E"):
            clearconsole()
            print(">>> SILOS <<<")
            print()
            OPMENU()
        elif(op2=="F"):
            clearconsole()
            print(">>> SUCURSALES <<<")
            print()
            OPMENU()
        elif(op2=="G"):
            clearconsole()
            print(">>> PRODUCTOS x TITULAR <<<")
            print()
            OPMENU()
        else:
            clearconsole()
            print("x ¡¡OPCION INVÁLIDA!! x")
            print()
        print(">>> BIENVENIDO AL MENU ADMINISTRACIONES <<<\n")
        print("A - TITULARES")
        print("B - PRODUCTOS")
        print("C - RUBROS")
        print("D - RUBROS x PRODUCTOS")
        print("E - SILOS")
        print("F - SUCURSALES")
        print("G - PRODUCTOS x TITULAR")
        print("V - VOLVER AL MENÚ PRINCIPAL\n")
        op2 = input('INGRESE UNA OPCIÓN NUEVAMENTE: ')
        op2=op2.upper()
    clearconsole()

#------------------> MODULO MENÚ DE OPCIONES <------------------------------

# variables: op3: string;

def OPMENU():
    print("A. ALTA")
    print("B. BAJA")
    print("C. CONSULTA")
    print("M. MODIFICACION")
    print("V. VOLVER AL MENÚ ANTERIOR\n")
    op3=input("INGRESE UNA OPCIÓN: ")
    op3=op3.upper()
    while(op3!="V"):
        if(op3=="A"):
            clearconsole()
            print(">>> ALTA <<<")
            print("Esta funcionalidad está en construccion...")
            print()
        elif(op3=="B"):
            clearconsole()
            print(">>> BAJA <<<")
            print("Esta funcionalidad está en construccion...")
            print()
        elif(op3=="C"):
            clearconsole()
            print(">>> CONSULTA <<<")
            print("Esta funcionalidad está en construccion...")
            print()
        elif(op3=="M"):
            clearconsole()
            print(">>> MODIFICACIÓN <<<")
            print("Esta funcionalidad está en construccion...")
            print()
        else:
            clearconsole()
            print("x ¡¡OPCION INVALIDA!! x")
            print()
        print("A. ALTA")
        print("B. BAJA")
        print("C. CONSULTA")
        print("M. MODIFICACIÓN")
        print("V. VOLVER AL MENÚ ANTERIOR\n")
        op3=input("INGRESE UNA OPCIÓN NUEVAMENTE: ")
        op3=op3.upper()
    clearconsole()

#-----------------------> MÓDULO DE REPORTES <------------------------------------

# variables: op5,opvolver: string; salir: integer;

def REPORTES():
    print(">>> BIENVENIDO AL MENU DE REPORTES <<<\n")
    print("¿Desea revisar los últimos datos ingresados? S/N\n")
    op5=input()
    op5=op5.upper()
    while (op5!="S" and op5!="N"):
        clearconsole()
        print("¡¡OPCION INVALIDA!!")
        print('¿Desea revisar los últimos datos ingresados? S/N\n')
        op5 = input()
        op5 = op5.upper()
    if (op5=="S"):
        clearconsole()
        salir=totalCamiones
        while (salir!=0):
            print(">>> BIENVENIDO AL MENU DE REPORTES <<<\n")
            print(f"Cantidad total de camiones que llegaron: {totalCamiones}")
            print(f"Cantidad total de camiones de soja: {camionesSoja}")
            print(f"Cantidad total de camiones de maíz: {camionesMaiz}")
            print(f"Peso neto total de soja: {netoSoja}")
            print(f"Peso neto total de maiz: {netoMaiz}")
            if (camionesSoja!=0):
                print(f"Promedio del peso neto de soja por camión: {promedioSoja/camionesSoja}")
            else:
                print("No se puede calcular el promedio de la doja.")
            if (camionesMaiz!=0):
                print(f"Promedio del peso neto de maiz por camión: {promedioMaiz/camionesMaiz}")
            else:
                print("No se puede calcular el promedio del maíz.")
            print(f"Patente del camion de soja que mayor cantidad de soja descargó: {patenteMayor}")
            print(f"Patente del camion de maiz que menor cantidad de maíz descargó: {patenteMenor}")
            salir=0
    print()
    opvolver=input("* Pulse cualquier tecla para volver al Menú Principal: ")
    clearconsole()
    
#------------------> MÓDULO DE RECEPCION <------------------------------------

# variables: totalCamiones,camionesSoja,camionesMaiz: intger;
#            netos,netom,netoSoja,netoMaiz,promedioSoja,promedioMaiz,mayor,menor,brutos,brutom,taras,taram: float;
#            opconteo,op4,producto,patentes,patentem: string;

def RECEPCION():
    clearconsole()
    print(">>>> ¿DESEA INICIAR UN NUEVO CONTEO/ELIMINAR EL ANTERIOR? S/N")
    opconteo=input()
    opconteo=opconteo.upper()
    while (opconteo!="S" and opconteo!="N"):
        print("Seleccione una opcion valida:")
        opconteo=input()
        opconteo=opconteo.upper()
    if (opconteo=="S"):
        global totalCamiones
        totalCamiones=0
        global camionesSoja
        camionesSoja=0
        global camionesMaiz
        camionesMaiz=0
        global netoSoja
        netoSoja=0
        global netoMaiz
        netoMaiz=0
        global patenteMayor
        patenteMayor=0
        global patenteMenor
        patenteMenor=0
        global netos
        netos=0
        global netom
        netom=0
        global promedioMaiz
        promedioMaiz=0
        global promedioSoja
        promedioSoja=0
        global mayor
        mayor=0
        global menor
        menor=0
    clearconsole()
    print("BIENVENIDO AL MENÚ RECEPCION\n")
    print("¿Desea ingresar un producto? S/N\n")
    op4=input()
    op4=op4.upper()
    while (op4!="S" and op4!="N"):
        clearconsole()
        print("¡¡OPCION INVALIDA!!")
        print('¿Desea ingresar un producto?  S / N\n')
        op4 = input()
        op4 = op4.upper()
    while (op4!="N"):
        clearconsole()
        print("Ingrese el nombre del producto, Soja o Maiz\n")
        producto=input()
        producto=producto.upper()
        clearconsole()
        while (producto!="SOJA" and producto!="MAIZ"):
            print("Ingrese nombre de producto correcto, Soja o Maiz")
            producto=input()
            producto=producto.upper()
            clearconsole()
        if (producto=="SOJA"):
            camionesSoja += 1
            print('>>> PRODUCTO INGRESADO: SOJA\n')
            print("Ingrese el número de patente:")
            patentes=input()
            print("Ingrese el peso bruto:")
            brutos=float(input())
            print("Ingrese tara:")
            taras=float(input())
            netos= brutos-taras
            netoSoja=netoSoja+netos
            promedioSoja=promedioSoja+netoSoja
            print('El peso para el camión',patentes,'es ',netos, 'kgs')
            if (netos>mayor):
                netos=mayor
                patenteMayor=patentes
        elif(producto=="MAIZ"):
            camionesMaiz +=1
            print('>>> PRODUCTO INGRESADO: MAÍZ\n')
            print("Ingrese el número de patente")
            patentem=input()
            print("Ingrese el peso bruto:")
            brutom=float(input())
            print("Ingresar tara:")
            taram=float(input())
            netom=brutom-taram
            netoMaiz=netoMaiz+netom
            promedioMaiz=promedioMaiz+netoMaiz
            print('El peso para el camión',patentem,'es ',netom, 'kgs')
            if (netom<menor or 0 == menor):
                menor = netom
                patenteMenor=patentem
        totalCamiones += 1
        print()
        print("¿Desea ingresar un producto? S/N")
        op4=input()
        op4=op4.upper()
    clearconsole()

#-----------------> MÓDULO DEL  PROGRAMA PRINCIPAL <------------------

# variables: op: integer;

def MENUP():
    clearconsole()
    print(">>> BIENVENIDO AL PROGRAMA PRINCIPAL <<<\n")
    print("1 - ADMINISTRACIONES")
    print("2 - ENTREGAS DE CUPOS")
    print("3 - RECEPCION")
    print("4 - REGISTRAR CALIDAD")
    print("5 - REGISTRAR PESO BRUTO")
    print("6 - REGISTRAR DESCARGA")
    print("7 - REGISTRAR TARA")
    print("8 - REPORTES")
    print("0 - FIN DEL PROGRAMA\n")
    op=input("INGRESE UNA OPCIÓN: ")
    while (op != "0"):
        if (op == "1"):
            MODULOADMINISTRACIONES()
        elif (op == "2"):
            clearconsole()
            print('* ENTREGAS DE CUPOS *')
            print("Esta funcionalidad está en construccion...")
            print()
        elif(op == "3"):
            RECEPCION()
        elif(op == "4"):
            clearconsole()
            print('* REGISTRAR CALIDAD *')
            print("Esta funcionalidad está en construccion...")
            print()
        elif(op == "5"):
            clearconsole()
            print('* REGISTRAR PESO BRUTO *')
            print("Esta funcionalidad está en construccion...")
            print()
        elif(op == "6"):
            clearconsole()
            print('* REGISTRAR DESCARGA *')
            print("Esta funcionalidad está en construccion...")
            print()
        elif(op == "7"):
            clearconsole()
            print('* REGISTRAR TARA *')
            print("Esta funcionalidad está en construccion...")
            print()
        elif(op == "8"):
            clearconsole()
            REPORTES()
        else:
            clearconsole()
            print("x ¡¡OPCIÓN INGRESADA INVÁLIDA!! x")
            print()
        print(">>> BIENVENIDO AL PROGRAMA PRINCIPAL <<<\n")
        print("1 - ADMINISTRACIONES")
        print("2 - ENTREGAS DE CUPOS")
        print("3 - RECEPCIÓN")
        print("4 - REGISTRAR CALIDAD")
        print("5 - REGISTRAR PESO BRUTO")
        print("6 - REGISTRAR DESCARGA")
        print("7 - REGISTRAR TARA")
        print("8 - REPORTES")
        print("0 - FIN DEL PROGRAMA\n")
        op=input("INGRESE UNA OPCIÓN NUEVAMENTE: ")
    print()
    print("¡Gracias por su visita, hasta pronto!")
    print()

#------------------------> M E N U <-------------------------------------

MENUP()