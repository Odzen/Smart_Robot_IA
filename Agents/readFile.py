# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 23:38:42 2022

@author: Juan Sebastian Velasquez
"""


nombreLectura = "maze"
nombreEscritura = "out"

'''
input()
Funcion para leer el archivo bajo el formato establecido la tarea. El
nombre se cambia en la variable global "nombreLectura". (No modificar)
'''

'''
Para cambiar el # de la prueba, solo cambie la variable global 'numeroPrueba', 
dependiendo de que prueba se quiera escoger del directorio Pruebas/Tests_in_files
'''
def input(numeroPrueba):
    with open("MazesTests/in/"+nombreLectura+str(numeroPrueba)+".txt", "r") as f:
        content = f.read().split('\n')
        lines = []
        width = len(content)
        for line in content:
            lines.append(list(map(lambda x: int(x), line.split(" "))))
        height = len(lines[0])
        #a = list(map(lambda x: int(x), content[0].split(" ")))
        #b = list(map(lambda x: int(x), content[1].split(" ")))
        #ab = list(map(lambda x: int(x), content[2].split(" ")))
        #ba = list(map(lambda x: int(x), content[3].split(" ")))
        return width, height, lines

'''
output()
Funcion para escribir sobre el archivo segun lo solicitado en el proyecto. El
nombre del archivo se cambia en la variable global "nombreEscritura". (No modificar método)
'''

'''
Las salidas de los archivos se guardaran la carpeta Pruebas/outDinamica/
Para la prueba ini.txt el archivo de salida sera outi.txt, siendo i el 
'numeroPrueba', variable global definida anteriormente
'''

def output(output, numeroOutput):
    n, time, lines = output
    toWrite = ""
    toWrite += str(n) + "\n"
    toWrite += str(time)
    for line in lines:
        toWrite += "\n" + str(line)

    with open("../../Pruebas/outDinamica/"+nombreEscritura+numeroOutput+".txt", "w") as f:
        f.write(toWrite)