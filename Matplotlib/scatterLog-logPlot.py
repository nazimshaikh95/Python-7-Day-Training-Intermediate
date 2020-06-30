from numpy import loadtxt, linspace
from matplotlib.pyplot import scatter
import matplotlib.pyplot as plt

year ,profit = loadtxt('company-a-data.txt', unpack = True)

#Scatter Plot

#plt.scatter(year,profit)
#plt.show()

#OR
#plt.show(scatter(year,profit))    #shows Deprecated warning


#Scatter Plot With Red Diamond Markers

#plt.show(scatter(year, profit, color = 'r', marker = 'd'))



#==Log-Log Plot=========
#For corresponding X,Y

x = linspace(1, 20, 100)    #           3
y = 5 * (x**3)              #i.e. y = 5x

plt.loglog(x,y)
plt.show()

