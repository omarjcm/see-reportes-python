import openpyxl
# Esto es para acceder a la fecha y hora del computador
from datetime import datetime

now = datetime.now()
'''
 %b  -> Mes
 %d  -> Día
 %Y  -> Año
 %H  -> Hora
 %M  -> Minutos
 %S  -> Segundos
'''
date_now = now.strftime( "%b-%d-%Y_%H-%M-%S" )

nombre_archivo = '../Data/reporte_see' + date_now + '.xlsx'
wb = openpyxl.Workbook()
sheet = wb['Sheet']
sheet.title = 'Reporte 1'

img = openpyxl.drawing.image.Image('../Data/image/see_webinar.png')
sheet.add_image( img, 'A1' )

wb.save(nombre_archivo)








