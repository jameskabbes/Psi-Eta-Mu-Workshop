import random

N = 50
DIGITS = 8

pins = []
for i in range( N ):
    
    pin = ''
    for j in range ( DIGITS ):
        pin += str( random.randint( 1, 9 ) )

    pins.append(pin)

f = open( '../Data/valid_pins.txt', 'w' )
f.write( '\n'.join( pins ) )
f.close()