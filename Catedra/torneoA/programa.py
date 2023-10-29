#!/usr/bin/python
# -*- coding: utf-8 -*-

#Declaración de funciones.
def leer_archivo(nombre):
    ar = open(nombre)
    objectos = []
    for linea in ar:
        linea = linea.rstrip("\n")
        objectos.append(linea)
    ar.close()
    return objectos

def verificar(lista):
    resultado = []
    for palabra in lista:
        if "i" in palabra:
            resultado.append("N"+"\n")
        else:
            resultado.append("S"+"\n")
    resultado[-1] = resultado[-1].rstrip("\n")
    return resultado

def salida(nombre, resultado):
    ar = open(nombre,"w")
    for linea in resultado:
        ar.write(linea)
    ar.close()

if __name__ == "__main__":
    objectos = leer_archivo("abuelo.txt")
    resultado = verificar(objectos)
    salida("salida.txt", resultado)