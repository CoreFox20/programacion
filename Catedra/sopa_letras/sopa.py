
def obtiene_dimensiones(archivo):
    dimensiones = archivo.readline().rstrip("\n").split(" ")
    dimensiones[0] = int(dimensiones[0])
    dimensiones[1] = int(dimensiones[1])
    return dimensiones
    
def generar_tablero(archivo,dimensiones):
    tablero = []
    for i in range(0,dimensiones[0]):
        linea = archivo.readline().rstrip("\n")
        tablero.append(linea)
    return tablero

def obtiene_palabras(archivo):
    numero_palabras = int(archivo.readline().rstrip("\n"))
    palabras = []
    for i in range(0,numero_palabras):
        linea = archivo.readline().rstrip("\n")
        palabras.append(linea)
    return palabras

def leer_archivo(nombre):
    ar = open(nombre)
    dimensiones = obtiene_dimensiones(ar)
    tablero = generar_tablero(ar,dimensiones)
    palabras = obtiene_palabras(ar)
    ar.close()
    return tablero, dimensiones, palabras

def invertir_palabra(palabra):
    palabra = palabra[::-1]
    return palabra

def obtener_posicion_inicial(palabra,fila,invertido):
    fila = list(fila)
    comprueba = True
    i = 0
    columna = 0
    while comprueba == True:
        if fila[i] == palabra[0]:
            columna = i
            if invertido==False:
                if fila[columna+1] == palabra[1]:
                    comprueba = False
                else:
                    i=i+1
            if invertido==True:
                if fila[columna-1] == palabra[1]:
                    comprueba = False
                else:
                    i=i+1
        else:
            i+=1
    return columna + 1 

def transpuesta(tablero):
    columnas = []
    for x in range(0,len(tablero[0])):
        columna = ""
        for fila in tablero:
            columna += fila[x]
        columnas.append(columna)
    return(columnas)

def invertir_tablero(tablero):
    tablero_invertido = []
    for fila in tablero:
        fila = list(fila)
        fila.reverse()
        nueva_fila = ""
        for i in fila:
            nueva_fila += i
        tablero_invertido.append(nueva_fila)
    return tablero_invertido

def obtiene_nuevo_tablero(tablero):
    nuevo_tablero = []
    for fila in tablero:
        fila = list(fila)
        for i in range(1,len(tablero[0])):
            fila.append("#")
        nuevo_tablero.append(fila)
    
    for i in range(1,len(tablero[0])):
        nuevafila = []
        for i in range(1,len(tablero[0])*2):
            nuevafila.append("#")
        nuevo_tablero.append(nuevafila)

    return nuevo_tablero

def obtener_diagonales(tablero):
    tablero_para_diagonal = obtiene_nuevo_tablero(tablero)
    diagonales = []
    for fila in range(len(tablero)-1,-1,-1):
        diagonal = ""
        for i in range(0,len(tablero[0])):
            diagonal += tablero_para_diagonal[(fila+i)][i]
        diagonales.append(diagonal)
    for columna in range(1,len(tablero[0])):
        diagonal = ""
        for i in range(0,len(tablero[0])):
            diagonal += tablero_para_diagonal[(i)][columna+i]
        diagonales.append(diagonal)
    return diagonales

def horizontal(tablero, palabra):
    esta = False
    nfila = 1
    pos_inicial = ""
    pos_final = ""
    for fila in tablero:
        if fila.find(palabra) != -1:
            pos_inicial = [nfila, fila.find(palabra) + 1]
            pos_final = [nfila, int(pos_inicial[1]) + (len(palabra) - 1)]
            esta = True
            break
        if fila.find(invertir_palabra(palabra)) != -1:
            pos_final = [nfila, fila.find(invertir_palabra(palabra)) + 1]
            pos_inicial = [nfila, int(pos_final[1]) + (len(palabra) - 1)]
            esta = True
            break
        nfila += 1
    return esta, pos_inicial, pos_final

def vertical(tablero,palabra):
    esta = False
    ncolumna = 1
    pos_inicial = ""
    pos_final = ""
    for columna in tablero:
        if palabra in columna:
            esta = True
            pos_inicial = [obtener_posicion_inicial(palabra, columna, invertido = False),ncolumna]
            pos_final = [int(pos_inicial[0]) + (len(palabra)-1),ncolumna]
            break
        ncolumna +=1
    if esta == False: # comprobar el inverso
        ncolumna = 1
        for columna in tablero:
            if invertir_palabra(palabra) in columna:
                esta = True
                pos_inicial = [obtener_posicion_inicial(palabra, columna, invertido = True),ncolumna]
                pos_final = [int(pos_inicial[0]) - (len(palabra)-1),ncolumna] 
                break
            ncolumna +=1
    return esta, pos_inicial, pos_final

def fila_columna_diagonal(ndiagonal,diagonal,diagonales,ubicacion):
    if ndiagonal > len(diagonales) - (len(diagonal)-1):
        columna = (ndiagonal - len(diagonales) - (len(diagonal)-1)) + ubicacion
        fila = ubicacion
    else:
        fila = (len(diagonales) - (len(diagonal)-1)  - ndiagonal) + ubicacion
        columna = ubicacion

    return [fila,columna]

def posicion_inicial_diagonal(palabra,diagonal,diagonales,ndiagonal,invertido):
    diagonal = list(diagonal)
    comprueba = True
    i = 0
    ubicacion = 0
    while comprueba == True:
        if diagonal[i] == palabra[0]:
            ubicacion = i
            #comprueba el siguiente caracter
            if invertido == False:
                if diagonal[ubicacion+1] == palabra[1]:
                    comprueba == False
                    ubicacion += 1
                    break
            if invertido == True:
                if diagonal[ubicacion-1] == palabra[1]:
                    print("si")
                    comprueba == False
                    ubicacion += 1
                    break
            i+=1
        else:
            i+=1
        
    posicion = fila_columna_diagonal(ndiagonal,diagonal,diagonales,ubicacion)
    return posicion

def fila_columna_diagonal_2(ndiagonal,diagonal,diagonales,ubicacion):
    if ndiagonal > len(diagonales) - (len(diagonal)-1):
        columna = len(diagonales) - (ndiagonal-2) - ubicacion
        fila = ubicacion
    else:
        fila = ((len(diagonales) - (len(diagonal)-1)) - ndiagonal) + ubicacion
        columna = len(diagonal) - (ubicacion-1)
    return [fila,columna]

def posicion_inicial_diagonal_2(palabra,diagonal,diagonales,ndiagonal,invertido):
    diagonal = list(diagonal)
    comprueba = True
    i = 0
    ubicacion = 0
    while comprueba == True:
        if diagonal[i] == palabra[0]:
            ubicacion = i
            if invertido == False:
                if diagonal[ubicacion+1] == palabra[1]:
                    comprueba == False
                    ubicacion += 1
                    break
            if invertido == True:
                if diagonal[ubicacion-1] == palabra[1]:
                    comprueba == False
                    ubicacion += 1
                    break
            i += 1
        else:
            i += 1
    posicion = fila_columna_diagonal_2(ndiagonal,diagonal,diagonales,ubicacion)
    return posicion
    
def diagonal_horizontal(diagonales,palabra):
    esta = False
    ndiagonal = 1
    pos_inicial = ""
    pos_final = ""
    for diagonal in diagonales:
        if palabra in diagonal:
            esta = True
            pos_inicial = posicion_inicial_diagonal(palabra,diagonal,diagonales,ndiagonal, invertido=False)
            pos_final = [pos_inicial[0] + (len(palabra) - 1), pos_inicial[1] + (len(palabra) - 1)]
            break
        ndiagonal += 1
    if esta == False:
        ndiagonal = 1
        for diagonal in diagonales:
            if invertir_palabra(palabra) in diagonal:
                esta = True
                pos_inicial = posicion_inicial_diagonal(palabra,diagonal,diagonales,ndiagonal, invertido=True)
                pos_final = [pos_inicial[0] - (len(palabra) - 1), pos_inicial[1] - (len(palabra) - 1)] 
                break
            ndiagonal += 1
    return esta, pos_inicial, pos_final

def diagonal_vertical(diagonales,palabra):
    esta = False
    ndiagonal = 1
    pos_inicial = ""
    pos_final = ""
    for diagonal in diagonales:
        if palabra in diagonal:
            esta = True
            pos_inicial = posicion_inicial_diagonal_2(palabra,diagonal,diagonales,ndiagonal, invertido=False)
            pos_final = [pos_inicial[0] + (len(palabra)-1), pos_inicial[1] + (len(palabra)-1)]
            break
        ndiagonal += 1
    if esta == False:
        ndiagonal = 1
        for diagonal in diagonales:
            if invertir_palabra(palabra) in diagonal:
                esta = True
                pos_inicial = posicion_inicial_diagonal_2(palabra,diagonal,diagonales,ndiagonal, invertido=True)
                pos_final = [pos_inicial[0] - (len(palabra)-1), pos_inicial[1] + (len(palabra)-1)] 
                break
            ndiagonal += 1
    return esta, pos_inicial, pos_final

def verificar(tablero, palabra):
    esta, pos_inicial, pos_final = horizontal(tablero,palabra)
    if esta == False:
        esta, pos_inicial, pos_final = vertical(transpuesta(tablero),palabra)
    if esta == False:
        esta, pos_inicial, pos_final = diagonal_horizontal(obtener_diagonales(tablero),palabra)
    if esta == False:
        esta, pos_inicial, pos_final = diagonal_vertical(obtener_diagonales(invertir_tablero(tablero)),palabra)   
    
    return esta, pos_inicial, pos_final
    
def procesar(tablero, palabras):
    resultado = []
    for palabra in palabras:
        esta, pos_inicial, pos_final = verificar(tablero,palabra)
        if esta == True:
            posiciones = str(pos_inicial[0]) + " " + str(pos_inicial[1]) + " " + str(pos_final[0]) + " " + str(pos_final[1]) +"\n"
            resultado.append(posiciones)
        else:
            resultado.append("???"+"\n")
    return resultado

def crear_archivo(resultado):
    resultado[-1] = resultado[-1].rstrip("\n")
    ar = open("SOP.RES","w")
    for posicion in resultado:
        ar.write(posicion)
    ar.close()

if __name__ == "__main__":
    tablero, dimensiones, palabras = leer_archivo("SOP.DAT")
    resultado = procesar(tablero, palabras)
    crear_archivo(resultado)