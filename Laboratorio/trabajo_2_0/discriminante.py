import tkinter as tk

def determinante(a,b,c,label):
    a = int(a.get())
    b = int(b.get())
    c = int(c.get())
    resultado = (b**2) - 4*(a*c)
    if resultado < 0:
        label["text"] = f"El determinante es negativo\nLa ecuacion no tiene soluciones en los reales"
    if resultado == 0:
        label["text"] = f"El determinante es cero\nLa ecuacion tiene una unica solucion real"
    if resultado > 0:
        label["text"] = f"El determinante es positivo\nLa ecuacion tiene dos soluciones reales"

def inicializar():
    app = tk.Tk()
    app.geometry("600x400")
    app.title("calculadora discriminante")

    label1 = tk.Label(app,text="Escriba el valor del coeficiente A")
    label1.place(relx= 0.5,rely= 0.15,anchor="center")
    label2 = tk.Label(app,text="Escriba el valor del coeficiente B")
    label2.place(relx= 0.5,rely= 0.3,anchor="center")
    label3 = tk.Label(app,text="Escriba el valor del coeficiente C")
    label3.place(relx= 0.5,rely= 0.45,anchor="center")

    valor_a = tk.Entry(app)
    valor_a.place(relx= 0.5,rely= 0.2,anchor="center")
    valor_b = tk.Entry(app)
    valor_b.place(relx= 0.5,rely= 0.35,anchor="center")
    valor_c = tk.Entry(app)
    valor_c.place(relx= 0.5,rely= 0.5,anchor="center")
    resultado = tk.Label(app,text="")
    resultado.place(relx= 0.5,rely= 0.75,anchor="center")
    boton = tk.Button(text="Calcular",command= lambda: determinante(valor_a,valor_b,valor_c,resultado) )
    boton.place(relx= 0.5,rely= 0.6,anchor="center")

    app.mainloop()

if __name__ == "__main__":
    inicializar()