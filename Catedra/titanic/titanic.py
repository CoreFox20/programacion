
def leer_archivo(nombre):
    ar = open(nombre)
    datos = []
    for linea in ar:
        datos.append(linea.rstrip("\n").split(","))
    return datos

def sobrevive(datos, parametros):
    sobrevivientes = 0
    for pasajero in datos:
        sobrevivientes += int(pasajero[1])
    parametros.append(f"sobrevivientes: {sobrevivientes}")
    return sobrevivientes

def mujeres_hombres(datos, parametros):
    mujeres = 0
    for pasajero in datos:
        mujeres += pasajero.count("female")
    parametros.append(f"mujeres:{mujeres}")
    hombres = 0
    for pasajero in datos:
        hombres += pasajero.count("male")
    parametros.append(f"hombres:{hombres}")
    return mujeres, hombres

def clases(datos,parametros):
    clase_1 = 0
    clase_2 = 0
    clase_3 = 0
    for pasajero in datos:
        clase_1 += pasajero[0].count("1")
        clase_2 += pasajero[0].count("2")
        clase_3 += pasajero[0].count("3")
    parametros.append(f"1er clase: {clase_1}")
    parametros.append(f"1er clase: {clase_2}")
    parametros.append(f"1er clase: {clase_3}")
    return clase_1, clase_2, clase_3

def embarcar(datos,parametros):
    c = 0
    q = 0
    s = 0
    for pasajero in datos:
        c += pasajero[10].count("C")
        q += pasajero[10].count("S")
        s += pasajero[10].count("Q")
    parametros.append(c)
    parametros.append(q)
    parametros.append(s)
    return c, q, s

def procesar(datos):
    parametros = []
    sobrevivientes = sobrevive(datos, parametros)
    mujeres, hombres = mujeres_hombres(datos, parametros)
    clase_1, clase_2, clase_3 = clases(datos, parametros)
    cherburgo , queenstown, southampton = embarcar(datos, parametros)

    for i in range(0,len(parametros)):
        print(parametros[i])

if __name__ == "__main__":
    datos = leer_archivo("titanic3.txt")
    procesar(datos)
