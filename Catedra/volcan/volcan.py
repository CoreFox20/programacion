#!/usr/bin/python3
# -*- coding: utf-8 -*-

def lee_dimension(ar):
    dimension = ar.readline().rstrip('\n').split(' ')
    dimension[0] = int(dimension[0])
    dimension[1] = int(dimension[1])   
    return dimension

def lee_centro(ar):
    centro = ar.readline().rstrip('\n').split(' ')
    centro[0] = int(centro[0])
    centro[1] = int(centro[1])   
    return centro

def str_a_int(linea):
    i = 0
    while i < len(linea):
        linea[i] = int(linea[i])
        i = i + 1
    return linea

def lee_tablero(ar, filas):
    tablero = []
    i = 0
    while i < filas:
        linea = ar.readline().rstrip('\n').split(' ')
        linea = str_a_int(linea)
        tablero.append(linea)
        i = i + 1
    return tablero

def lee_altura(tablero, centro):
    altura = tablero[centro[0]-1][centro[1]-1]
    return altura

def genera_ladera(tablero, altura, dimension):
    fila0 = []
    i = 0
    while i < dimension[0] + 2:
        fila0.append(altura)
        i = i + 1
    ladera =[]
    ladera.append(fila0)
    i = 0
    while i < dimension[0]:
        ladera.append([altura]+tablero[i]+[altura])
        i = i + 1
    ladera.append(fila0)
    return ladera

def leer_datos(nombre):
    ar = open(nombre)
    dimension = lee_dimension(ar)
    centro = lee_centro(ar)
    tablero = lee_tablero(ar, dimension[0])
    altura = lee_altura(tablero, centro)
    ladera = genera_ladera(tablero, altura, dimension)
    respaldo = genera_ladera(tablero, altura, dimension)
    return ladera, respaldo, centro, altura

def que_paso_vecino(ladera, ladera_res, i, j):
    altura = ladera[i][j]
    altura = int(altura)
    verificaciones_i = [-1,-1,-1,0,1,1,1,0]
    verificaciones_j = [-1,0,1,1,1,0,-1,-1]

    for ind in range(0,8):    
        if ladera[i+verificaciones_i[ind]][j+verificaciones_j[ind]] < altura:
            ladera_res[i+verificaciones_i[ind]][j+verificaciones_j[ind]] = 'X'
            que_paso_vecino(ladera, ladera_res, i+verificaciones_i[ind], j+verificaciones_j[ind])      

def estallo_crater(ladera, respaldo, centro, altura):
    i = centro[0]
    j = centro[1]
    print("")
    que_paso_vecino(ladera,respaldo, i, j)
    return respaldo

def genera_archivo(mapa):
    mapa[-1] = mapa[-1].rstrip("\n")
    ar = open('VOLCAN.RES',"w")
    for fila in mapa:
        ar.write(fila)
    ar.close()

def genera_mapa(lava):
    mapa = []
    lava.pop(-1)
    lava.pop(0)
    for fila in lava:
        nueva_fila = ""
        fila.pop(-1)
        fila.pop(0)
        for columna in fila:
            nueva_fila += str(columna) + " "
        nueva_fila = nueva_fila.rstrip(" ")
        nueva_fila += "\n"
        mapa.append(nueva_fila)

    genera_archivo(mapa)

if __name__ == "__main__":
    ladera, respaldo, centro, altura = leer_datos('VOLCAN.DAT')
    lava = estallo_crater(ladera, respaldo, centro, altura)
    genera_mapa(lava)