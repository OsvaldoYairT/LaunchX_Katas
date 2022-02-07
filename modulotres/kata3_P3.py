# Kata 3, Problema 3
print ('Introduzca la velocidad del asteroide')
veloc_asteroide = int (input('La velocidad es: '))
print ('Introduzca el tamaño del asteroide')
tam_asteroide = int (input('El tamaño es: '))
#veloc_asteroide = 25
#tam_asteroide = 40
if veloc_asteroide > 25:
    print('Peligro!! Un asteroide viene hacia la Tierra!')
elif veloc_asteroide >= 20:
    print('Hay una luz en el cielo')
elif tam_asteroide < 25 and tam_asteroide <1000:
    print('Peligro, Causara daño en la Tierra!!!')
else:
    print('No hay peligro :)')