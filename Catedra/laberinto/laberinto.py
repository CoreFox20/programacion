
def generar(filas,columnas):
    laberinto = []
    for i in range(filas):
        laberinto.append([])
        for j in range(columnas):
            laberinto[i].append("0")
    return laberinto

def agregar_muros(laberinto,muros):
    for elem in muros:
        laberinto[elem[0]][elem[1]] = "X"

def construir_lab(filas,columnas):
    muros = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
    laberinto = generar(filas,columnas)
    agregar_muros(laberinto,muros)
    entrada = (0,0)
    salida = (4,4)
    return laberinto, entrada, salida

def recorrer(laberinto,pos,salida,movimientos):
    ejex = [0,1,0,-1]
    ejey = [-1,0,1,0]
    lista_mov = ["arriba","derecha","abajo","izquierda"]
    if pos != salida:
        laberinto[pos[0]][pos[1]] = "1"
        for comp in range(4):
            posy = pos[0] + ejey[comp]
            posx = pos[1] + ejex[comp]
            if posy >= 0 and posy < 5 and posx >= 0 and posx < 5:
                    if (laberinto[posy][posx] != "X") and (laberinto[posy][posx] == "0"):
                        movimientos.append(lista_mov[comp])
                        pos = (posy,posx)
                        if recorrer(laberinto,pos,salida,movimientos) == True:
                            return True
                        else:
                            movimientos.pop()
        return False
    else:
        return True

def procesar(laberinto,entrada,salida):
    pos = entrada
    movimientos = []
    a = recorrer(laberinto,pos,salida,movimientos)
    if a == True:
        print(movimientos)
    
if __name__ == "__main__":
    laberinto, entrada, salida = construir_lab(5,5)
    procesar(laberinto,entrada,salida)