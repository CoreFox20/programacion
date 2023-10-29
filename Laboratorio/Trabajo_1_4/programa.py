import tkinter as tk

def pedir_sueldo(entry,mensaje):
    sueldo = entry.get()
    if sueldo.isdigit() == True :
        sueldo = float(sueldo)
        aplicar_impuesto(sueldo,mensaje)
    else:
        mensaje["text"] = "Por favor ingrese un monto adecuado"
        
def generar_tabla():
    tabla = [(0,857452.5,1905450,3175750,4446050,5716350,7621800,19689650),(0,0.04,0.08,0.135,0.23,0.304,0.35,0.4),(0,34298.1,110516.1,285182.35,707557.1,1130567,1481169.8,2465652.3)]
    return tabla

def aplicar_impuesto(sueldo,label):
    tabla = generar_tabla()
    for i in range(0,len(tabla[0])):
        if float(sueldo) > tabla[0][i]:
            indice = i
        else:
            break 
    impuesto = (sueldo * tabla[1][indice]) - tabla[2][indice]
    restante = sueldo - impuesto
    porcentaje = "{:,.2f} %".format((impuesto/sueldo)*100)
    impuesto = "{:,.0f} $".format(impuesto)
    restante = "{:,.0f} $".format(restante)
    label["text"] = f"Impuestos a pagar: {impuesto}\n\nSueldo despues de impuestos: {restante}\n\nPorcentaje efectivo: {porcentaje}"

def interfaz():
    app = tk.Tk()
    app.geometry("600x400")
    app.title("Calculadora de Impuestos")
    
    intro_label = tk.Label(app,text="Ingrese el monto de su sueldo en pesos")
    intro_label.place(relx=0.5,rely=0.2,anchor="center")
    entrada_sueldo = tk.Entry()
    entrada_sueldo.config(justify="center")
    entrada_sueldo.place(relx=0.5,rely=0.3,anchor="center")
    boton = tk.Button(app, text = "INGRESAR",command= lambda: pedir_sueldo(entrada_sueldo,mensaje))
    boton.place(relx=0.5,rely=0.375,anchor="center")
    mensaje = tk.Label(app, text = "")
    mensaje.place(relx=0.5,rely=0.6,anchor="center")

    app.mainloop()

if __name__ == "__main__":
    interfaz()
