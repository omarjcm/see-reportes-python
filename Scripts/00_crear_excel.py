import openpyxl
from os import path

def cargar_archivo( ruta_archivo ):
    if path.exists( ruta_archivo ):
        return openpyxl.load_workbook( ruta_archivo )
    else:
        return openpyxl.Workbook()


ruta = '../Data/test.xlsx'
wb = cargar_archivo( ruta )
'''
    Por default se me crea una hoja en el archivo, esta
    hoja se denomina como 'Sheet'.
'''
hoja = wb["Sheet"]
hoja.title = 'Habitos'

habitos = [
        (1, 'Leer ciencia ficción.'),
        (2, 'Ir al cine.'),
        (3, 'Comer cosas raras una vez al mes.'),
]

for habito in habitos:
    hoja.append( habito )

wb.save( ruta )