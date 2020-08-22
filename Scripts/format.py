print( 'Hola mundo' )

a = 'Hola'
b = 'mundo'
c = '!'
print( '{} {}{}'.format(a, b, c) )


nombre = 'Guillermo'
apellido = 'Pizarro'
correo = 'gpizarro@ups.edu.ec'
print( 'El correo de {} {} es {}.'.format(nombre, apellido, correo) )

edad = 37
nombre_apellido = nombre+' '+apellido
print( 'La edad de {} es {}.'.format(nombre_apellido, edad) )

print( '\n' )
print( 'La edad de ' + nombre + ' ' + apellido + ' es ' + str(edad) + '.' )

peso = 120.5/3.2

print( 'El peso de {} es {}'.format(nombre, peso) )
print( 'El peso de {} es {}'.format(nombre, round(peso, 2)) )