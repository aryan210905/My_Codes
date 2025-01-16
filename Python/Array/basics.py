import array as arr

'''
typeCodes table:

'i' => signed int 4 bytes
'I' => unsigned int 4 bytes
'f' => floating point 4 bytes
'd' => double precision float 8 bytes
'b' => signed bytes 1 byte
'B' => unsigned bytes 1 byte
'h' => short integer 2 bytes
'u' => characters

'''

var = arr.array('i',[2,4,5,6,9,7])
print(var)
print(var.buffer_info())        # prints address and size of array
var.reverse()
print(var)
print(var[3])