from openpyxl.chart import PieChart, Reference
from funciones import cargar_archivo, obtener_hoja

ruta = '../Data/test.xlsx'
wb = cargar_archivo( ruta )
hoja = obtener_hoja(wb, 'Seguidores')

# Carga de imagen en un archivo en excel
imagen = openpyxl.drawing.image.Image('../Data/see.png')
hoja.add_image( imagen, 'A8' )

wb.save( ruta )