def obtine_numero_celdas(archivo):
    numero_celdas = int(archivo.readline().rstrip("\n"))
    return numero_celdas

def genera_celdas_braille(archivo, numero_celdas):
    #linea 1 y crea la lista de celdas
    braille = archivo.readline().rstrip("\n").split(" ")
    #linea 2
    linea = archivo.readline().rstrip("\n").split(" ")
    for i in range(0,numero_celdas):
        braille[i] += linea[i]
    #linea 3
    linea = archivo.readline().rstrip("\n").split(" ")
    for i in range(0,numero_celdas):
        braille[i] += linea[i]

    return braille

def leer_entrada(nombre):
    ar = open(nombre,"r")
    numero_celdas = obtine_numero_celdas(ar)
    braille = genera_celdas_braille(ar, numero_celdas)
    ar.close()
    return braille

def abecedario_braille():
    abecedario = (".***..","*.....","*.*...","**....","**.*..","*..*..","***...","****..","*.**..",".**...")
    return abecedario

def traducir(braille):
    abecedario = abecedario_braille()
    resultado = ""
    for celda in braille:
        resultado += str(abecedario.index(celda))
    return resultado

def mensaje_salida(salida):
    ar = open("mensaje_out.txt","w")
    ar.write(salida)
    ar.close()

if __name__ == "__main__":
    braille = leer_entrada("mensaje_in.txt")
    salida = traducir(braille)
    mensaje_salida(salida)