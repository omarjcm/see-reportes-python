nombre, apellido, correo = ('Guillermo', 'Pizarro', 'gpizarro@ups.edu.ec')
print( nombre )
print( apellido )
print( correo )

estudiante = ('Guillermo', 'Pizarro', 'gpizarro@ups.edu.ec')

for indice, valor in enumerate( estudiante, start=1 ):
    print( 'Indice: {} Valor: {}'.format( indice, valor ) )

print('\n')
#estudiantes = [
#        ('Guillermo', 'Pizarro', 'gpizarro@ups.edu.ec'),
#        ('Omar', 'Vásquez', 'ovasquez@ups.edu.ec'),        
#        ('Néstor', 'Montaño', 'nmontano@see.org.ec')
#]
#
#for estudiante in estudiantes:
#    for indice, valor in enumerate( estudiante ):
#        print( valor )
#    print()
#
#    
habitos = [
        ('Número de Serie', 'Hábitos', 'Ranking'),
        (1, 'Leer ciencia ficción.', 3),
        (2, 'Ir al cine.', 5),
        (3, 'Comer cosas raras una vez al mes.', 3),
]

for indice, valor in enumerate( habitos, start=1 ):
    serie, habito, ranking = valor
    print( 'Indice: {} Habito: {}'.format(indice, habito) )

#print( [habito[1] for habito in habitos] )







