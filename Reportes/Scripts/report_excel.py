import openpyxl

def agregar_imagen( sheet ):
    img = openpyxl.drawing.image.Image('../Data/image/see_webinar.png')
    sheet.add_image( img, 'A1' )
