import openpyxl
# Esto es para acceder a la fecha y hora del computador
from datetime import datetime
from report_excel import *
from report_data import *
from correo_electronico import *

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

cabecera = [
        'Country', 
        'Year', 
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

agregar_filtro(ws, sheet, cabecera)

agregar_datos(ws, sheet, cabecera)

wb.save(nombre_archivo)

destinatarios = ['gpizarro@ups.edu.ec', 'omarjcm@gmail.com', 'gpizarro@ieee.org']

for destinatario in destinatarios:
    enviar_correo( nombre_archivo, destinatario )







