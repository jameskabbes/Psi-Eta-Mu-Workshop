import random
import py_seedlings as ps

N = 25
DIGITS = 8

pins = []
for i in range( N ):
    
    pin = ''
    for j in range ( DIGITS ):
        pin += str( random.randint( 1, 9 ) )

    pins.append(pin)

if ps.confirm_raw(string='This will overwrite previous pins.'):
    f = open( '../Data/valid_pins.txt', 'w' )
    f.write( '\n'.join( pins ) )
    f.close()