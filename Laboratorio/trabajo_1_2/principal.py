from tkinter import *

def leer_archivo(nombre):
    ar = open(nombre)
    boleta = []
    for linea in ar:
        linea = linea.rstrip("\n").split("|")
        linea = linea[1:-1]
        boleta.append(linea)
    ar.close()
    boleta = boleta[2:]
    return boleta

def cambio_fecha(fecha, fecha_seleccion, fecha_nueva):
    if fecha_seleccion != "" or fecha_nueva != "":
        fecha = fecha.replace(fecha_seleccion,fecha_nueva)
    return fecha

def filtrado(boleta):
    filtrado = ""
    for linea in boleta:
        if "-09-" in linea[2] and float(linea[13]) >= 40000:
            for elem in linea:
                filtrado += f"|{elem}"
            filtrado +="|\n"
    return filtrado
            
def procesar(boleta, fecha_seleccion, fecha_nueva, ventana):
    info = Label(ventana, text = "El procesamiento de datos fue realizado")
    info.place(relx=0.5, rely=0.55, anchor = "center")
    fecha_seleccion = fecha_seleccion.get()
    fecha_nueva = fecha_nueva.get()
    print(fecha_seleccion, fecha_nueva)
    arreglo = ""
    for linea in boleta:
        linea[2] = cambio_fecha(linea[2], fecha_seleccion, fecha_nueva)
        for elem in linea:
            arreglo += f"|{elem}"
        arreglo += "|\n"
    filtro = filtrado(boleta)
    salida(arreglo,filtro)

def salida(arreglo,filtro):
    ar = open("boletam.txt","w")
    ar.write(arreglo)
    ar.close()
    ar2 = open("ventasm94.dat","w")
    ar2.write(filtro)
    ar2.close()

if __name__ == "__main__":
    boleta = leer_archivo("boleta.txt")

    ventana = Tk()
    ventana.geometry("600x400")
    ventana.title("Boleta")
    var1 = StringVar()
    var2 = StringVar()
    instrucciones = Label(ventana,text="Por favor ingrese las fechas en el formato: YYYY-MM-DD")
    instrucciones.place(relx=0.5,rely=0.1,anchor="center")
    label1 = Label(ventana,text="Ingrese fecha a remplazar: ")
    label1.place(relx=0.275,rely=0.2)
    caja = Entry(ventana,textvariable=var1)
    caja.place(relx=0.525,rely=0.2)
    label2 = Label(ventana,text="Ingrese la nueva fecha: ")
    label2.place(relx=0.275,rely=0.3)
    caja2 = Entry(ventana,textvariable=var2)
    caja2.place(relx=0.525,rely=0.3)
    procesar_boton = Button(ventana,text="Procesar" , command= lambda: procesar(boleta,var1,var2,ventana))
    cerrar_boton = Button(ventana, text = "Salir" , command = quit)
    procesar_boton.place(relx=0.45,rely=0.425,anchor="center")
    cerrar_boton.place(relx=0.55,rely=0.425,anchor="center")
    
    ventana.mainloop()