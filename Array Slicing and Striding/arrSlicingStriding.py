import numpy as np

a = np.arange(1,26).reshape(5,5)
print(a)
print('================')
#print(a[0:5,0:4])           # a[ row_range, col_range ]
    #OR
#print(a[0:,0:4])

#print(a[0:4,0:5])
    #OR
#print(a[0:4,0:])

#print(a[2,0:4])

#print(a[2,1:])

#print(a[3,1:4])

#=====================Striding====================

#print(a[0::2,0:])           # a[ start : end : step ]

#print(a[0:,0::2])

print(a[::2,::2])
