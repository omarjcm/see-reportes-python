import openpyxl
# Esto es para acceder a la fecha y hora del computador
from datetime import datetime
from report_excel import *

import pandas as pd

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


transacciones = pd.read_excel('../Data/transacciones_202008.xlsx')
transacciones['InvoiceDate'] = pd.to_datetime( transacciones['InvoiceDate'] )


wb.save(nombre_archivo)








