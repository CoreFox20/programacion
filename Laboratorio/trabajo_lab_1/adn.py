
def leer_archivo(nombre):
    ar = open(nombre)
    cadena = ""
    for linea in ar:
        cadena = list(linea.rstrip("/n"))
    ar.close()
    return cadena

def comprobacion(base):
    origen = ["A","T","G","C"]
    complemento = ["T","A","C","G"]
    return complemento[origen.index(base)]

def procesar(cadena):
    nueva_cadena = ""
    cadena_original = ""
    for base in cadena:
        nueva_cadena += comprobacion(base) + " "
        cadena_original += base + " "
    doble_cadena = ["N1: " + cadena_original+"\n", "N2: " + nueva_cadena] 
    return doble_cadena

def crear_archivo(doble_cadena):
    ar = open("hélice.dat","w")
    ar.write("Bases Nitrogenadas\n")
    for cadena in doble_cadena:
        ar.write(cadena)
    ar.close()

if __name__ == "__main__":
    cadena = leer_archivo("cadena.dat")
    doble_cadena = procesar(cadena)
    crear_archivo(doble_cadena)