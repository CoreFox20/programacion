class Persona:
    def __init__(self,nom,ide,edad):
        self.nombre = nom
        self.identidad = ide
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}\nCedula: {self.identidad}\nEdad: {self.edad}")

if __name__ == "__main__":
    datos = input(">>>")
    datos = datos.split(",")
    dic = {}
    for i in range(0,10):
        dic[i] = Persona(datos[0],datos[1],datos[2])
  
    print(dic)
    