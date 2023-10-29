
def leer_datos(nombre):
    ar = open(nombre)
    cadenas = []
    for linea in ar:
        cadenas.append(linea.rstrip("\n"))
    cadenas.pop(0)
    ar.close()
    return cadenas

def nucleotidos():
    nucleotidos = {"A": 1, "C": 2, "G":3 ,"T": 4}
    return nucleotidos

def desorden(cadena):
    indice = 0
    dic = nucleotidos()
    numero = 0
    for letra in cadena:
        for i in range(indice,len(cadena)):
            if dic[letra] > dic[cadena[i]]:
                numero += 1
        indice += 1
    return numero 

def procesar(cadenas):
    lista = []
    for cadena in cadenas:
        n = desorden(cadena)
        lista.append([cadena,n])
    return lista

def ordenar(cadenas_procesadas):
    ordenado = []
    for cadena in cadenas_procesadas:
        if len(str(cadena[1])) == 1:
            ordenado.append("00"+str(cadena[1])+cadena[0])
        if len(str(cadena[1])) == 2:
            ordenado.append("0"+str(cadena[1])+cadena[0])
        if len(str(cadena[1])) > 2:
            ordenado.append(str(cadena[1])+cadena[0])
    ordenado.sort()
    salida = []
    for cadena in ordenado:
        salida.append(cadena[3:])
    return salida

def archivo_salida(cadenas_ordenadas):
    ar = open("ADN.RES","w")
    for cadena in cadenas_ordenadas:
        ar.write(cadena+"\n")
    ar.close

if __name__ == "__main__":
    cadenas = leer_datos("ADN.dat")
    cadenas_procesadas = procesar(cadenas)
    cadenas_ordenadas = ordenar(cadenas_procesadas)
    archivo_salida(cadenas_ordenadas)