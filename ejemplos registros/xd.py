from copyreg import pickle
import os

class cubano:
    def init(self):
        self.name = "miguel oliveros vega"
        self.dni = -1324234
        self.armas = {"AK-47", "PALA", "METRALLETA", "FISICA I"}
        self.enemigos = "bibiana"

seguenziaAF = 'C:\\fuck ultad\TP Algorritmos\ejemplos registros\seguenzia.dat'
seguenziaAL = cubano()

seguenziaAL = open(seguenziaAF, "r+b")

coso = input("decime el coso ")
size = os.path.getsize(seguenziaAF)
seguenziaAL.seek(0, 0)

while seguenziaAL.tell() < size:
    RM = pickle.load(seguenziaAL)
    print("coso")