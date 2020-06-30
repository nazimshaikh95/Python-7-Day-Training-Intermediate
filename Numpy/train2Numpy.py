#========Script By NazimSK===

import numpy as np

file = np.loadtxt('student_record.txt', usecols = (3,4,5,6,7 ) , delimiter=';')

#=============================MATRIX MANIPULATION===========================================

#print('All Contents Of File : \n',file)

#print('\nMean =',np.mean(file[0]))

#print('\nMedian =',np.median(file[1]))

#print('\nStandard Deviation =',np.std(file[1]))

#print('\nSum = ',np.sum(file[2]))

#print('\n')

#for i in file:
 #   print(np.sum(i))
  #  c=c+1
   # if c==10:
    #    break

##print mean of nth "column" of matrix returned by 'np' object
#print('\nMean Column 0 : ',np.mean(file[:,0]))
#print('\nMean Column 1 : ',np.mean(file[:,1]))

##OR
#c=0
#total = 0
#for i in file:
  #  total = total + i[1]
   # c=c+1
#print('\nMean Column 1 : ',total/c)

##print mean of nth "row" of matrix returned by 'np' object
#print('\nMean row 0 : ',np.mean(file[0,:]))
#print('\nMean row 1 : ',np.mean(file[1,:]))


#===============================ARRAY MANIPULATION==========================================

arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr)

#shape method to represent the dimensions of array
print(arr.shape)

#reshape method to change dimensions of array
print(arr.reshape(4,2))
