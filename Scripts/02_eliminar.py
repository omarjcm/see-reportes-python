import openpyxl
from funciones import *

ruta = '../Data/test.xlsx'
wb = cargar_archivo( ruta )
hoja = obtener_hoja(wb, 'Habitos')

hoja.delete_rows(2)
hoja.delete_cols(2)

wb.save( ruta )