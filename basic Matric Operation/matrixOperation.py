######################from numpy import matrix,asmatrix,arange,allclose,eye,diag
import numpy as np
from numpy.linalg import det,inv,eig

m1 = matrix([1,2,3,4])

#print(m1)

#print(m1.shape)

#   asmatrix:covert array into matrix
#arr = np.array([1,2,3,4,5,6,7,8])
#mat1 = asmatrix(arr.reshape(2,4))
#mat1 = asmatrix(arange(1,9).reshape(2,4))


#===========Matrix Operations===========================
m1 = asmatrix(arange(1,9).reshape(2,4))
m2 = asmatrix(arange(9,17).reshape(2,4))

#print(m1+m2)
#print(m2-m1)

#print(m1 * (m2.reshape(4,2)))       #changes in dimensions are made to satisfy rules of matrix multiplication

#print( 6.5 * m1)
#print(m1/m2)

######################

#print(m1.T)         #Transpose of matrix

#m3 = matrix([[2,-3,1],[2,0,-1],[1,4,5]])
#print(det(m3))      #Determinant of matrix

#print(inv(m3))

# eye(3):returns identity matrix 3 x 3
# allclose(): to check to matrices are equal or not
#allclose returns True or False
#   multiplictn of : matrix * inverse of matrix  = identity matrix
#print(allclose( inv(m3) * m3 , asmatrix(eye(3)) ))  

m4 = asmatrix(diag((1,2,3)))    # diagonal arrangement of values
#print(m4)

#Eiegn vector
print(eig(m4))

print(eig(m4)[0])
print(eig(m4)[1])
