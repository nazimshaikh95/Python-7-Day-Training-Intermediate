from numpy import loadtxt, array, ones_like
import matplotlib.pyplot as plt
from numpy.linalg import lstsq

L , t = loadtxt("pendulum.txt" , unpack = True)
tsq = t * t
#plt.plot(L , tsq, 'bo')
#plt.show()

inter_mat = array((L, ones_like(L)))
#print(inter_mat)

A = inter_mat.T             #Transpose of matrix inter_mat
#print(A)

result = lstsq(A, tsq, rcond=None)      #generate least square fit line
#print(result)

p = result[0]
m, c = p
#print(m,' & ',c)


tsq_fit = m * L + c
plt.plot(L, tsq, 'bo' )         # 'bo'- draw blue dots
plt.plot(L, tsq_fit, 'r' )      # 'r' - draw a line of red color
plt.show()
