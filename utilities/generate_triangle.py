import py_seedlings as ps

DEPTH = 10
MIN_NUM = 0
MAX_NUM = 99
MAX_DIGITS = len(str(MAX_NUM))

import random

def zero_padded( integer ):

    string = str(integer)
    return '0'*(MAX_DIGITS-len(string))+string
    

string = ''
for row in range(1,DEPTH+1):
    row_string = '  '.join( [ zero_padded(random.randint( MIN_NUM, MAX_NUM )) for i in range(row) ]  )
    string += ( '  '*(DEPTH-row) + row_string + '\n')

print (string)
ps.write_text_file( '../prompts/3/triangle.txt', string ) 