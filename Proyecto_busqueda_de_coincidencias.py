#Proyecto que buscara coincidencias de patrones en un directorio
from os import system, walk
import timeit
from datetime import date
import re
from pathlib import Path


#Busqueda coincidencias y numero total de coincidencias enontradas
def iteration():
    ruta = Path(r'D:\SD!!!!!!!!!!!!!!!!!!!!!!!!!1\Carrera Programacion\06Cursos python TOTAL\Mi_Gran_Directorio')
    while True:
        count = 0
        for carp, subcarp, archivo in walk(ruta):
            for sub in subcarp:
                pass
            for arch in archivo:
                contenido = Path(ruta,carp, arch)
                leer = contenido.read_text()
                pattern = r'N\w{3}-\d{5}'
                search = re.search(pattern, leer)
                if search:
                    count += 1
                    print(f'{search.group()}              {arch}')
        print(f'No de coincidencias: {count}')
        return
    

#Funcion que proporciona la fecha de la busqueda
def today():
    date_today = date.today()
    return date_today
hoy = today()

def inicio():
    system('cls')
    while True:
        print(f'Fecha de búsqueda: {hoy}')
        print('''
NRO. SERIE              ARCHIVO		        
-------		        ----------''')
        iteration()
        declaration = 'iteration'
        set_up = 'from __main__ import iteration'
        time = timeit.timeit(declaration, set_up, number = 10000000)
        print(f'Duración de la búsqueda: {round(time, 3)} segundos')
        break

inicio()
