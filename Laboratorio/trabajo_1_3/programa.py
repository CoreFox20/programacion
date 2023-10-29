import tkinter as tk

def leer_datos(archivo):
    ar = open(archivo,"r")
    tasas = []
    for linea in ar:
        linea = linea.rstrip("\n").replace('"','').split(",")
        tasas.append(linea)
    ar.close()
    tasas.pop(0)
    return tasas

def procesar(datos):
    diccionario = {}
    for dato in datos:
        diccionario[dato[0]] = int(dato[3].split(".")[0])
    return diccionario

def busqueda(diccionario, comuna, label):
    comuna = comuna.lower().capitalize()
    comunas = diccionario.keys()
    if comuna in comunas and comuna != None:
        resultado = diccionario[comuna]
        label["text"] = f"Los casos activos de {comuna} son {resultado}"
    else:
        label["text"] = f"No se encontro la comuna"
        
def interfaz(diccionario):
    ventana = tk.Tk()
    ventana.title("contagios")
    ventana.geometry("600x400")
    canvas = tk.Canvas(width=400,height=300,bg="light blue")
    canvas.pack(expand=True)

    nombre_comuna = tk.StringVar()
    label = tk.Label(ventana,text="Ingrese Comuna:",background="light blue").place(relx=0.5,rely=0.2,anchor="center")
    entry = tk.Entry(textvariable=nombre_comuna)
    entry.place(relx=0.5,rely=0.3,anchor="center")
    boton = tk.Button(ventana,text="Buscar",command= lambda: busqueda(diccionario, nombre_comuna.get(), salida))
    boton.place(relx=0.5,rely=0.4,anchor="center")
    salida = tk.Label(ventana,text="",background="light blue")
    salida.place(relx=0.5,rely=0.5,anchor="center")

    ventana.mainloop()

if __name__ == "__main__":
    tasas = leer_datos("tasas.txt")
    diccionario = procesar(tasas)
    interfaz(diccionario)