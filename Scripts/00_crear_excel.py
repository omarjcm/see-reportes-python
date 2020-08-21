import openpyxl

wb = openpyxl.Workbook()
hoja = wb["Sheet"]
hoja.title = 'Habitos'

habitos = [
        (1, 'Leer ciencia ficción.'),
        (2, 'Ir al cine.'),
        (3, 'Comer cosas raras una vez al mes.'),
]

for habito in habitos:
    hoja.append( habito )

ruta = '../Data/test.xlsx'
wb.save( ruta )