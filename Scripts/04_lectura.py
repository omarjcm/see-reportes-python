import openpyxl
from funciones import *

ruta = '../Data/test.xlsx'
wb = cargar_archivo( ruta )
hoja = obtener_hoja(wb, 'Habitos')

for fila in hoja.values:
    serie, habito = fila
    print( '{} - {}'.format(serie, habito) )

wb.save( ruta )