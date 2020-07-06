from numpy import asmatrix, arange, matrix
from numpy.linalg import inv, norm, svd
from numpy import inf, diag, allclose
from numpy.matlib import zeros

#a = asmatrix(arange(1,10).reshape(3,3))

#print(a.flatten())

m = asmatrix(arange(1,17).reshape(4,4))

m[0,1] = 0
m[1,3] = 0
#print(m)

im = inv(m)             #inverse of matrix
#print(norm(im))        #frobenius norm - by default norm() takes ord=fro i.e. frobenius norm

#print(norm(im,ord=inf)) #infinity normalization

#========SVD ( Single Value Decomposition ) ====================

m1 = matrix([[3,2,2],[2,3,-2]])

U, sigma, V_conjugate = svd(m1)
#print(U,'&&',sigma,'&&',V_conjugate)

smat = zeros((2,3))
#print(smat)
smat[:2 , :2] = diag(sigma)
#print(smat)

print(allclose(m1 , U * smat * V_conjugate))       #allclose() used to compare two matrices
                                                   #returns True if equal;
