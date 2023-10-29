#Angel Silva
#Ordena ascendentemente el primer millon de numeros 

def leer_datos(nombre):
    ar = open(nombre)
    lista = []
    for elem in ar:
        lista.append(int(elem.rstrip("\n")))
    ar.close()
    return lista

def ordenar(minimo,maximo,lista,ordenada):
    if maximo-1 < 1000000:
        sublista = lista[minimo:maximo]
        for n in sublista:
            ordenada.append(n)
        ordenada.sort()
        ordenar(minimo+20000,maximo+20000,lista,ordenada)
        return
    else:
        return

def procesar(lista):
    lista_ordenada = []
    ordenar(0,20000,lista,lista_ordenada)
    return(lista_ordenada)

def archivo_salida(lista_ord):
    ar = open("num_ord.txt","w")
    for num in lista_ord:
            ar.write(f"{num}\n")
    ar.close()

if __name__ == "__main__":
    lista = leer_datos("numeros.txt")
    lista_ordenada = procesar(lista)
    archivo_salida(lista_ordenada)