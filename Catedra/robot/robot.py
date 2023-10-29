
def en_int(lista):
    for i in range(0,len(lista)):
        lista[i] = int(lista[i])
    return lista

def generar(dimensiones,archivo):
    laberinto = []
    for i in range(0,dimensiones[0]):
        laberinto.append(archivo.readline().rstrip("\n").split(" "))
    return laberinto

def leer_datos(nombre):
    ar = open(nombre)
    tamaño = en_int(ar.readline().rstrip("\n").split(" "))
    laberinto = generar(tamaño,ar)
    inicio = en_int(ar.readline().rstrip("\n").split(" "))
    final = en_int(ar.readline().rstrip("\n").split(" "))
    orientacion = ar.readline().rstrip("\n")
    ar.readline()
    movimientos = ar.readline().rstrip("\n").split(" ")
    ar.close()
    return laberinto, inicio, final, orientacion, movimientos

def girar(orientacion,movimiento):
    puntos = ["N","E","S","O"]
    if movimiento == "D":
        index = (puntos.index(orientacion) + 1)%4
    if movimiento == "I":
        index = puntos.index(orientacion) - 1
    return puntos[index]

def comprobar(posicion,laberinto,i,j):
    if laberinto[posicion[0]+i][posicion[1]+j] == "0":
        return True
    else:
        return False

def avance(orientacion, laberinto, posicion):
    puntos = {"N":[-1,0],"E":[0,1],"S":[1,0],"O":[0,-1]}
    i = puntos[orientacion][0]
    j = puntos[orientacion][1]
    if comprobar(posicion,laberinto,i,j) == True:
        return [posicion[0]+i,posicion[1]+j]
    else:
        return False
    
def procesar(laberinto, inicio, final, orientacion, movimientos):
    pos = inicio
    for orden in movimientos:
        if orden == "D" or orden == "I":
            orientacion = girar(orientacion,orden)
        else:
            pos = avance(orientacion,laberinto,pos)
            if pos == False:
                return "Exploto"
    return "Correcto"

def archivo_salida(resultado):
    ar = open("ROBCOM.RES","w")
    ar.write(resultado)
    ar.close()

if __name__ == "__main__":
    laberinto, inicio, final, orientacion, movimientos = leer_datos("ROBCOM.DAT")
    resultado = procesar(laberinto, inicio, final, orientacion, movimientos)
    archivo_salida(resultado)