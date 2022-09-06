import pickle
import os
import io

class cubano:
    def init(self):
        self.name = " "
        self.dni = 0

seguenziaAF = 'C:\\fuck ultad\\TP Algorritmos\\ejemplos registros\\seguenzia.dat'
seguenziaAL = open(seguenziaAF, "w+b")

def BuscaSec(dni):
    global seguenziaAF, seguenziaAL
    t = os.path.getsize(seguenziaAF)
    pos=0
    seguenziaAL.seek(0, 0) 
    vrAlu = cubano() 
    if t>0:
        vrAlu = pickle.load(seguenziaAL)
        while (seguenziaAL.tell()<t) and (int(dni) != int(vrAlu.dni)):
            pos = seguenziaAL.tell()
            vrAlu = pickle.load(seguenziaAL)
        if int(vrAlu.dni) == int(dni):
            return pos
        else:
            return -1

registroseguenzia = cubano()
coso = input("decime el nombre ")
registroseguenzia.name = coso
dni = int(input("decime el dni "))
registroseguenzia.dni = dni
pickle.dump(registroseguenzia, seguenziaAL)
seguenziaAL.flush()
print("ya ta")
seguenziaAL.close()

# dni = input("pasame el dni")
# pos = BuscaSec(dni) # el ordenamiento es por el campo promedio, por eso acá llamo a busca secuencial x legajo
# if (pos == -1):
#     print ("Legajo no Encontrado")
# else:
#     print ("Legajo Encontrado") # mostrar los campos de ESE solo alumno 
#     seguenziaAL.seek(pos,0)
#     RegAlu= pickle.load(seguenziaAL)
#     print ("Nombre: ",RegAlu.name)
#     print ("Nombre: ",RegAlu.dni)
