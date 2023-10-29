#Nombres: Matias Rodriguez y Angel Silva

def leer_archivo(archivo):
    ar = open(archivo)
    linea = ar.readline().rstrip("\n").split(";")
    coaliciones = []
    partidos = []
    for elem in linea:
        elem = elem.split(":")
        coaliciones.append(elem[0])
        partidos.append(elem[1])
    for col in partidos:
        partidos[partidos.index(col)] = col.split("-")
    votos = ar.readline().rstrip("\n")
    votos = votos.split("$")
    ar.close()
    return coaliciones, partidos, votos

def votos_partido(partido, votos):
    nv = votos.count(partido)
    return nv

def contar(partidos,votos):
    total_coaliciones = []
    total_partidos = []
    for col in partidos:
        voto = []
        suma_col = 0
        for partido in col:
            voto.append(votos_partido(partido,votos))
        for p in voto:
            suma_col += int(p)
        total_partidos.append(voto)
        total_coaliciones.append(suma_col)
    return total_partidos, total_coaliciones

def ganador(total_coalicion, coaliciones):
    ganadores = ""
    voto_ganadores = 0 
    i = 0
    for elem in total_coalicion:
        if elem == voto_ganadores:
            ganadores += "" + coaliciones[i]
        elif elem > voto_ganadores:
            ganadores = coaliciones[i]
            voto_ganadores = elem

        i += 1
    if ganadores.count(" ") > 0:
        return f"Empataron las coaliciones {ganadores} con {voto_ganadores} votos"
    else:
        return f"La coalicion ganadora es {ganadores} con {voto_ganadores} votos"

def ordenar(total_partidos, total_coalicion, coaliciones, partidos):
    output = ""
    i = 0
    for col in partidos:
        output += f"Coalicion: {coaliciones[i]}\n"
        j = 0
        for partido in col:
            output += f"{partido} {total_partidos[i][j]}\n"
            j += 1
        output += f"Total coalicion {coaliciones[i]} : {total_coalicion[i]}\n\n"
        i += 1
    output += ganador(total_coalicion, coaliciones)
    return output
    
def crear_archivo(resultado):
    ar = open("resultados.txt","w")
    ar.write(resultado)
    ar.close()

if __name__ == "__main__":
    coaliciones, partidos, votos = leer_archivo("datos.dat")
    total_partidos, total_coalicion = contar(partidos, votos)
    resultado = ordenar(total_partidos, total_coalicion, coaliciones, partidos)
    crear_archivo(resultado)