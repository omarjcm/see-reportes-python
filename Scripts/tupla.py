
nombre, apellido, correo = ('Guillermo', 'Pizarro', 'gpizarro@ups.edu.ec')
#print( nombre )
#print( apellido )
#print( correo )

estudiante = ('Guillermo', 'Pizarro', 'gpizarro@ups.edu.ec')

#for indice, valor in enumerate( estudiante, start=1 ):
#    print( 'Indice: {} Valor: {}'.format( indice, valor ) )
    
estudiantes = [
        ('Guillermo', 'Pizarro', 'gpizarro@ups.edu.ec'),
        ('Omar', 'Vásquez', 'ovasquez@ups.edu.ec'),        
        ('Néstor', 'Montaño', 'nmontano@see.org.ec')
]

for estudiante in estudiantes:
    for indice, valor in enumerate( estudiante ):
        print( valor )
    print()