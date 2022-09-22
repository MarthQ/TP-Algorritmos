import pickle
import os
import io
import os.path


class cubano:
    def __init__(self):
        self.name = " "
        self.dni = 0

seguenziaAF = "C:\\fuck ultad\\TP Algorritmos\\ejemplos registros\\seguenzia.dat"
if not os.path.exists(seguenziaAF):
    seguenziaAL = open(seguenziaAF, "w+b")
else:
    seguenziaAL = open(seguenziaAF, "r+b")

def BuscaSec(coso):
    global seguenziaAF, seguenziaAL
    t = os.path.getsize(seguenziaAF)
    pos=0
    seguenziaAL.seek(0, 0) 
    vrAlu = cubano()
    if t>0:
        vrAlu = pickle.load(seguenziaAL)
        while (seguenziaAL.tell()<t) and (int(coso) != int(vrAlu.dni)):
            pos = seguenziaAL.tell()
            vrAlu = pickle.load(seguenziaAL)
        if int(vrAlu.dni) == int(coso):
            return pos
        else:
            return -1
    else:
        print('-----------------')
        print("Archivo sin datos")
        print('-----------------')
        input()
        return -1

os.system("cls")
opcion = -1
while opcion != 0:
    print("Bienvenido...")
    print("------- Este es el menú de prueba de archivos... -------")
    print("Opción 1- cargar algo que se yo")
    print("Opción 2- leer algo a lo mejor")
    print("0 - salir")
    opcion = int(input("ingrese su opción: "))
    while opcion < 0 or opcion > 2:
        opcion = int(input("PERO QUE HACES "))

    if opcion == 1:
        os.system("cls")
        registroseguenzia = cubano()
        coso = input("decime el nombre ")
        registroseguenzia.name = coso
        dni = int(input("decime el dni "))
        registroseguenzia.dni = dni
        pickle.dump(registroseguenzia, seguenziaAL)
        seguenziaAL.flush()
        sadsdas = input("ya ta, ingresa algo pa continuar")
        os.system("cls")

    if opcion == 2:
        os.system("cls")
        coso = input("pasame el dni ")
        pos = BuscaSec(coso) # el ordenamiento es por el campo promedio, por eso acá llamo a busca secuencial x legajo
        if (pos == -1):
            print ("no hay nada pa")
        else:
            print ("te encontre hdp") # mostrar los campos de ESE solo alumno 
            seguenziaAL.seek(pos,0)
            RegAlu = pickle.load(seguenziaAL)
            print ("Nombre: ",RegAlu.name)
            print ("DNI: ",RegAlu.dni)
        asdas = input("ingresame algo pa continuar")
        os.system("cls")

seguenziaAL.close()