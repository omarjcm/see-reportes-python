import openpyxl
from funciones import *

# Esto es un script
ruta = '../Data/test.xlsx'

wb = cargar_archivo( ruta )
hoja = obtener_hoja(wb, 'Habitos')
hoja.insert_rows(1, 2)

for col_idx, valor in enumerate(('Número de Serie', 'Hábitos'), start=1):
    hoja.cell( row=1, column=col_idx, value=valor )
    
wb.save( ruta )