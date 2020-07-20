import matplotlib.pyplot as plt

#################img is stored as an array in "img" variable
img = plt.imread('Squares.png')

#plt.imshow(img)

#plt.show()

#plt.imshow(img, cmap='gray')
#plt.show()

##Contents of "img" variable
#print(img)

##print dimensions of img array
#print(img.shape)


##To show top left square
#print(img[:150 , :150])
#plt.imshow(img[:150 , :150])
#plt.show()

##To show center square
#plt.imshow(img[75:225, 75:225])
#plt.show()

##Save the above center square in another variable
#img1 = img[75:225 , 75:225]
#plt.imshow(img1)
#plt.show()

##reduce the axes step by 2
#print(img[::2,::2])
#plt.imshow(img[::2,::2])
#plt.show()

##reduce the axes step by 4
#plt.imshow(img[::4,::4])
#plt.show()

#============================RGB img: Python.png==============================

img0 = plt.imread('Python.png')
#plt.imshow(img0)
#plt.show()

#print(img0.shape)   # o/p: (600, 600, 4) -> (height, width, [red, green, blue, transparency value])

##display specific channel : R-0 G-1 B-2 Trans-3 
plt.imshow(img0[:,:,0])     # 0 - Red channel
plt.show()
