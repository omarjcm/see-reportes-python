import openpyxl
# Esto es para acceder a la fecha y hora del computador
from datetime import datetime
from report_excel import *

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

agregar_imagen( sheet )

ws = wb.active
ws.oddHeader.left.color = 'CC3366'

agregar_titulo( ws )

wb.save(nombre_archivo)








