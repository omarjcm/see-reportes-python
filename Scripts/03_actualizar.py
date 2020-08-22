import openpyxl
from funciones import *

ruta = '../Data/test.xlsx'
wb = cargar_archivo( ruta )
hoja = obtener_hoja(wb, 'Habitos')

habitos = [
        ('Número de Serie', 'Hábitos'),
        (1, 'Leer ciencia ficción.'),
        (2, 'Ir al cine.'),
        (3, 'Comer cosas raras una vez al mes.'),
]

columna_indice = 5
hoja.insert_cols( columna_indice )

for fila_indice, valor in enumerate( habitos, start=1 ):
    serie, habito = valor
    hoja.cell( row=fila_indice, column=columna_indice, value=habito )

wb.save( ruta )