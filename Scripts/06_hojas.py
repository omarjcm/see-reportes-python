from funciones_excel import cargar_archivo, obtener_hoja

ruta = '../Data/test.xlsx'
wb = cargar_archivo( ruta )
hoja = obtener_hoja(wb, 'Habitos')

wb.create_sheet( title='Seguidores', index=0 )
wb.create_sheet( title='Proyectos', index=2 )

print( wb.worksheets )

seguidores = [
        ('Id', 'Dominio', 'Seguidores'),
        (1, 'Youtube', 3000),
        (2, 'Udemy', 115000)
]

hoja = wb['Seguidores']

for seguidor in seguidores:
    hoja.append( seguidor )
    
wb.save( ruta )