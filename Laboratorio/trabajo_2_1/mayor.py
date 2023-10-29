#Angel Silva
#Muestra en pantalla el numero mayor de una lista de 10 millones de numeros

def leer_datos(nombre):
    ar = open(nombre)
    lista = []
    for elem in ar:
        lista.append(int(elem.rstrip("\n")))
    ar.close()
    return lista

def mayor(indice,minimo,lista):
    if indice > minimo:
        numero = mayor(indice - 1, minimo, lista)
        if lista[indice] > numero:
            return lista[indice]
        else:
            return numero
    else:
        return lista[indice]

def procesar():
    ref = 0
    for i in range(11112):
        if i != 11111:
            maximo = 900*i + 900
            minimo = 900*i
        else:
            maximo = 10000000
            minimo = maximo - 100
        evaluar = mayor(maximo-1,minimo,lista)
        if evaluar > ref:
            ref = evaluar
    print("numero mayor: " + str(ref))

if __name__ == "__main__":
    lista = leer_datos("numeros.txt")
    procesar()