import matplotlib.pyplot as plt

img = plt.imread('kk(1).jpg')
#plt.imshow(img)
#plt.show()

a,b,c = img.shape
plt.imshow(img[:int(a/2),:int(b/2)])
plt.show()

