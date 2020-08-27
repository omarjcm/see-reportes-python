import openpyxl
from openpyxl.styles import Border, Side, PatternFill, Font, Alignment

thin = Side(border_style='thin', color='0089bb')
titulo_border = Border(top=thin, bottom=thin, left=thin, right=thin)
titulo_rect = PatternFill('solid', fgColor='0089bb')
titulo_font_big = Font(name='Calibri', size=16, b=True, color='ffffff')
titulo_alignment = Alignment(horizontal='center', vertical='center')

def agregar_imagen( sheet ):
    img = openpyxl.drawing.image.Image('../Data/image/see_webinar.png')
    sheet.add_image( img, 'A1' )

def agregar_titulo( ws ):
    ws.merge_cells( 'A5:N5' )
    top_left_cell = ws['A5']
    top_left_cell.value = 'Reporte de los Países'
    
    top_left_cell.border = titulo_border
    top_left_cell.fill = titulo_rect
    top_left_cell.font = titulo_font_big
    top_left_cell.alignment = titulo_alignment
    

