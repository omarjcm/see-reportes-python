import openpyxl
from openpyxl.styles import Border, Side, PatternFill
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

thin = Side(border_style='thin', color='0089bb')
titulo_border = Border(top=thin, bottom=thin, left=thin, right=thin)
titulo_rect = PatternFill('solid', fgColor='0089bb')

ws.merge_cells( 'A5:N5' )
top_left_cell = ws['A5']
top_left_cell.value = 'Reporte de los Países'
top_left_cell.border = titulo_border
top_left_cell.fill = titulo_rect

wb.save(nombre_archivo)








